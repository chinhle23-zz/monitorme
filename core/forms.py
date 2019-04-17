from django import forms
from registration.forms import RegistrationForm
from django.contrib.auth import password_validation

class CustomRegistrationForm(RegistrationForm):

    email = forms.EmailField(
        label="E-mail",
        widget=forms.TextInput(attrs={'class': 'loginsection'})
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'loginsection'}),
        # help_text=password_validation.password_validators_help_text_html(),
        help_text=None,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'loginsection'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = None

    class Meta(RegistrationForm.Meta):
        widgets = {
            'username': forms.TextInput(attrs={'class': 'loginsection'}),
        }
