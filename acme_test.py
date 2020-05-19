import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
import io
import sys


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        """Test stealability method"""
        prod = Product('Test Product', 5, 10)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        prod.stealability()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Kinda stealable.\n")

    def test_explode(self):
        """Test test_explode method"""
        prod = Product('Test Product', 5, 10, 20)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        prod.explode()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "...BABOOM!!\n")

class AcmeReportTests(unittest.TestCase):
    
    def test_default_num_products(self):
        '''checks that it really does receive a list oflength 30'''
        self.assertEqual(len(generate_products()), 30)
    
    def test_legal_names(self):
        '''checks that the generated names for a default batch of products are all valid 
            possible names to generate (adjective, space, noun, from the lists of possible words)
        '''
        products = generate_products()
        for i in range(len(products)):
            split_string = products[i].name.split(" ")
            self.assertIn(split_string[0], ADJECTIVES)
            self.assertIn(split_string[1], NOUNS)

if __name__ == '__main__':
    unittest.main()