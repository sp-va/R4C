from django.db.models import signals
from django.dispatch import receiver

from orders.models import Order
from robots.models import Robot
from orders.utils import send_email_to_customer

@receiver(signals.post_save, sender=Robot)
def required_robot_notification(sender, instance, created, **kwargs):
    try:
        order = Order.objects.get(robot_serial=instance.serial, is_active=True)
        customer_email = order.customer.email
        x = instance.model
        y = instance.version
        if order:
            send_email_to_customer(customer_email, x, y)
            order.is_active = False
            order.save()
    except Order.DoesNotExist:
        print('Нет заказа, удовлетворяющего условию')

