"""
Celery задачи для модуля уведомлений.
Асинхронная отправка email уведомлений.
"""
# from celery import shared_task
# from django.core.mail import send_mail


# @shared_task
# def send_notification_email(subject, message, recipient_list):
#     """Асинхронная отправка email уведомления."""
#     send_mail(
#         subject=subject,
#         message=message,
#         from_email=None,
#         recipient_list=recipient_list,
#         fail_silently=False,
#     )



