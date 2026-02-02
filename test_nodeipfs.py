# test_nodeipfs.py
"""
Tests for NodeIPFS module.
"""

import unittest
from nodeipfs import NodeIPFS

class TestNodeIPFS(unittest.TestCase):
    """Test cases for NodeIPFS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeIPFS()
        self.assertIsInstance(instance, NodeIPFS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeIPFS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
