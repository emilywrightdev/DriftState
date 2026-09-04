# test_driftstate.py
"""
Tests for DriftState module.
"""

import unittest
from driftstate import DriftState

class TestDriftState(unittest.TestCase):
    """Test cases for DriftState class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DriftState()
        self.assertIsInstance(instance, DriftState)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DriftState()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
