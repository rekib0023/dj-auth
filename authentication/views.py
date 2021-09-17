from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.http import HttpResponseRedirect
from authentication.forms import CustomUserCreationForm, CustomUserPasswordChangeForm, CustomUserUpdateForm
from django.shortcuts import render, reverse
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


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "registration/user_update.html"
    model=User
    form_class = CustomUserUpdateForm


    def get_success_url(self):
        return reverse("landing-page")

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])

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


class UserPassword(LoginRequiredMixin,generic.TemplateView):

    def get(self, request, *args, **kwargs):
        form_class = CustomUserPasswordChangeForm
        form = form_class(self.request.user)
        return render(request, 'registration/password.html',{'form': form,})

    def post(self, request, *args, **kwargs):
        form_class = CustomUserPasswordChangeForm

        form = form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
        return render(request, 'registration/password.html', {'form': form})