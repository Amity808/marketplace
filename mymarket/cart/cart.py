from decimal import Decimal
from django.conf import settings
from mymarket.market.models import Product

# working on session
class Cart:
    def __init__(self, request):
        """
        initiliaze the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save am empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
