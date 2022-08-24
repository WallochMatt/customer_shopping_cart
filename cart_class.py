from product_class import Product

class ShoppingCart:
    def __init__(self):
        self.products_held = []

    def total(self, products_held):
        grand_total = 0
        for product_index in products_held:
            grand_total = grand_total + product_index.price

    def add_product(self, product):
        self.products_held.append(product.name)#?

    def dump_cart(self):
        self.products_held = [] #this should overwrite it , if not I can make another variable to pass it on