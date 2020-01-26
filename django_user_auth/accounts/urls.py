from django.urls import path
from .views import start, login, recover, profile, AccountsLoginView, AccountsLogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', AccountsLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', AccountsLogoutView.as_view(), name='logout'),

]