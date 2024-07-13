import random
import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView
from users.forms import UserRegisterForm, PasswordRecoveryForm, UserProfileForm
from config.settings import EMAIL_HOST_USER
from django.http import HttpResponseRedirect
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        token = "".join([str(random.randint(0, 9)) for i in range(10)])
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейдите по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class PasswordRecoveryView(TemplateView):
    model = User
    template_name = 'users/password_recovery_form.html'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('users:recovery_message')

    code = secrets.token_hex(8)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        code = PasswordRecoveryView.code
        user.set_password(PasswordRecoveryView.code)
        user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/login/'

        send_mail(
            'Восстановление пароля',
            f'Ваш новый пароль {code}, перейдите по ссылке {url}',
            EMAIL_HOST_USER,
            [user.email],
        )
        return HttpResponseRedirect('/users/password_recovery/message/')


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
