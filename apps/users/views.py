from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import CreateView
from apps.users.forms import CustomUserCreationForm
from django.template.loader import render_to_string
from django.utils.encoding import force_str, force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_link = f"http://{current_site.domain}/users/activate/{uid}/{token}/"
        message = render_to_string('email/activation_email.html', context={
            'user': user,
            'activation_link': activation_link
        })
        print("Activation link:", activation_link)

        send_mail(
            subject="Akkountingizni faollashtiring",
            message=message,
            from_email="zarnigor1008@gmail.com",
            recipient_list=[user.email],
        )

        return redirect("users:login")


class ActivationView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Sizning akkountingiz muvaffaqiyatli aktivlashtirildi.")
            return redirect("users:login")
        else:
            messages.error(request, "Aktivatsiya havolasi xato yoki eskirgan.")
            return redirect("users:login")



