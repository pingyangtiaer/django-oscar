from decimal import Decimal as D

from oscar.apps.shipping.base import ShippingMethod
from oscar.apps.shipping.models import OrderAndItemCharges, WeightBand
from oscar.apps.shipping import Scales


class Free(ShippingMethod):
    """
    Simple method for free shipping
    """
    code = 'free-shipping'
    name = 'Free shipping'
    
    def basket_charge_incl_tax(self):
        return D('0.00')
    
    def basket_charge_excl_tax(self):
        return D('0.00')
    

class FixedPrice(ShippingMethod):
    code = 'fixed-price-shipping'
    name = 'Fixed price shipping'
    
    def __init__(self, charge_incl_tax, charge_excl_tax=None):
        self.charge_incl_tax = charge_incl_tax
        if not charge_excl_tax:
            charge_excl_tax = charge_incl_tax
        self.charge_excl_tax = charge_excl_tax
    
    def basket_charge_incl_tax(self):
        return self.charge_incl_tax
    
    def basket_charge_excl_tax(self):
        return self.charge_excl_tax

