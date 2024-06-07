#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.transactions = []
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.transactions.append(price)
            self.total += price
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
           discount_amount = self.total * (self.discount / 100)
           self.total -= discount_amount
           print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
           print("There is no discount to apply.")


    def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()
            self.total -= last_transaction
            self.items.pop()


