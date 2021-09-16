from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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
