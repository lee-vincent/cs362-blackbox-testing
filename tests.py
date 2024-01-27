import unittest
from credit_card_validator import credit_card_validator

# Visa
#   Prefix(es): 4
#   Length: 16
#   valid Luhn algorithm check bit
# MasterCard
#   Prefix(es): 51 through 55 and 2221 through 2720
#   Length: 16
#   valid Luhn algorithm check bit
# American Express
#   Prefix(es): 34 and 37
#   Length: 15
#   valid Luhn algorithm check bit


class TestCreditCardValidator(unittest.TestCase):

    def test_noinput(self):
        self.assertFalse(credit_card_validator())

    def test_prefix(self):
        self.assertFalse(credit_card_validator(7))

    def test_prefix_length15(self):
        self.assertFalse(credit_card_validator(700000000000000))

    def test_prefix_length16(self):
        self.assertFalse(credit_card_validator(7000000000000000))

    def test_prefix_length17(self):
        self.assertFalse(credit_card_validator(70000000000000000))


if __name__ == '__main__':
    unittest.main()
