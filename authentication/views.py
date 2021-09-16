from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from authentication.forms import CustomUserCreationForm
from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User


class LandingPageView(LoginRequiredMixin, generic.ListView):
    template_name = "landing.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
          queryset = User.objects.all()
        else:
          queryset = User.objects.filter(email=user.email)
        return queryset
    
    
class SignupView(generic.FormView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm


    def get_success_url(self):
        return reverse("landing-page")

    def form_valid(self, form):
        form.save()
        email = self.request.POST['email']
        password = self.request.POST['password1']
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "user_delete.html"

    def get_success_url(self):
        return reverse("landing-page")

    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
          queryset = User.objects.all()
        else:
          queryset = User.objects.filter(email=user.email)
        return queryset