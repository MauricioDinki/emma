#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.template import loader
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.views.generic import View, TemplateView, FormView
from django.conf import settings

from emma.apps.users.forms import LoginForm, SignupForm
from emma.core.mixins import NextUrlMixin, AuthRedirectMixin
from .forms import PasswordResetRequestForm, PasswordResetForm


class PasswordReset(View):
    template_name = 'xauth/password_reset.html'
    token_generator = default_token_generator
    set_password_form = PasswordResetForm
    post_reset_redirect = reverse_lazy('xauth:reset_password_done')
    extra_context = None
    User = None

    def get(self, request, uidb64, token):
        UserModel = get_user_model()
        assert uidb64 is not None and token is not None
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            self.User = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            self.User = None

        if self.User is not None and \
                self.token_generator.check_token(self.User, token):
            validlink = True
            title = 'Enter new password'
            form = self.set_password_form(self.User)
        else:
            validlink = False
            form = None
            title = 'Password reset unsuccessful'

        context = {
            'form': form,
            'title': title,
            'validlink': validlink,
        }

        return TemplateResponse(request, self.template_name, context)

    def post(self, request, uidb64, token):
        UserModel = get_user_model()
        assert uidb64 is not None and token is not None
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            self.User = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            self.User = None
        form = self.set_password_form(self.User, request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.post_reset_redirect)


class PasswordResetDone(TemplateView):
    template_name = 'xauth/password_reset_done.html'


class PasswordResetRequest(View):
    template_name = 'xauth/password_reset_request.html'
    from_email = "Notificaciones - Emma <postmaster@%s>" % (
        settings.MAILGUN_SERVER_NAME
    )
    email_template_name = 'email/password_reset_request.html'
    email_subject = 'email/subjects/password_reset_request.txt',
    form = PasswordResetRequestForm
    token_generator = default_token_generator
    success_url = reverse_lazy('xauth:reset_password_request_done')
    html_email_template_name = None
    extra_email_context = None

    def get(self, request):
        form = self.form()
        ctx = {
            'form': form,
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': self.token_generator,
                'from_email': self.from_email,
                'email_template_name': self.email_template_name,
                'subject_template_name': self.email_subject,
                'request': request,
                'html_email_template_name': self.html_email_template_name,
                'extra_email_context': self.extra_email_context,
            }
            form.save(**opts)
            return redirect(self.success_url)


class PasswordResetRequestDone(TemplateView):
    template_name = 'xauth/password_reset_request_done.html'


class LoginView(NextUrlMixin, AuthRedirectMixin, FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users:select_card')

    def form_valid(self, form):
        login(self.request, form.user_cache)
        if not form.user_cache.client.active_client:
            return redirect(reverse_lazy('landing:date'))

        elif not form.user_cache.client.change_password:
            return redirect(reverse_lazy('users:change_password'))
        else:
            return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())


@login_required(login_url=reverse_lazy('xauth:login'))
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('landing:home'))


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('landing:home')

    def form_valid(self, form):
        form.save()
        login(self.request, form.user_cache)
        return super(SignupView, self).form_valid(form)

    def get_success_url(self):
        if 'submit_btn_1' in self.request.POST:
            url = reverse_lazy('landing:home')
        elif 'submit_btn_2' in self.request.POST:
            url = reverse_lazy('landing:date')
        else:
            url = self.success_url

        subject = loader.render_to_string(
            'email/subjects/notification_welcome.txt'
        )

        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())

        body = loader.render_to_string(
            'email/notification_welcome.html'
        )

        from_email = "Emma - Notificaciones <postmaster@%s>" % (
            settings.MAILGUN_SERVER_NAME
        )

        to_email = [self.request.user.email]

        msg = EmailMultiAlternatives(
            subject=subject,
            from_email=from_email,
            body=body,
            to=to_email
        )

        msg.send()

        return url
