import unittest
from muddypearl import mputils

class ParserTest(unittest.TestCase):

    def test_textForIdentifier_None_returnsNone(self):
        actual = mputils.text_for_identifier(None, None)
        self.assertEqual(actual, None)

    def test_textForIdentifier_EmptyString_returnsWholeString(self):
        text = "sample text"
        actual = mputils.text_for_identifier("", text)
        self.assertEqual(actual, text)

    def test_textForIdentifier_ContainsIdentifiedText_returnsStringAfterIdentifier(self):
        actual = mputils.text_for_identifier("Email: ", "Email: hello@example.com")
        self.assertEqual(actual, "hello@example.com")

    def test_textForIdentifier_ContainsIdentifiedTextOnSecondLine_returnsEmailAfterIdentifier(self):
        text = """Some unrelated junk
        ID:isitme@yourelookingfor.com"""
        actual = mputils.text_for_identifier("ID:", text)
        self.assertEqual(actual, "isitme@yourelookingfor.com")

    def test_textForIdentifier_ContainsIdentifiedTextWithFollowingLines_returnsEmailOnly(self):
        text = """Stuff: can@youfind.me
        Even with other stuff in the file?"""
        actual = mputils.text_for_identifier("Stuff: ", text)
        self.assertEqual(actual, "can@youfind.me")

    def test_textForIdentifier_NoSpaceBeforeText_StillReturnsString(self):
        text = "ident:anEmail@email.mail"
        actual = mputils.text_for_identifier("ident:", text)
        self.assertEqual(actual, "anEmail@email.mail")
    
if __name__ == '__main__':
    unittest.main()