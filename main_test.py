import unittest

from main import Category, Product

class TestCategoryAndProduct(unittest.TestCase):
    def test_category_initialization(self):
        category = Category("Electronics", "Electronic devices")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Electronic devices")
        self.assertEqual(category.products, [])

    def test_product_initialization(self):
        product = Product("Smartphone", "Smartphone with a good camera", 500, 10)
        self.assertEqual(product.name, "Smartphone")
        self.assertEqual(product.description, "Smartphone with a good camera")
        self.assertEqual(product.price, 500)
        self.assertEqual(product.quantity, 10)

    def test_product_count(self):
        category = Category("Electronics", "Electronic devices")
        product1 = Product("Smartphone", "Smartphone with a good camera", 500, 10)
        product2 = Product("Laptop", "Lightweight and powerful laptop", 1200, 5)
        category.add_product(product1)
        category.add_product(product2)
        self.assertEqual(len(category.products), 2)

    def test_category_count(self):
        Category("Electronics", "Electronic devices")
        Category("Clothing", "Fashionable clothing")
        self.assertEqual(Category.total_categories, 2)

