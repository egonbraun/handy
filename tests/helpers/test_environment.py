import unittest

from handy.core.constants import Env
from handy.helpers.environment import *


class EnvironmentTestCase(unittest.TestCase):
    """helpers/environment test cases."""

    def test_env_short(self):
        self.assertIs(env_short(Env.ACCEPTANCE), "a")
        self.assertIsNot(env_short(Env.ACCEPTANCE), "A")
        self.assertIs(env_short(Env.COMMON), "c")
        self.assertIsNot(env_short(Env.COMMON), "C")
        self.assertIs(env_short(Env.DEVELOPMENT), "d")
        self.assertIsNot(env_short(Env.DEVELOPMENT), "D")
        self.assertIs(env_short(Env.PRODUCTION), "p")
        self.assertIsNot(env_short(Env.PRODUCTION), "P")
        self.assertIs(env_short(Env.SERVICES), "s")
        self.assertIsNot(env_short(Env.SERVICES), "S")
        self.assertIs(env_short(Env.TEST), "t")
        self.assertIsNot(env_short(Env.TEST), "T")

        with self.assertRaises(LookupError):
            env_short(Env.NONE)


if __name__ == "__main__":
    unittest.main()
