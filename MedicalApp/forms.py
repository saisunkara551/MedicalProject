from django import forms

class medNameForm(forms.Form):

    name=forms.CharField(max_length=50)
