from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

def send_email(subject, message, from_mail, to_list, fail_silently=False):
    send_mail(
        subject,
        message,
        from_mail,
        to_list,
        fail_silently
    )


def send_otp_mail(mail_id, otp, user):
    subject = 'Your OTP for Registration - ULFS'
    message = render_to_string('accounts/otp_email_template.html', {'user': user, 'otp_code': otp})
    from_email = 'UNT Lost and Found - ULFS'
    recipient_list = [mail_id]

    email_message = EmailMessage(subject, message, from_email, recipient_list)
    email_message.content_subtype = 'html'
    email_message.send()