class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Le montant du dépôt doit être supérieur à zéro.")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("La valeur à retirer ne peut être négative.")

        if amount > self.balance:
            raise ValueError("Fonds insuffisants pour effectuer cette opération.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
