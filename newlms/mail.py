from django.core.mail import send_mail
from django.conf import settings


class Mail:
    email_from = settings.EMAIL_HOST

    def __init__(self, subject="LMS System", message=None, recipient_list=None):
        try:
            print("------------------------trying for mail-----------------------")
            send_mail(subject, message, self.email_from, recipient_list)
        except:
            return "Error occured"