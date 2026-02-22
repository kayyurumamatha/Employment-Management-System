from django import forms
from .models import staff
class newstaffform(forms.ModelForm):
    class Meta:
        model=staff
        fields='__all__'
class searchform(forms.Form):
    dept=forms.CharField(max_length=20)
    name=forms.CharField(max_length=20)

class updateform(forms.Form):
    staffid=forms.CharField(max_length=10)
    mobno=forms.CharField(max_length=10,label='Mobile Number')
    emailid=forms.CharField(max_length=40)
    
class deleteform(forms.Form):
    staffid = forms.CharField(max_length=10)
