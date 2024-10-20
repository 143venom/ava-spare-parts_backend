# home/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import FeedBackForm

@receiver(post_save, sender=FeedBackForm)
def send_feedback_notifications(sender, instance, created, **kwargs):
    if created:
        send_notification_email(instance)
        send_reply_email(instance)

def send_notification_email(feedback):
    subject = 'New Feedback Form Submission'
    message = (
        f"Name: {feedback.name}\n"
        f"Email: {feedback.email}\n"
        f"Phone: {feedback.phone}\n"
        f"Subject: {feedback.subject}\n"
        f"Message: {feedback.message}\n"
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        ['iamamirkusi@gmail.com'],  # Replace with your admin email
        fail_silently=False,
    )

def send_reply_email(feedback):
    subject = 'Thank You for Your Feedback'
    message = (
        f"Hi {feedback.name},\n\n"
        f"Thank you for your feedback! We have received your message and will get back to you soon.\n\n"
        f"Here’s a summary of your submission:\n"
        f"Subject: {feedback.subject}\n"
        f"Message: {feedback.message}\n\n"
        f"Best regards,\n"
        f"Your Company Name"
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [feedback.email],
        fail_silently=False,
    )
