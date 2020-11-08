from django.db import models


class Person(models.Model):
    class Meta:
        abstract: True

    pk_person = models.UUIDField(primary_key=True)

    first_name = models.CharField(max_length=50, verbose_name="First Name", null=False, blank=False)
    last_name = models.CharField(max_length=50, verbose_name="Last Name", null=False, blank=False)

    def __str__(self) -> str:
        return "{first} {last}".format(first=self.first_name, last=self.last_name)


class Timestamps(models.Model):
    class Meta:
        abstract: True

    pk_timestamps = models.UUIDField(primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
