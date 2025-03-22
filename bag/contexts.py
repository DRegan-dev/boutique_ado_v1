from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = Decimal(0)  # Ensure total is a Decimal
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity* product.price
        product_count += quantity
        bag_items.append ({
            'item_id': item_id,
            'quantity': quantity,
            'product': product

        })

    free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)
    standard_delivery_percentage = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)

    if total < free_delivery_threshold:
        delivery = total * (standard_delivery_percentage / 100)
        free_delivery_delta = free_delivery_threshold - total
    else:
        delivery = Decimal(0)
        free_delivery_delta = Decimal(0)

    grand_total = delivery + total

    context = {
        'bag_items': bag_items, 
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
    }

    return context
