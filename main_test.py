import unittest

from main import Category, Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product("Laptop", "High-end gaming laptop", 1200, 5)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "High-end gaming laptop")
        self.assertEqual(product.price, 1200)
        self.assertEqual(product.quantity, 5)


class TestCategory(unittest.TestCase):
    def setUp(self):
        # Reset the class variables before each test
        Category.total_categories = 0
        Category.all_unique_products.clear()
        self.prod1 = Product("Laptop", "High-end gaming laptop", 1200, 5)
        self.prod2 = Product("Mouse", "Wireless mouse", 20, 20)
        self.prod3 = Product("Keyboard", "Mechanical keyboard", 70, 10)
        self.category1 = Category("Electronics", "Devices and gadgets", [self.prod1, self.prod2])
        self.category2 = Category("Computing Accessories", "Keyboards and mice", [self.prod2, self.prod3])

    def test_total_categories(self):
        self.assertEqual(Category.total_categories, 2)

    def test_all_unique_products(self):
        self.assertEqual(len(Category.all_unique_products), 3)
        self.assertIn(self.prod1, Category.all_unique_products)
        self.assertIn(self.prod2, Category.all_unique_products)
        self.assertIn(self.prod3, Category.all_unique_products)

    def test_add_product_updates_unique_products(self):
        new_product = Product("Tablet", "Portable device", 300, 7)
        self.category1.add_product(new_product)
        self.assertIn(new_product, Category.all_unique_products)
        self.assertEqual(len(Category.all_unique_products), 4)

    def test_remove_product_does_not_affect_all_unique_products(self):
        self.category1.remove_product(self.prod1)
        self.assertIn(self.prod1, Category.all_unique_products)
        self.assertEqual(len(Category.all_unique_products), 3)

    def test_add_price(self):
        p1 = Product("Laptop", "High-end gaming laptop", 100, 5)
        p2 = Product("Mouse", "Wireless mouse", 10, 20)
        self.assertEqual(p1 + p2, 700)
