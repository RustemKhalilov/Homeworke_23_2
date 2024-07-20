from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, PasswordRecoveryView, ProfileView

app_name = UsersConfig.name

urlpatterns = [
   path("login/", LoginView.as_view(template_name='login.html'), name='login'),
   path("logout/", LogoutView.as_view(next_page='/'), name='logout'),
   path("register/", UserCreateView.as_view(), name='register'),
   path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
   path("email-confirm/<str:token>/", email_verification, name='email-confirm'),
   path('profile/', ProfileView.as_view(), name='profile')
]
