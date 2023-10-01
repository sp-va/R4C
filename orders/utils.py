from django.core.mail import send_mail
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'R4C.settings')

my_email = settings.EMAIL_HOST_USER


def send_email_to_customer(customer_email, x, y):
    send_mail(
        subject='Ваш робот изготовлен', 
        message=f'''Добрый день!\n
        Недавно вы интересовались нашим роботом модели {x}, версии {y}.\n
        Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами''', 
        from_email=my_email, 
        recipient_list=[customer_email], 
        fail_silently=False
    )