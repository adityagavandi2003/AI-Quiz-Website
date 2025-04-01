from django import forms
from aiquiz.models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['marks','total_marks','quiz']

