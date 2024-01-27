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

    def test_mastercard_valid(self):
        self.assertTrue(credit_card_validator(5574726700232866))
        self.assertTrue(credit_card_validator(5126396502239288))
        self.assertTrue(credit_card_validator(2720926415343830))
        self.assertTrue(credit_card_validator(2221858293648259))

    def test_visa_valid(self):
        self.assertTrue(credit_card_validator(4532782263081517))

    def test_amex_valid(self):
        self.assertTrue(credit_card_validator(341786522775107))
        self.assertTrue(credit_card_validator(372492094099164))

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

    def test_invalid_prefix_length15(self):
        # invalid prefix for length 15
        for i in (
            100000000000000,
            200000000000000,
            300000000000000,
            351786522775107,
            362492094099164,
            400000000000000,
            500000000000000,
            600000000000000,
            700000000000000,
            800000000000000,
            900000000000000
        ):
            with self.subTest(i=i):
                self.assertFalse(credit_card_validator(i))

    def test_invalid_prefixes_length16(self):
        for i in (
            1000000000000000,
            2000000000000000,
            3000000000000000,
            5000000000000000,
            6000000000000000,
            7000000000000000,
            8000000000000000,
            9000000000000000
        ):
            with self.subTest(i=i):
                self.assertFalse(credit_card_validator(i))

    def test_mastercard_invalid_length_valid_check(self):
        """Verifies if Master Cards with invalid lengths
        and valid check bits returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator(513784674839468))
        self.assertFalse(credit_card_validator(553783994839464))
        self.assertFalse(credit_card_validator(55378393452449462))
        self.assertFalse(credit_card_validator(51560693452449462))

    def test_visa_invalid_length_valid_check(self):
        """Verifies if Master Cards with invalid lengths
        and valid check bits returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator(439983737393031))
        self.assertFalse(credit_card_validator(49388839032114035))

    def test_amex_invalid_length_valid_check(self):
        """Verifies if Master Cards with invalid lengths
        and valid check bits returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator(34958576497456))
        self.assertFalse(credit_card_validator(3494888332097455))
        self.assertFalse(credit_card_validator(37892736598027))
        self.assertFalse(credit_card_validator(3794889033097452))


if __name__ == '__main__':
    unittest.main()
