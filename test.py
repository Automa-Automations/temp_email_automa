import unittest
from temp_email_automa.main import TempMail, Email


class TestTempMail(unittest.TestCase):
    def setUp(self):
        self.temp_mail = TempMail()

    def test_generate_random_email_address(self):
        self.temp_mail.generate_random_email_address()
        self.assertIsNotNone(self.temp_mail.login)
        self.assertIsNotNone(self.temp_mail.domain)

    def test_get_list_of_active_domains(self):
        domains = self.temp_mail.get_list_of_active_domains()
        self.assertIsInstance(domains, list)
        self.assertGreater(len(domains), 0)

    def test_get_email_list(self):
        self.temp_mail.generate_random_email_address()
        emails = self.temp_mail.get_list_of_emails()
        self.assertIsInstance(emails, list)

    def test_get_single_email(self):
        self.temp_mail.generate_random_email_address()
        emails = self.temp_mail.get_list_of_emails()
        if emails:
            email = self.temp_mail.get_single_email(emails[0]["id"])
            self.assertIsInstance(email, Email)
        else:
            self.skipTest("No emails found")


if __name__ == "__main__":
    unittest.main()
