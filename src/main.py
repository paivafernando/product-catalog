from catalog import ProductCatalog


def main():
  catalog = ProductCatalog()

  category = "Electronics"
  max_price = 500.0

  print(
      f"Fetching products for category '{category}' up to ${max_price}...\n"
  )
  results = catalog.get_products_by_category(
      category=category, max_price=max_price
  )

  if not results:
    print("No products found.")
  else:
    for product_name in results:
      print(product_name)


if __name__ == "__main__":
  main()
