import unittest
from unittest.mock import MagicMock, patch
from src.catalog import ProductCatalog


class TestProductCatalog(unittest.TestCase):

  def setUp(self):
    self.catalog = ProductCatalog()

  @patch("requests.get")
  def test_get_products_filtering_and_sorting(self, mock_get):
    # Mocked API response (1 page with 5 items)
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "page": 1,
        "total_pages": 1,
        "data": [
            {"name": "Bluetooth Speaker", "category": "Electronics", "price": 150.0},
            {"name": "Smart TV 4K", "category": "Electronics", "price": 450.0},
            {"name": "Gaming Monitor", "category": "Electronics", "price": 450.0},
            {"name": "Office Chair", "category": "Furniture", "price": 200.0},
            {"name": "Expensive Laptop", "category": "Electronics", "price": 1200.0},
        ],
    }
    mock_get.return_value = mock_response

    results = self.catalog.get_products_by_category("Electronics", 500.0)

    # Assertions:
    # 1. Excludes items above 500.0 (Expensive Laptop) and other categories (Office Chair)
    # 2. Tie-breaker for equal prices (450.0): 'Gaming Monitor' comes before 'Smart TV 4K' alphabetically
    expected = [
        "Gaming Monitor",
        "Smart TV 4K",
        "Bluetooth Speaker",
    ]
    self.assertEqual(results, expected)

  @patch("requests.get")
  def test_invalid_price_fallback_to_zero(self, mock_get):
    # Mock items with invalid or missing price
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "page": 1,
        "total_pages": 1,
        "data": [
            {"name": "Free Cable", "category": "Electronics", "price": None},
            {"name": "Adapter", "category": "Electronics", "price": "invalid"},
        ],
    }
    mock_get.return_value = mock_response

    results = self.catalog.get_products_by_category("Electronics", 100.0)

    # Both fallback to 0.0 and get sorted alphabetically by name
    expected = ["Adapter", "Free Cable"]
    self.assertEqual(results, expected)

  def test_empty_input_returns_empty_list(self):
    self.assertEqual(self.catalog.get_products_by_category(None, 500.0), [])
    self.assertEqual(self.catalog.get_products_by_category("Electronics", None), [])


if __name__ == "__main__":
  unittest.main()