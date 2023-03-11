from Shop import Shop
from ShoppingCart import ShoppingCart

class Order:
    def __init__(self, date, shopping_cart, delivery_address, payment_method):
        self.date = date
        self.status = "Pending"
        self.shopping_cart = shopping_cart
        self.delivery_address = delivery_address
        self.payment_method = payment_method

    def validate_payment(self):
        # implementation of payment validation logic
        payment_validated = True  # placeholder value
        if payment_validated:
            self.status = "Payment Validated"
            print("Payment validated successfully")
            return True
        else:
            print("Payment validation failed")
            return False

    def cancel(self):
        if self.status == "Pending":
            self.status = "Cancelled"
            print("Order cancelled successfully")
            return True
        else:
            print("Order cannot be cancelled")
            return False

    def dispatch(self):
        if self.status == "Payment Validated":
            self.status = "Dispatched"
            print("Order dispatched successfully")
            return True
        else:
            print("Order cannot be dispatched")
            return False

    def confirm_delivery(self):
        if self.status == "Dispatched":
            self.status = "Delivered"
            print("Delivery confirmed successfully")
            return True
        else:
            print("Delivery confirmation failed")
            return False

    def refund(self):
        if self.status == "Delivered":
            # implementation of refund logic
            self.status = "Refunded"
            print("Order refunded successfully")
            return True
        else:
            print("Order cannot be refunded")
            return False

    def archive(self):
        if self.status == "Refunded":
            # implementation of archiving logic
            self.status = "Archived"
            print("Order archived successfully")
            return True
        else:
            print("Order cannot be archived")
            return False
