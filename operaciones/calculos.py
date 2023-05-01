import unittest
from operaciones import *

a, b, c, d = (10, 5, 0, "Hola")

class ComprobacionTestCase(unittest.TestCase):
    def test_suma_y_resta(self):
        self.assertEqual( "{} + {} = {}".format(a, b, suma(a, b) ), "10 + 5 = 15.0")
        self.assertEqual( "{} * {} = {}".format(b, b, producto(b, b) ), "5 * 5 = 25.0")

    def test_errores(self):
     with self.assertRaises( TypeError ):
            print("{} - {} = {}".format(b, d, resta(b, d)) )
     with self.assertRaises( ZeroDivisionError ):
         print("{} / {} = {}".format(a, c, division(a, c) ))
if __name__ == '__main__':
    unittest.main()