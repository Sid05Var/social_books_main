from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


@receiver(user_logged_in)
def send_login_notification(sender, request, user, **kwargs):
    subject = 'Login Notification'
    message = f'Hello {user.username}, you have successfully logged in.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = user.email

    send_mail(subject, message, from_email, [recipient_list])