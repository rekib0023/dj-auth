from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  address = forms.CharField(required=True)

  class Meta:
    model = User
    fields = ("email", "username", "password1", "password2", "address")

  def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.address = self.cleaned_data["address"]

        if commit:
            user.save()
        return user

class CustomUserUpdateForm(UserChangeForm):
  email = forms.EmailField(required=True)
  address = forms.CharField(required=True)

  class Meta:
    model = User
    fields = ("email", "username", "address")

  def save(self, commit=True):
        user = super(CustomUserUpdateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.address = self.cleaned_data["address"]

        if commit:
            user.save()
        return user


class CustomUserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': "Old Password"})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
