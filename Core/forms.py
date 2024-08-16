from Core.models import *
from django import forms
class addtsudentForm(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"
