import unittest
from orderparser import storeorderparser

class ParserTest(unittest.TestCase):

    def test_customerEmailFromOrder_None_returnsNone(self):
        actual = storeorderparser.customer_email_from_order(None)
        self.assertEqual(actual, None)

    def test_customerEmailFromOrder_EmptyString_returnsNone(self):
        actual = storeorderparser.customer_email_from_order("")
        self.assertEqual(actual, None)

    def test_customerEmailFromOrder_OrderContainsIdentifiedEmailAddress_returnsStringAfterIdentifier(self):
        actual = storeorderparser.customer_email_from_order("Email: hello@example.com")
        self.assertEqual(actual, "hello@example.com")

    def test_customerEmailFromOrder_OrderContainsIdentifiedEmailAddressOnSecondLine_returnsEmailAfterIdentifier(self):
        order = """Some unrelated junk
        Email: isitme@yourelookingfor.com"""
        actual = storeorderparser.customer_email_from_order(order)
        self.assertEqual(actual, "isitme@yourelookingfor.com")

    def test_customerEmailFromOrder_OrderContainsIdentifiedEmailAddressWithFollowingLines_returnsEmailOnly(self):
        order = """Email: can@youfind.me
        Even with other stuff in the file?"""
        actual = storeorderparser.customer_email_from_order(order)
        self.assertEqual(actual, "can@youfind.me")

    def test_customerEmailFromOrder_NoSpaceBeforeEmail_StillReturnsString(self):
        order = "Email:anEmail@email.mail"
        actual = storeorderparser.customer_email_from_order(order)
        self.assertEqual(actual, "anEmail@email.mail")
    
    """
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    """
if __name__ == '__main__':
    unittest.main()