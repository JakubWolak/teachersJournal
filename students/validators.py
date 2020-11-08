from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def greater_than_zero(value):
    if value < 0:
        raise ValidationError(
            _('%(value), is less than 0'),
            params={'value': value}
        )


def is_grade(value):
    if value < 1 or value > 6:
        raise ValidationError(
            _('%(value), given number can not be a grade'),
            params={'value': value}
        )
