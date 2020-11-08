from django.db import models

from common.models import Person, Timestamps
from lessons.models import Group, Subject

from students.validators import greater_than_zero, is_grade


class Student(Person, Timestamps):
    """student"""
    pass


class Mark(Timestamps):
    """student's mark"""
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, blank=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)

    weight = models.IntegerField(validators=[greater_than_zero], verbose_name="Mark's weight", null=False, blank=False)
    grade = models.FloatField(validators=[is_grade], verbose_name="Student's grade", null=False, blank=False)


class StudentGroup(Timestamps):
    """students' group"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)
