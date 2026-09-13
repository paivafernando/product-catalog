# Technical Challenge: Product Catalog API

## Description
Implement the `ProductCatalog` class to fetch, filter, and sort product data consumed from a mock REST API.

## Requirements

1. **Endpoint**: `https://jsonmock.hackerrank.com/api/inventory`
2. **Method**: `get_products_by_category(category, max_price)`
3. **Business Rules**:
   - Handle full pagination to retrieve all records returned by the API.
   - Filter products ensuring that:
     - They belong to the requested category (case-insensitive and stripping leading/trailing whitespace).
     - Their price is less than or equal to `max_price`.
   - Defensive price parsing: if the `price` field is missing, `None`, or invalid, default its value to `0.0`.
   - **Sorting**:
     - Primary criterion: `price` in **descending** order (highest to lowest).
     - Secondary criterion (tie-breaker): `name` in **ascending** order (alphabetical).
   - **Return**: A list containing only the names (`name`) of the filtered and sorted products.

## Sample Input
- **Category**: `"Electronics"`
- **Max Price**: `500.0`

## Sample Output
```text
Smart TV 4K
Gaming Monitor
Wireless Headphones
Bluetooth Speaker