from django import forms
from .models import Archivo
from .validators import validate_file_extension

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ('titulo', 'file', )
        extra_kwargs = {"titulo": {"required": True}, "file": {"required": True}}