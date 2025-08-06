import subprocess
import sys
import unittest

class TestE2E(unittest.TestCase):
    def test_full_program_flow(self):
        # Simulate a real user session: enter starting capital then target goal
        process = subprocess.Popen(
            [sys.executable, "main.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Send inputs: 100 starting capital, 500 target goal
        stdout, stderr = process.communicate(input="100\n500\n", timeout=5)

        self.assertEqual(process.returncode, 0, f"Exited with code {process.returncode}, stderr: {stderr}")
        self.assertIn("Starting Capital: $100.00", stdout)
        self.assertIn("Target Profit Goal: $500.00", stdout)

if __name__ == '__main__':
    unittest.main()
