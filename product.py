class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Prikazuje informacije o proizvodu."""
        return f"Proizvod: {self.name}, Cena: {self.price}, Količina: {self.quantity}"

    def update_quantity(self, amount):
        """Ažurira količinu proizvoda."""
        if self.quantity + amount >= 0:
            self.quantity += amount
        else:
            print("Nedovoljno proizvoda na stanju")
