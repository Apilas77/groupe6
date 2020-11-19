from .models import Application
from django import forms

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ["nom", "active"]

