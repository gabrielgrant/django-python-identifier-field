from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _

from python_identifier_field import forms
from python_identifier_field.validators import validate_py_identifier

class PythonIdentifierField(CharField):
    default_validators = [validate_py_identifier]
    description = _("String (up to %(max_length)s)")
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 50)
        # Set db_index=True unless it's been set manually.
        if 'db_index' not in kwargs:
            kwargs['db_index'] = True
        super(PythonIdentifierField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.PythonIdentifierField}
        defaults.update(kwargs)
        return super(PythonIdentifierField, self).formfield(**defaults)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^python_identifier_field\.db\.models\.fields\.PythonIdentifierField"])
except ImportError:
    pass
