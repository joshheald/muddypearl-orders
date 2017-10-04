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
        
        text_for_identifier_mock.assert_called_with("Email:", order)

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

    @patch('orderparser.storeorderparser.mputils.text_for_identifier')
    def test_customerFirstNameFromOrder_callsTextFromIdentifier_WithCorrectIdentifier(self, text_for_identifier_mock):
        storeorderparser.customer_first_name("order text")
        text_for_identifier_mock.assert_called_with("Name:", "order text")

    @patch('orderparser.storeorderparser.mputils.text_for_identifier')
    def test_customerFirstNameFromOrder_twoWords_returnsFirstWord(self, text_for_identifier_mock):
        text_for_identifier_mock.return_value = "Samantha McIntire"
        actual = storeorderparser.customer_first_name("text that doesn't really matter because it's mocked anyway")
        self.assertEqual(actual, "Samantha")

    @patch('orderparser.storeorderparser.mputils.text_for_identifier')
    def test_customerFirstNameFromOrder_firstWordHasApostrophe_returnsFirstWord(self, text_for_identifier_mock):
        text_for_identifier_mock.return_value = "M'chael Widdershins"
        actual = storeorderparser.customer_first_name("there's no name here but it doesn't matter")
        self.assertEqual(actual, "M'chael")

    @patch('orderparser.storeorderparser.mputils.text_for_identifier')
    def test_customerFirstNameFromOrder_firstWordHasHyphen_returnsFullWord(self, text_for_identifier_mock):
        text_for_identifier_mock.return_value = "Sammie-Ann Bolton"
        actual = storeorderparser.customer_first_name("order text")
        self.assertEqual(actual, "Sammie-Ann")

    @patch('orderparser.storeorderparser.mputils.text_for_identifier')
    def test_customewFirstNameFromOrder_ThreeWords_returnsFirstTwoWords(self, text_for_identifier_mock):
        text_for_identifier_mock.return_value = "Anthony John Horrocks"
        actual = storeorderparser.customer_first_name("parsed stuff")
        self.assertEqual(actual, "Anthony John")





if __name__ == '__main__':
    unittest.main()