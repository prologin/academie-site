import json
import time
import glob
import traceback
import enum
import os
import requests
import ast

from pprint import pprint

class Encoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

class Difficulty(enum.Enum):
    TRIVIAL = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3
    VERY_HARD = 4

class Problem:
    def __init__(
        self,
        title,
        allowed_languages,
        tests,
        skeletons,
        correction_templates,
        author,
        description,
        subject,
        difficulty,
    ):

        self.title = title
        self.author = author
        self.description = description
        self.subject = subject
        self.difficulty = difficulty
        self.allowed_languages = allowed_languages
        self.skeletons = skeletons
        self.correction_templates = correction_templates
        self.tests = tests

languages_extension = {
        "ada": ".ada",
        "c": ".c",
        "c#": ".cs",
        "c++": ".cc",
        "d": ".d",
        "go": ".go",
        "haskell": ".hs",
        "java": ".java",
        "javascript": ".js",
        "lua": ".lua",
        "ocaml": ".ml",
        "pascal": ".pp",
        "perl": ".pl",
        "php": ".php",
        "prolog": ".pro",
        "python": ".py",
        "ruby": ".rb",
        "rust": ".rs",
        "scheme": ".scm",
}

allowed_languages = [
        "ada",
        "c",
        "c#",
        "c++",
        "d",
        "go",
        "haskell",
        "java",
        "javascript",
        "lua",
        "ocaml",
        "pascal",
        "perl",
        "php",
        "prolog",
        "python",
        "ruby",
        "rust",
        "scheme",
]

class ActivityExecption(Exception):
    pass

def problem_description_validator(desc):
    if not isinstance(desc, dict):
        raise ActivityExecption
    try:
        author = desc["author"]
        title = desc["title"]
        description = desc["description"]
        subject = desc["subject"]
        difficulty = Difficulty(desc["difficulty"])
    except Exception:
        raise ActivityExecption
    if not isinstance(author, str) or \
        not isinstance(description, str) or \
        not isinstance(subject, str) or \
        not isinstance(title, str):
            print("FAIL")
            raise ActivityExecption


def load_problem(allowed_languages, slug, name):
    skeletons = dict()
    correction_templates = dict()
    tests = []

    author = ""
    description = ""
    subject = ""
    title= ""
    diff = None


    for lang in allowed_languages:
        root = slug + "/" + lang + "/"
        with open(root + "tests_" + name + ".json") as json_file:
            data = json.load(json_file)
            tests = data
        try:
            with open(root + "skeleton_" + name + languages_extension[lang]) as skeleton:
                skeletons[lang] = skeleton.read()
        except FileNotFoundError:
            pass

        try:
            with open(root + "correction_template_" + name + languages_extension[lang]) as correction:
                correction_templates[lang] = correction.read()
        except FileNotFoundError:
            pass
        try:
            with open(slug + "/information.json") as info_json:
                data = json.load(info_json)
                problem_description_validator(data)
                author = data["author"]
                description = data["description"]
                subject = data["subject"]
                title = data["title"]
                diff = Difficulty(data["difficulty"])
        except Exception:
            pass
    
    problem = Problem(
        name,
        allowed_languages,
        tests,
        skeletons,
        correction_templates,
        author,
        description,
        subject,
        diff.value
    )
    return problem


def update_problem(slug, allowed_languages):

    # 1 problem =   1 optional file skeleton_*.*
    #             + 1 optional file correction_template_*.*
    #             + 1 file tests_*.json that contains the tests

    try:
        name = slug.removeprefix("problem_")
        return load_problem(allowed_languages, slug, name)
    except Exception:
        raise ActivityExecption


def send_request(slug, access):
    dump = os.listdir(slug)
    languages = []
    for lang in dump:
        if os.path.isdir(slug + "/" + lang):
            if not lang in allowed_languages:
                raise ActivityExecption
            languages.append(lang)
    
    if len(languages) == 0:
        raise ActivityExecption

    problem = update_problem(slug, languages)

    headers = dict()
    headers = {'Content-type': 'application/json',
               'Authorization': f"Bearer {access}"}

    r = requests.post(
        "http://127.0.0.1:8080/api/problems/?title=" + problem.title,
        data=json.dumps(problem.__dict__),
        headers=headers,
    )



if __name__ == "__main__":

    email = "mr.prologin@prologin.org"
    password = "aurelienchetor"

    login = dict()
    login['email'] = email
    login['password'] = password

    r = requests.post(
        "http://127.0.0.1:8080/auth/login/",
        json=login
    )

    r = r.content.decode("UTF-8")
    r = json.loads(r)


    dirs = os.listdir()
    for directory in dirs:
        if os.path.isdir(directory) and directory.startswith("problem_"):
            try:
                send_request(directory, r['access'])
            except Exception:
                traceback.print_exc()
                print("Cannot update " + directory)