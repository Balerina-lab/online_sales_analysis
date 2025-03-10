class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        """Dodaje proizvod u korpu."""
        self.cart_items.append(product)

    def display_cart(self):
        """Prikazuje sve proizvode u korpi."""
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("\nSadržaj korpe:")
            for product in self.cart_items:
                print(product.display_info())

    def total_cart_value(self):
        """Računa ukupnu vrednost korpe."""
        return sum(product.price * product.quantity for product in self.cart_items)
