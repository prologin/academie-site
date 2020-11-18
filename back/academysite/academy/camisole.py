import requests
from django.conf import settings


class Camisole:
    @classmethod
    def _get_request_dict(cls):
        return {
            "lang": "python",
            "all_fatal": True,
            "execute": {
                "time": 20,
                "wall-time": 30,
            },
        }

    @classmethod
    def _convert_tests(cls, tests):
        out = []
        for name, test in tests.items():
            out.append({"name": name, "stdin": test["stdin"]})
        return out

    @classmethod
    def run(cls, code, tests):
        """
        This method may raise exceptions
        You should run it in a try...except block
        """
        body = cls._get_request_dict()
        body["source"] = code
        body["tests"] = cls._convert_tests(tests)

        req = requests.post(
            f"{settings.CAMISOLE_URL}/run",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            json=body,
        )

        return req.json()
