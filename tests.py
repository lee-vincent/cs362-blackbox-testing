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

def is_valid_luhn(digits):
    check_digit = 0

    for i in range(len(digits) - 2, -1, -1):
        if i % 2 == 0:
            doubled_digit = digits[i] * 2
            check_digit += doubled_digit - 9 if doubled_digit > 9 else doubled_digit
        else:
            check_digit += digits[i]

    return (10 - (check_digit % 10)) % 10 == digits[-1]

# Example usage:
digits = [4, 5, 1, 2, 3, 6, 7, 8, 9, 0, 1]
result = is_valid_luhn(digits)
print(result)  # True or False depending on the input digits


class TestCreditCardValidator(unittest.TestCase):

    def test_noinput(self):
        self.assertFalse(credit_card_validator(0))

    def test_invalidprefix(self):
        self.assertFalse(credit_card_validator(7))

    def test_mastercardprefix51_56(self):
        # test correct prefix and length but wrong check bit
        for i in range(51, 55):
            with self.subTest(i=i):
                cc_num = str(i)+"00000000000000"
                self.assertFalse(credit_card_validator(cc_num))

    def test_mastercardprefix2221_2720(self):
        # test correct prefix and length but wrong check bit
        for i in range(2221, 2720):
            with self.subTest(i=i):
                cc_num = str(i)+"000000000000"
                self.assertFalse(credit_card_validator(cc_num))

    def test_prefix_length15(self):
        # invalid prefix, correct check bit
        self.assertFalse(credit_card_validator(700000000000005))

    def test_prefix_length16(self):
        self.assertFalse(credit_card_validator(7000000000000000))

    def test_prefix_length17(self):
        self.assertFalse(credit_card_validator(70000000000000000))


if __name__ == '__main__':
    unittest.main()
