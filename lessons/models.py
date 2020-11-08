from django.db import models

from common.models import Timestamps
from lecturers.models import Subject, Lecturer
from students.models import Student


class Lesson(Timestamps):
    lesson_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, blank=False)
    topic = models.CharField(max_length=75, verbose_name="Lesson's topic", null=False, blank=False)

    lesson_date = models.DateTimeField(verbose_name="Lesson started at", auto_now_add=True, null=False, blank=False)

    def __str__(self) -> str:
        return "{topic}".format(topic=self.topic)


class Presence(Timestamps):
    presence_student = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=False, blank=False)
    presence_lesson = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)


class Group(Timestamps):
    group_lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=False, blank=False)
    group_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, blank=False)

    name = models.CharField(max_length=100, verbose_name="Group's name", null=False, blank=False)

    def __str__(self) -> str:
        return "{name}".format(name=self.name)


class StudentGroup(Timestamps):
    """students' group"""
    studentgroup_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    studentgroup_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)