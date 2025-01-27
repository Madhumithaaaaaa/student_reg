from django import forms
from application.models import Datas
class StudentsForm(forms.ModelForm):
    class Meta:
        model=Datas
        fields="__all__"  
   