from django import forms

class uploadFileFrom(forms.Form):
    file = forms.FileField()
