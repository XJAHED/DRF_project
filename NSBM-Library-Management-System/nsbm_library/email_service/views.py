from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.decorators import action
import threading
from rest_framework.response import Response
from nsbm_library.settings import EMAIL_HOST_USER

from AddMember.models import *
# Create your views here.

def send_library_notification(subject, message):

        emails = list(
            AddMember.objects.exclude(email='').values_list('email', flat=True)
        )
        
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            emails,
            fail_silently=True,
        )
        
def start_library_notification(subject, message):
    thread = threading.Thread(
        target=send_library_notification,
        args=(subject, message)
    )

    # thread.daemon = True
    thread.start()