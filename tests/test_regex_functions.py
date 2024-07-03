import unittest
from regex_solutions.regex_functions import anonymize_emails, format_date, standardize_phone, normalize_whitespace, remove_html_tags

class TestRegexFunctions(unittest.TestCase):

    def test_anonymize_emails(self):
        self.assertEqual(anonymize_emails("Contact us at support@example.com"), "Contact us at [email]")
        self.assertEqual(anonymize_emails("Email me at john.doe123@example.org for details."), "Email me at [email] for details.")
        self.assertEqual(anonymize_emails("No emails in this string."), "No emails in this string.")

    def test_format_date(self):
        self.assertEqual(format_date("Event on 12/05/2023"), "Event on 2023-05-12")
        self.assertEqual(format_date("Due date is 31-12-2023"), "Due date is 2023-12-31")
        self.assertEqual(format_date("The date 2023.01.01 marks a new year."), "The date 2023-01-01 marks a new year.")

    def test_standardize_phone(self):
        self.assertEqual(standardize_phone("Call +359-88-7123-456 for assistance"), "Call +359 88 7123 456 for assistance")
        self.assertEqual(standardize_phone("My number is +359 879123 456"), "My number is +359 87 9123 456")
        self.assertEqual(standardize_phone("Emergency number: +359878123456"), "Emergency number: +359 87 8123 456")

    def test_normalize_whitespace(self):
        self.assertEqual(normalize_whitespace("This  text   has  extra   spaces"), "This text has extra spaces")
        self.assertEqual(normalize_whitespace("Line with\nnew line character"), "Line with new line character")
        self.assertEqual(normalize_whitespace("Tab\tcharacter\ttest"), "Tab character test")

    def test_remove_html_tags(self):
        self.assertEqual(remove_html_tags("<p>Some <b>bold</b> text</p>"), "Some bold text")
        self.assertEqual(remove_html_tags("No <a href='link'>HTML</a> tags!"), "No HTML tags!")
        self.assertEqual(remove_html_tags("<div><span>Nested <i>tags</i></span></div>"), "Nested tags")

if __name__ == '__main__':
    unittest.main()
