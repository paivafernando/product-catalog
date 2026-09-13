import requests


class ProductCatalog:

  def get_products_by_category(self, category=None, max_price=None):
    """Fetches products from the API, applies category and max_price filters,

    and returns only the product names sorted accordingly.
    """
    if category is None or max_price is None:
      return []

    # TODO: 1. Sanitize input parameters (types and string formatting)

    # TODO: 2. Make the initial API request to retrieve initial data and total_pages
    # Base URL: https://jsonmock.hackerrank.com/api/inventory

    # TODO: 3. Loop through remaining pages to collect the entire dataset

    # TODO: 4. Handle invalid prices (None/ValueError -> 0.0) and filter by category and max_price

    # TODO: 5. Sort by price (descending) and name (ascending)

    # TODO: 6. Return the list of product names
    pass
