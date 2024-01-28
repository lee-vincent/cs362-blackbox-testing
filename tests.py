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

    def test_visa_mastercard_prefix_invalid(self):
        """Verifies if Visas/MasterCards with invalid prefixes, valid lengths,
        and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(8823732446254233))

    def test_amex_prefix_invalid(self):
        """Verifies if America Express cards with invalid prefixes,
        valid lengths, and valid check digits returns False
        Picked using Manual Error Guessing Testing"""
        self.assertFalse(credit_card_validator(882373244625426))


if __name__ == '__main__':
    unittest.main()
