from django.urls import path
from .views import profile, AccountsLoginView, AccountsLogoutView, ChangeUserInfoViews, AccountsPasswordChangeView, RegisterUserView, RegisterDoneView, user_activate

app_name = 'accounts'
urlpatterns = [
    path('', profile, name='profile'),
    path('login/', AccountsLoginView.as_view(), name='login'),
    path('logout/', AccountsLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/change/', ChangeUserInfoViews.as_view(), name='profile_change'),
    path('password/change/', AccountsPasswordChangeView.as_view(), name='password_change'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('register/activate/<str:sign>', user_activate, name='register_activate'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),   
]