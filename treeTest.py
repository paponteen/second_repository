import unittest

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert_and_find(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        
        self.assertTrue(self.bst.find(10))
        self.assertTrue(self.bst.find(5))
        self.assertTrue(self.bst.find(15))
        self.assertFalse(self.bst.find(8))
        
    def test_higher(self):
        self.bst.insert(20)
        self.bst.insert(10)
        self.bst.insert(30)
        self.bst.insert(25)

        self.assertEqual(self.bst.higher(10), 20)
        self.assertEqual(self.bst.higher(25), 30)
        with self.assertRaises(ValueError):
            self.bst.higher(40)  # Value not in the tree

        with self.assertRaises(ValueError):
            self.bst.higher(30)  # No higher value

    def test_lower(self):
        self.bst.insert(20)
        self.bst.insert(10)
        self.bst.insert(30)
        self.bst.insert(25)

        self.assertEqual(self.bst.lower(30), 25)
        self.assertEqual(self.bst.lower(20), 10)
        with self.assertRaises(ValueError):
            self.bst.lower(5)  # Value not in the tree

        with self.assertRaises(ValueError):
            self.bst.lower(10)  # No lower value

    def test_find_empty_tree(self):
        self.assertFalse(self.bst.find(10))
        with self.assertRaises(ValueError):
            self.bst.higher(10)
        with self.assertRaises(ValueError):
            self.bst.lower(10)

if __name__ == '__main__':
    unittest.main()
