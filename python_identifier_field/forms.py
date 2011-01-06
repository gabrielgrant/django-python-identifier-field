from django.forms.fields import CharField
from django.utils.translation import ugettext_lazy as _
from python_identifier_field import validators

class PythonIdentifierField(CharField):
    default_error_messages = {
        'invalid': _(u"Enter a valid Python identifier consisting of"
                     u" letters, numbers, or underscores, but not"
                     u" beginning with a number."),
    }
    default_validators = [validators.validate_py_identifier]
