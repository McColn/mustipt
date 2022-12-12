from django.forms import ModelForm
from field.models import *

class FieldApplicationForm(ModelForm):
	class Meta:
		model=FieldApplication
		fields='__all__'