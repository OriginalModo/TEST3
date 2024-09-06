from celery import shared_task
from .models import Order


@shared_task
def prepare_order(order_id):
    order = Order.objects.get(id=order_id)
    order.status = 'Ready'
    order.save()