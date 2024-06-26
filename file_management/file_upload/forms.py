from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UploadedFile

class LoginForm(AuthenticationForm):
    pass

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
