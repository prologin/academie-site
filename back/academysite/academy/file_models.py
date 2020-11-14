from django.conf  import settings
import os
import json

class Problem:

    def _check_file(self, name):
        return os.path.isfile(os.path.join(self.path, name))
    
    def _check_dir(self, name):
        return os.path.isdir(os.path.join(self.path, name))
    
    def _fetch_properties(self):
        props = {}
        with open(os.path.join(self.path, 'problem.json')) as f:
            props = json.loads(f.read())
        return props
    
    def _fetch_tests(self):
        tests_path = os.path.join(self.path, 'tests')
        tests = []
        for t_in in filter(lambda x: x.endswith('.in'), os.listdir(tests_path)):
            t_out = os.path.join(tests_path, os.path.splitext(t_in)[0] + '.out')
            assert os.path.isfile(t_out)
            t_in = os.path.join(tests_path, t_in)
            stdin, stdout = None, None
            with open(t_in) as f:
                stdin = f.read()
            with open(t_out) as f:
                stdout = f.read()
            tests.append((stdin, stdout))
        return tests
    
    def _fetch_scaffold(self):
        scaffold_path = os.path.join(self.path, 'scaffold.py')

        # no scaffold provided <=> empty scaffold
        if not os.path.isfile(scaffold_path):
            return ''
        
        with open(scaffold_path) as f:
            return f.read()
    
    def _fetch_template(self):
        template_path = os.path.join(self.path, 'template.py')

        with open(template_path) as f:
            return f.read()
    
    def _fetch_subject(self):
        subject_path = os.path.join(self.path, 'subject.md')

        with open(subject_path) as f:
            return f.read()

    def is_valid(self):
        return (
            self._check_dir('') and
            self._check_file('problem.json') and
            self._check_file('subject.md') and
            self._check_file('template.py') and
            self._check_dir('tests')
        )
    
    def __init__(self, path):
        self.path = path

        if self.is_valid():
            self.tests = self._fetch_tests()
            self.properties = self._fetch_properties()
            self.template = self._fetch_template()
            self.scaffold = self._fetch_scaffold()
            self.subject = self._fetch_subject()
    
    def __repr__(self):
        return f'<Problem \'{self.name}\'>'

    @property
    def name(self):
        return self.properties.get('name', os.path.split(self.path)[-1])
            

class Track:

    @classmethod
    def discover(cls):
        tracks = []
        for p in os.listdir(settings.ACADEMY_RESOURCES_PATH):
            track = None
            try:
                track = cls(p)
            except AssertionError:
                continue
            tracks.append(track)
        return tracks

    def _check_files(self):
        assert os.path.isfile(self._get_path('track.json'))

    def _track_exists(self):
        return os.path.isdir(self._get_path())

    def _get_path(self, ext=None):
        if ext is None:
            return os.path.abspath(os.path.join(settings.ACADEMY_RESOURCES_PATH, self.id))
        return os.path.abspath(os.path.join(settings.ACADEMY_RESOURCES_PATH, self.id, ext))

    def __init__(self, id):
        self.id = id

        assert self._track_exists()
        self._check_files()
    
    def __repr__(self):
        return f'<Track \'{self.name}\' ({self.id})>'
    
    @property
    def properties(self):
        props = {}
        with open(self._get_path('track.json')) as f:
            props = json.loads(f.read())
        return props
    
    @property
    def name(self):
        return self.properties.get('full_name', self.id)
    
    @property
    def problems(self):
        problems = []
        for p in os.listdir(self._get_path()):
            path = self._get_path(p)
            if not os.path.isdir(path):
                continue
            problem = Problem(path)
            if problem.is_valid():
                problems.append(problem)
        return problems