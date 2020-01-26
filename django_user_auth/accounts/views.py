from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Login form
class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'

# logout form
class AccountsLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'

# Profile form
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def start(request):
    
    context = {'result': ''}
    return render(request, 'accounts/start.html', context)

def login(request):
    
    context = {'result': ''}
    return render(request, 'accounts/login.html', context)

def recover(request):

    context = {'result': ''}
    return render(request, 'accounts/recover.html', context)