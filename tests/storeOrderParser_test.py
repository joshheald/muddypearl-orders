import unittest
from unittest.mock import patch
from muddypearl import mputils

from orderparser import storeorderparser

class ParserTest(unittest.TestCase):

    @patch('orderparser.storeorderparser.mputils.text_for_identifier')
    def test_customerEmailFromOrder_callsTextFromIdentifier(self, text_for_identifier_mock):
        order = "Email:blahblah"
        text_for_identifier_mock.return_value = "blahblah"
        
        storeorderparser.customer_email_from_order(order)
        
        text_for_identifier_mock.assert_called_once_with("Email:", order)

    @patch('orderparser.storeorderparser.mputils.text_for_identifier')
    def test_customerEmailFromOrder_returnsNoneIfThatsWhatItGets(self, text_for_identifier_mock):
        text_for_identifier_mock.return_value = None
        actual = storeorderparser.customer_email_from_order("")
        self.assertEqual(actual, None)
    
    @patch('orderparser.storeorderparser.mputils.text_for_identifier')
    def test_customerEmailFromOrder_returnsTextIfItGetsSome(self, text_for_identifier_mock):
        text_for_identifier_mock.return_value = "blahblah"
        actual = storeorderparser.customer_email_from_order("")
        self.assertEqual(actual, "blahblah")

    @patch('orderparser.storeorderparser.mputils.text_for_identifier')
    def test_customerEmailFromOrder_returnsTextStrippedOfWhitespace(self, text_for_identifier_mock):
        text_for_identifier_mock.return_value = "   someemail@email.com \n"
        actual = storeorderparser.customer_email_from_order("")
        self.assertEqual(actual, "someemail@email.com")



if __name__ == '__main__':
    unittest.main()