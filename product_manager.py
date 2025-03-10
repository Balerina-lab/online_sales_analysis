from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Dodaje novi proizvod u listu."""
        self.products.append(product)

    def display_products(self):
        """Prikazuje sve proizvode u sistemu."""
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        """Izračunava ukupnu vrednost svih proizvoda."""
        return sum(product.price * product.quantity for product in self.products)
