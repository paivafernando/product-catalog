import requests


class ProductCatalog:

  def get_products_by_category(self, category=None, max_price=None):
    """Fetches products from the API, applies category and max_price filters,

    and returns only the product names sorted accordingly.
    """
    
    if category is None or max_price is None:
      return []
    target_category = str(category).strip().lower()
    target_max_price = float(max_price)

    base_url = "https://jsonmock.hackerrank.com/api/inventory"
    first_response = requests.get(base_url).json()
    total_pages = first_response.get("total_pages",1)
    data = first_response.get("data",[])
    
    for page in range(2, total_pages+1):
      resp = requests.get(base_url, params={"page": page}).json()
      if resp.get("data", []) == []:
        break
      data.extend(resp.get("data",[]))
      
    def parse_price(val):
      try:
        return float(val) if val is not None else 0.0
      except (ValueError, TypeError):
        return 0.0

    filtered = [
      {**item, "price": parse_price(item.get("price"))}
      for item in data
      if str(item.get("category")).strip().lower() == target_category
      and parse_price(item.get("price")) <= target_max_price
    ]

    sorted_products = sorted(filtered, key=lambda x: (-x["price"], x["name"]))

    names = [
      product.get('name') for product in sorted_products
      ]
    return names
