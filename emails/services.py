from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from space_rangers.models import Pilot


def send_all_healed(pilot: Pilot) -> None:
    """Send email notification that all spaceships are healed."""
    html_content = render_to_string('email.html', {'pilot': pilot})

    send_mail(
        subject='All your spaceships are ready!',
        message='',
        from_email=settings.EMAIL_FROM,
        recipient_list=[
            pilot.user.email,
        ],
        html_message=html_content,
    )
