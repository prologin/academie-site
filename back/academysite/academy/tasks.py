from .camisole import Camisole
from . import models
import logging
from django.utils import timezone
import sys
from celery import shared_task

logger = logging.getLogger(__name__)

def test_passes(got, expected) -> bool:
    for g in got:
        expected_stdout = expected[g['name']]['stdout']
        if not (g['exitcode'] == 0 and expected_stdout == g['stdout']):
            return False
    return True

@shared_task
def run_code_submission(submission_id) -> bool:
    submission = None
    try:
        submission = models.Submission.objects.get(pk=submission_id)
    except:
        logger.error(f'[submission_run][id={submission_id}] Submission Not Found')
        return False
    
    code = submission.get_templated_code()
    tests = submission.problem.tests

    camisole_response = None
    try:
        camisole_response = Camisole.run(code, tests)
    except:
        e = sys.exc_info()[0]
        logger.error(f'[submission_run][id={submission_id}] Camisole request error : {e}')
        return False

    # if all checks are passing then the problem is solved
    passed = False
    try:
        passed = test_passes(camisole_response['tests'], submission.problem.tests)
    except:
        e = sys.exc_info()[0]
        logger.error(f'[submission_run][id={submission_id}] Camisole response malformed: {e}')
        return False
    
    
    submission.correction_date = timezone.now()
    submission.correction_data = camisole_response
    submission.passed = passed
    submission.save()

    return True