from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.signing import BadSignature

from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import AdvUser
from .forms import ChangeUserInfoForm, RegisterUserForm 
from .utilities import signer

# Login form
class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'

# Logout form
class AccountsLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'

# Change user data from
class ChangeUserInfoViews(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'accounts/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('accounts:profile')
    success_message = 'Personal users data is change'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)    

# Profile form
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# Change user password from
class AccountsPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:profile')
    success_message = 'Password is changed'

# Register 
class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'accounts/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('accounts:register_done') 

class RegisterDoneView(TemplateView):
    template_name = 'accounts/register_done.html'

# User activation
def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'accounts/bad_signature.html')
    
    user = get_object_or_404(AdvUser, username=username)
    
    if user.is_activated:
        template = 'accaunts/user_is_activated.html'
    else:
        template = 'accaunts/activation_done.html' 
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)

    