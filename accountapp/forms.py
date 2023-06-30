from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class CustomUserCreationForm(UserCreationForm):
    # Define custom error messages
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
        'password_length': "Password must be at least 8 characters long.",
        'username_invalid': (
            "Invalid username. Only letters, digits,"
            " and underscores are allowed."
        ),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the username field
        self.fields['username'].required = True
        self.fields['username'].widget.attrs['maxlength'] = 30
        self.fields['username'].widget.attrs['pattern'] = r'^[a-zA-Z0-9_]+$'
        self.fields['username'].help_text = (
            "Required. 30 characters or fewer."
            "Letters, digits, and underscores only."
            ),

        # Customize the password fields
        self.fields['password1'].required = True
        self.fields['password1'].widget.attrs['minlength'] = 8
        self.fields['password1'].help_text = (
            "Required. At least 8 characters."
            "Letters, digits, and symbols allowed."
            ),

        self.fields['password2'].required = True

    def clean_password1(self):
        # Validate password length
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError(self.error_messages['password_length'])
        validate_password(password1, self.instance)
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            # Raise validation error if passwords don't match
            self.add_error(
                'password2', self.error_messages['password_mismatch']
                ),

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username.isalnum():
            # Raise validation error if username contains invalid characters
            raise ValidationError(self.error_messages['username_invalid'])
        return username


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['password'].required = True


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
