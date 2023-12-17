# test_stock.py

import unittest
import stock

s = stock.Stock('GOOG', 100, 490.1)

class TestStock(unittest.TestCase):
    def test_create(self):
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertAlmostEqual(s.price, 490.1, 4)

    def test_cost(self):
        self.assertAlmostEqual(s.cost, 49010.00, 4)

    def test_sell(self):
        s.sell(50)
        self.assertEqual(s.shares, 50)
        self.assertRaises(ValueError, s.sell, s.shares+1)

    def test_set_bad_name(self):
        self.assertRaises(TypeError, setattr, s, 'name', 1)

    def test_set_bad_shares(self):
        self.assertRaises(TypeError, setattr, s, 'shares', '1')

    def test_set_bad_price(self):
        # An alternative
        with self.assertRaises(TypeError):
            s.price = '1.0'

if __name__ == '__main__':
    unittest.main()
