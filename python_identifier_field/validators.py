import re

from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

py_identifier_re = re.compile(r'^[a-zA-Z_][\w]+$')
validate_py_identifier = RegexValidator(
    py_identifier_re,
    _(u"Enter a valid Python identifier consisting of letters, numbers, "
    u"or underscores, but not begining with a number."),
    'invalid'
)

