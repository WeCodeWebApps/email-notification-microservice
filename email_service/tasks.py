from django.core.mail import send_mail as django_send_mail
from celery import shared_task

from .utils import format_template
from .models import EmailTemplate

ASYK = True


def asynk_wrapper(fun):
    def _inner(*args, **kwargs):
        if ASYK:
            return fun.delay(*args, **kwargs)
        return fun(*args, **kwargs)

    return _inner


@shared_task
def _schedule_send_mail(email: str, subject: str, template: str, **kwargs) -> None:
    template = EmailTemplate.objects.get(template_name=template)

    django_send_mail(
        subject,
        "",
        from_email=None,
        recipient_list=[email],
        fail_silently=False,
        html_message=format_template(template, **kwargs),
    )


@asynk_wrapper
def send_mail(email: str, subject: str, template: str, **kwargs):
    return _schedule_send_mail(email, subject, template, **kwargs)
