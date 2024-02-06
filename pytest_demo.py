
import pytest

def test_addition():
    result = 2 + 2
    assert result == 4, "2 + 2 devrait être égal à 4"

def test_uppercase():
    result = "HELLO"
    assert result == "HELLO", "hello en majuscules devrait être égal à HELLO"
