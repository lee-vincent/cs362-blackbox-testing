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

    def test_mastercard_51_valid(self):
        """Verifies if MasterCards with 51 prefixes, valid lengths,
        and valid check digits returns True
        Picked using Manual Boundary Value Testing"""
        self.assertTrue(credit_card_validator(5126396502239288))

    def test_mastercard_55_valid(self):
        """Verifies if MasterCards with 55 prefixes, valid lengths,
        and valid check digits returns True
        Picked using Manual Boundary Value Testing"""
        self.assertTrue(credit_card_validator(5574726700232866))

    def test_mastercard_2720_valid(self):
        """Verifies if MasterCards with 2720 prefixes, valid lengths,
        and valid check digits returns True
        Picked using Manual Boundary Value Testing"""
        self.assertTrue(credit_card_validator(2720926415343830))

    def test_mastercard_2221_valid(self):
        """Verifies if MasterCards with 2221 prefixes, valid lengths,
        and valid check digits returns True
        Picked using Manual Boundary Value Testing"""
        self.assertTrue(credit_card_validator(2221858293648259))

    def test_visa_4_valid(self):
        """Verifies if Visas with 4 prefixes, valid lengths,
        and valid check digits returns True
        Picked using Manual Boundary Value Testing"""
        self.assertTrue(credit_card_validator(4532782263081517))

    def test_amex_34_valid(self):
        """Verifies if America Express cards with 34 prefixes, valid lengths,
        and valid check digits returns True
        Picked using Manual Boundary Value Testing"""
        self.assertTrue(credit_card_validator(341786522775107))

    def test_amex_37_valid(self):
        """Verifies if America Express cards with 37 prefixes, valid lengths,
        and valid check digits returns True
        Picked using Manual Boundary Value Testing"""
        self.assertTrue(credit_card_validator(372492094099164))

        ###############################################################

    def test_mastercard_51_checkdigit_invalid(self):
        """Verifies if MasterCards with 51 prefixes, valid lengths,
        and invalid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(5126396502239280))

    def test_mastercard_55_checkdigit_invalid(self):
        """Verifies if MasterCards with 55 prefixes, valid lengths,
        and invalid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(5574726700232860))

    def test_mastercard_2720_checkdigit_invalid(self):
        """Verifies if MasterCards with 2720 prefixes, valid lengths,
        and invalid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(2720926415343835))

    def test_mastercard_2221_checkdigit_invalid(self):
        """Verifies if MasterCards with 2221 prefixes, valid lengths,
        and invalid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(2221858293648250))

    def test_visa_4_checkdigit_invalid(self):
        """Verifies if Visas with 4 prefixes, valid lengths,
        and invalid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(4532782263081510))

    def test_amex_34_checkdigit_invalid(self):
        """Verifies if America Express cards with 34 prefixes, valid lengths,
        and invalid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(341786522775100))

    def test_amex_37_checkdigit_invalid(self):
        """Verifies if America Express cards with 37 prefixes, valid lengths,
        and invalid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(372492094099160))

        ###############################################################

    def test_mastercard_51_length_short_invalid(self):
        """Verifies if MasterCards with 51 prefixes, invalid lengths (short),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(513784674839468))

    def test_mastercard_55_length_short_invalid(self):
        """Verifies if MasterCards with 55 prefixes, invalid lengths (short),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(553783994839464))

    def test_mastercard_2221_length_short_invalid(self):
        """Verifies if MasterCards with 2221 prefixes, invalid lengths (short),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(222123432423236))

    def test_mastercard_2720_length_short_invalid(self):
        """Verifies if MasterCards with 2720 prefixes, invalid lengths (short),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(272075483910348))

    def test_mastercard_51_length_long_invalid(self):
        """Verifies if MasterCards with 51 prefixes, invalid lengths (long),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(55378393452449462))

    def test_mastercard_55_length_long_invalid(self):
        """Verifies if MasterCards with 55 prefixes, invalid lengths (long),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(55378393452449462))

    def test_mastercard_2221_length_long_invalid(self):
        """Verifies if MasterCards with 2221 prefixes, invalid lengths (long),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(22218373999372124))

    def test_mastercard_2720_length_long_invalid(self):
        """Verifies if MasterCards with 2720 prefixes, invalid lengths (long),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(27207548123910343))

    def test_visa_4_length_long_invalid(self):
        """Verifies if Visas with 4 prefixes, invalid lengths (long),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(49388839032114035))

    def test_visa_4_length_short_invalid(self):
        """Verifies if Visas with 4 prefixes, invalid lengths (short),
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(439983737393031))

    def test_amex_34_length_short_invalid(self):
        """Verifies if America Express cards with 34 prefixes,
        invalid lengths (short), and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(34958576497456))

    def test_amex_34_length_long_invalid(self):
        """Verifies if America Express cards with 34 prefixes,
        invalid lengths (long), and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(3494888332097455))

    def test_amex_37_length_short_invalid(self):
        """Verifies if America Express cards with 37 prefixes,
        invalid lengths (short), and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(37892736598027))

    def test_amex_37_length_long_invalid(self):
        """Verifies if America Express cards with 37 prefixes,
        invalid lengths (long), and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(3794889033097452))

        ###############################################################

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


if __name__ == '__main__':
    unittest.main()
