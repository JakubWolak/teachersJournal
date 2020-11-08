from django.db import models

from common.models import Person, Timestamps


class Lecturer(Person, Timestamps):
    """lecturer"""
    password = models.CharField(max_length=100, verbose_name="Password", null=False, blank=False)
    email = models.CharField(max_length=100, verbose_name="Email", null=False, blank=False)


class Subject(Timestamps):
    """subject"""
    subject_lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=75, verbose_name="Name", null=False, blank=False)

    def __str__(self) -> str:
        return "{name}".format(name=self.name)
