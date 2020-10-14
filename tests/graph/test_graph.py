import unittest

from handy.graph import Edge, Graph, Vertex


class EdgeTestCase(unittest.TestCase):
    """graph test cases."""

    def test_default_password_length(self):
        self.assertEqual(DEFAULT_PASSWORD_LENGTH, 25)


if __name__ == '__main__':
    unittest.main()
