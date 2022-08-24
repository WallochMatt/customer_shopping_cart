from cart_class import ShoppingCart
from product_class import Product

class Customer:
    def __init__(self, name):
        self.cust_name = name
        self.custs_cart = ShoppingCart() #match parameters to the class(init)

    def add_new_product(self, product):       
        self.custs_cart.add_product() #thoguht process being my newly assigned cart is being added to with add product method
#   def add_product(self, product):
        #self.products_held.append(product.name)

    def view_items(self):
        for item_index in self.custs_cart:
            print(item_index)