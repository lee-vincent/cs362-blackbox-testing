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
# 5400654264330621
# 5126396502239288
# 2720926415343830
# 2221858293648259

# Visa
# 4532782263081517

# AMEX
# 341786522775107
# 372492094099164


class TestCreditCardValidator(unittest.TestCase):

    def test_edges(self):
        # test valid card numbers from the edge domain
        for i in (
            5574726700232866,
            5126396502239288,
            2720926415343830,
            2221858293648259,
            4532782263081517,
            341786522775107,
            372492094099164
        ):
            with self.subTest(i=i):
                self.assertTrue(credit_card_validator(i))

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

    def test_invalid_prefixes(self):
        # test invalid prefixes
        for i in (0, 1, 6, 7, 8, 9):
            with self.subTest(i=i):
                self.assertFalse(credit_card_validator(i))

    def test_visa_mastercard_length17(self):
        for i in (
            55747267002328660,
            51263965022392880,
            27209264153438300,
            22218582936482590,
            45327822630815170
        ):
            with self.subTest(i=i):
                self.assertFalse(credit_card_validator(i))

    def test_visa_mastercard_length15(self):
        for i in (
            557472670023286,
            512639650223928,
            272092641534383,
            222185829364825,
            453278226308151
        ):
            with self.subTest(i=i):
                self.assertFalse(credit_card_validator(i))

    def test_amex_length16(self):
        for i in (
            3417865227751070,
            3724920940991640
        ):
            with self.subTest(i=i):
                self.assertFalse(credit_card_validator(i))

    def test_amex_length14(self):
        for i in (
            34178652277510,
            37249209409916
        ):
            with self.subTest(i=i):
                self.assertFalse(credit_card_validator(i))

    def test_noinput(self):
        with self.assertRaises(TypeError):
            credit_card_validator()

    def test_invalid_prefix_length15(self):
        # invalid prefix for length 15
        for i in (
            35178652277510,
            36249209409916
        ):
            with self.subTest(i=i):
                self.assertFalse(credit_card_validator(i))

    # def test_prefix_length16(self):
    #     self.assertFalse(credit_card_validator(7000000000000000))

    # def test_prefix_length17(self):
    #     self.assertFalse(credit_card_validator(70000000000000000))


if __name__ == '__main__':
    unittest.main()
