products = [
    {'name': 'Wireless Headphones', 'price': 89.99, 'category': 'Electronics', 'stock': 45},
    {'name': 'Coffee Maker', 'price': 129.99, 'category': 'Appliances', 'stock': 12},
    {'name': 'Running Shoes', 'price': 79.99, 'category': 'Sports', 'stock': 23},
    {'name': 'Bluetooth Speaker', 'price': 59.99, 'category': 'Electronics', 'stock': 67},
    {'name': 'Yoga Mat', 'price': 24.99, 'category': 'Sports', 'stock': 8}
]

# TODO: Sort products by price (highest first)
by_price = sorted(products, key=lambda product: -product['price'])

# TODO: Sort products by category, then by name alphabetically
by_category_name = sorted(products, key=lambda product: (product['category'], product['name']))

# Test your sorting
print(by_price)
print(by_category_name)
print("Most expensive:", by_price[0]['name'])
print("First alphabetically:", by_category_name[0]['name'])


# TODO: Create a lambda to determine price category
# - Price >= 100: 'Premium'
# - Price <= 50: 'Budget'  
# - Otherwise: 'Standard'
price_category = lambda price: 'Premium' if price >= 100 else 'Budget' if price <= 50 else 'Standard'

# TODO: Create a lambda to check stock status
# - Stock <= 10: 'Low Stock'
# - Otherwise: 'In Stock'
stock_status = lambda stock: 'Low Stock' if stock <= 10 else 'In Stock'

# Test your lambdas
print("Product Status Report:")
for product in products:
    category = price_category(product['price'])
    status = stock_status(product['stock'])
    print(f"{product['name']}: {category}, {status}")