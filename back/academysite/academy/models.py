from django.db import models
from .file_models import Track, Problem
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from jinja2 import Template


class Validators:
    @classmethod
    def validate_track_id(cls, track_id):
        try:
            _ = Track(track_id)
        except AssertionError:
            raise ValidationError("No track corresponding to track_id")

    @classmethod
    def validate_problem(cls, track_id, problem_id):
        problem = Problem(track_id, problem_id)
        if not problem.is_valid():
            raise ValidationError(
                f"No problem {problem_id} in track {track_id}"
            )


class TrackInstance(models.Model):
    track_id = models.CharField(
        max_length=200, validators=[Validators.validate_track_id]
    )
    name = models.CharField(max_length=200, unique=True)
    public = models.BooleanField(default=True, editable=True)
    archived = models.BooleanField(default=False, editable=True)

    def __str__(self):
        return self.name

    @property
    def track(self):
        return Track(self.track_id)


class Submission(models.Model):
    track = models.ForeignKey(to=TrackInstance, on_delete=models.CASCADE)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    code = models.TextField(max_length=3000)
    problem_id = models.CharField(max_length=100)
    submission_date = models.DateTimeField(null=True, blank=True)
    correction_date = models.DateTimeField(null=True, blank=True)
    submission_count = models.IntegerField(default=1, editable=True)
    passed = models.BooleanField(default=False, editable=True)
    correction_data = models.JSONField(blank=True, null=True)

    def clean(self, *args, **kwargs):
        Validators.validate_problem(self.track.track_id, self.problem_id)

    class Meta:
        unique_together = [
            ("track", "author", "problem_id"),
        ]

    @property
    def problem(self):
        return Problem(self.track.track_id, self.problem_id)

    def get_templated_code(self):
        return Template(self.problem.template).render(student_code=self.code)
