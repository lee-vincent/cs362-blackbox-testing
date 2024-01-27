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

# MasterCard
# 5574726700232866
# 2720926415343830
# 2221858293648259

# Visa
# 4532782263081517

# AMEX
# 341786522775107
# 372492094099164


class TestCreditCardValidator(unittest.TestCase):

    def test_mastercard_prefix51_55_checkbit(self):
        # test correct prefix and length but wrong check bit
        self.assertFalse(credit_card_validator(5574726700232860))

    def test_mastercard_prefix2221_2720_checkbit(self):
        # test correct prefix and length but wrong check bit
        self.assertFalse(credit_card_validator(2221858293648250))

    def test_visa_prefix4_checkbit(self):
        # test correct prefix and length but wrong check bit
        self.assertFalse(credit_card_validator(4532782263081510))

    def test_amex_prefix34_checkbit(self):
        # test correct prefix and length but wrong check bit
        self.assertFalse(credit_card_validator(341786522775102))

    def test_amex_prefix37_checkbit(self):
        # test correct prefix and length but wrong check bit
        self.assertFalse(credit_card_validator(372492094099162))

    def test_invalid_prefixs(self):
        # test invalid prefixes
        for i in (0, 1, 6, 7, 8, 9):
            with self.subTest(i=i):
                self.assertFalse(credit_card_validator(i))

    # def test_noinput(self):
    #     self.assertFalse(credit_card_validator(0))

    # def test_invalidprefix(self):
    #     self.assertFalse(credit_card_validator(7))

    # def test_prefix_length15(self):
    #     # invalid prefix, correct check bit
    #     self.assertFalse(credit_card_validator(700000000000005))

    # def test_prefix_length16(self):
    #     self.assertFalse(credit_card_validator(7000000000000000))

    # def test_prefix_length17(self):
    #     self.assertFalse(credit_card_validator(70000000000000000))


if __name__ == '__main__':
    unittest.main()
