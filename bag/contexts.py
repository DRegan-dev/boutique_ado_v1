from decimal import Decimal
from django.conf import settings

def bag_contents(requestt):

    bag_items = []
    total = 0
    product_count = 0

    if total < setting.FREE_DELIVERY_THRESHOLD:
        delivery = total *Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
    context = {}

    return context