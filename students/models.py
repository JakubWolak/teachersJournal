from django.db import models

from common.models import Person, Timestamps
from lecturers.models import Subject

from students.validators import greater_than_zero, is_grade


class Student(Person, Timestamps):
    """student"""
    pass


class Mark(Timestamps):
    """student's mark"""
    mark_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, blank=False)
    mark_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)

    weight = models.IntegerField(validators=[greater_than_zero], verbose_name="Mark's weight", null=False, blank=False)
    grade = models.FloatField(validators=[is_grade], verbose_name="Student's grade", null=False, blank=False)

    def __str__(self) -> str:
        return "{grade} => weight: {weight}".format(grade=self.grade, weight=self.weight)



