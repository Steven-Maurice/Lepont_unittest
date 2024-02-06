import pytest
from bank.bank_account import BankAccount  # Assurez-vous que la classe BankAccount est dans un fichier nommé bank_account.py

def test_initial_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100, "Le solde initial devrait être 100"

def test_deposit_positive_amount():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100, "Déposer 100 devrait augmenter le solde à 100"

def test_deposit_negative_amount():
    account = BankAccount()
    with pytest.raises(ValueError):
        account.deposit(-50)

def test_withdraw_less_than_balance():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50, "Retirer 50 devrait réduire le solde à 50"

def test_withdraw_more_than_balance():
    account = BankAccount(50)
    with pytest.raises(ValueError):
        account.withdraw(100)

def test_withdraw_negative_amount():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(-50)

def test_get_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100, "Le solde devrait être 100 après l'initialisation"
