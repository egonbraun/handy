import unittest

from handy.helpers.security import *


class EnvironmentTestCase(unittest.TestCase):
    """helpers/security test cases."""

    def test_default_password_length(self):
        self.assertEqual(DEFAULT_PASSWORD_LENGTH, 25)

    def test_generate_password(self):
        self.assertEqual(len(generate_password()), 25)
        self.assertEqual(len(generate_password(10)), 10)
        self.assertEqual(len(generate_password(1000)), 1000)


if __name__ == '__main__':
    unittest.main()
