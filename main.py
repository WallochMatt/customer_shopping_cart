from customer_class import Customer
from product_class import Product

new_customer = Customer("Matt")
# print(new_customer.cust_name) #good

##############################################################

product_1 = Product("Death Sticks", 5.04, "Spice")
product_2 = Product("Tent", 249.89, "Outdoors")
product_3 = Product("Earbuds", 35.89, "Electronics")

new_customer.add_new_product(product_1)
new_customer.add_new_product(product_2)
new_customer.add_new_product(product_3)

new_customer.view_items() #works

##############################################################

value = new_customer.custs_cart.total(new_customer.custs_cart.products_held)
