from django import forms
from core.models import User










class EditProfileForm(forms.Form):
    name = forms.CharField(
        label= 'Name',
        max_length=100,
        widget=forms.TextInput(attrs={'required': True})
    )

   
    