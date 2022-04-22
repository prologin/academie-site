from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from submissions.models import ProblemSubmissionCode
from django.conf import settings
from django.utils import timezone
import requests


class CamisoleException(Exception):
    pass


def run_in_camisole(lang: str, code: str, tests: list[dict[str, str]]):
    req = requests.post(
        settings.CAMISOLE_ENDPOINT_URL,
        json={"lang": lang, "source": code, "tests": tests},
    )

    result = req.json()

    if not result["success"]:
        raise CamisoleException("success false")

    return result


def test_passed(ref, given) -> bool:
    return ref["stdout"] == given["stdout"]


@shared_task(name="run_code_submission")
def run_code_submission(submission_code_id: str) -> None:
    try:
        subcode = ProblemSubmissionCode.objects.get(id=submission_code_id)
    except ObjectDoesNotExist:
        print("warning: submission deleted")
        return None

    sub = subcode.submission
    problem = sub.problem.problem

    try:
        res = run_in_camisole(
            subcode.language,
            subcode.code,
            tuple(
                {"name": t["name"], "stdin": t["stdin"]} for t in problem.tests
            ),
        )
    except (requests.HTTPError, CamisoleException):
        print(
            f"error: task {submission_code_id} failed to run : camisole returned error"  # noqa
        )
        return None

    if not res["success"]:
        print(
            f"error: task {submission_code_id} failed to run: camisole response success: false"  # noqa
        )
        return None

    result = dict()

    for given, ref in zip(res["tests"], problem.tests):
        result[ref["name"]] = given["stdout"] == ref["stdout"]

    validated = all(result.values())

    subcode.validated = validated
    if validated:
        sub.validated = True
    subcode.result = result
    subcode.date_corrected = sub.validated_at = timezone.now()
    subcode.save()
    sub.save()
