from product import Product
from product_manager import ProductManager

# Kreiramo instancu ProductManager
manager = ProductManager()

# Dodajemo proizvode
p1 = Product("Laptop", 1000, 5)
p2 = Product("Telefon", 500, 10)
p3 = Product("Monitor", 300, 7)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikazujemo proizvode
print("\nLista proizvoda:")
manager.display_products()

# Prikazujemo ukupnu vrednost inventara
print(f"\nUkupna vrednost inventara: {manager.total_inventory_value()}$")
# Kreiramo korpu i dodajemo proizvode
cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p3)

# Prikazujemo sadržaj korpe
print("\nSadržaj korpe:")
cart.display_cart()

# Prikazujemo ukupnu vrednost korpe
print(f"\nUkupna vrednost korpe: {cart.total_cart_value()}$")