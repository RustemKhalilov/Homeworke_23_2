from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from catalog.forms import StyleMixin
from users.models import User
from django import forms


class UserRegisterForm(StyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserProfileForm(StyleMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'phone', 'country',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class PasswordRecoveryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ('email',)
