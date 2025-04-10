#!/usr/bin/env python3

import unittest
import io
import sys
from main import main


class TestMain(unittest.TestCase):
    def test_main_output(self):
        """Test that main() prints 'Hello World!'"""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello World!")


if __name__ == "__main__":
    unittest.main()
