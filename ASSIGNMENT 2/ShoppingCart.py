class ShoppingCart:
    def __init__(self, items, delivery_fees=0, discount=0):
        self.items = items
        self.delivery_fees = delivery_fees
        self.discount = discount
        self.total_amount = 0

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} not found in shopping cart')

    def select_delivery_option(self, delivery_fees):
        self.delivery_fees = delivery_fees

    def apply_discount(self, discount):
        self.discount = discount

    def calculate_total(self):
        subtotal = sum(item['price'] for item in self.items)
        total = subtotal + self.delivery_fees - self.discount
        self.total_amount = total
        return total

    def checkout(self):
        total = self.calculate_total()
        print('Checkout: ')
        for item in self.items:
            print(f"{item['name']} - {item['price']}")
        print(f"Subtotal: {sum(item['price'] for item in self.items)}")
        print(f'Delivery fees: {self.delivery_fees}')
        print(f'Discount: {self.discount}')
        print(f'Total: {total}')
