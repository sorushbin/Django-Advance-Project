from django.http import HttpResponse
import time
from .tasks import sendEmail


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h2>Done sending email</h2>")
