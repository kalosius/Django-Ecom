from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
import time
from . models import Order


@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    # Add a 10sec pause for paypal to send IPN data
    time.sleep(10)
    # Grab the info that paypal sends
    paypal_obj = sender
    # Grab the invoice
    my_Invoice = str(paypal_obj.invoice)

    # Match the paypal invoice to the Order invoice
    # Lookup the order
    my_order = Order.objects.get(invoice=my_Invoice)

    # Record the that the order was paid 
    my_order.paid = True
    # Save the order
    my_order.save()
    





    # print(paypal_obj) 