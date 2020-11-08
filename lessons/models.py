from django.db import models

from common.models import Timestamps
from lecturers.models import Subject, Lecturer
from students.models import Student


class Lesson(Timestamps):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, blank=False)
    topic = models.CharField(max_length=75, verbose_name="Lesson's topic", null=False, blank=False)

    lesson_date = models.DateTimeField(verbose_name="Lesson started at", auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.topic


class Presence(Timestamps):
    student = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=False, blank=False)
    lesson = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)


class Group(Timestamps):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=False, blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, blank=False)

    name = models.CharField(max_length=100, verbose_name="Group's name", null=False, blank=False)

    def __str__(self):
        return self.name
