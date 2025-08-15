# .map() - applies the same operation to every item (like painting all cars red)

# .filter() - selects items that meet criteria (like quality control inspection)

# Basic map - applying a function to every item
numbers = [1, 2, 3, 4, 5]

# Traditional approach
squares_tradtional = []
for num in numbers:
    squares_tradtional.append(num ** 2)
    
# Syntax for map:
# .map(function, list) - where the function is an operation that is applied to every item in the list
# One thing to keep in mind is map returns map objects, which should be converted back to a list with list()

# Functional approach with map
squares_functional = list(map(lambda x: x ** 2, numbers))

print(f"Traditional: {squares_tradtional}")
print(f"Functional: {squares_functional}")

# Real-world example: Processing user data
users = [
    {'name': 'alice johnson', 'email': 'ALICE@EMAIL.COM'},
    {'name': 'bob smith', 'email': 'BOB@EMAIL.COM'},
    {'name': 'charlie brown', 'email': 'CHARLIE@EMAIL.COM'}
]

# Clean and normalize user_data
def normalize_user(user):
    return {
        'name': user['name'].title(),
        'email': user['email'].lower(),
        'username': user['name'].replace(' ', '_').lower()
    }
    
# Using map for batch processing
normalized_users = list(map(normalize_user, users))

print(normalized_users)

# Or with lambda for simple tranformations
uppercase_names = list(map(lambda u: u['name'].upper(), users))
print(f"Uppercase names: {uppercase_names}")


# Muliple iterables - zip functionality
prices = [10.99, 25.50, 8.75]
quantities = [2, 1, 4]
items = ['laptop', 'mouse', 'cable']

# Calculate totals for each item
totals = list(map(lambda price, qty: price * qty, prices, quantities))
print(f"Item totals: {totals}")

# Create invoice lines
invoice_lines = list(map(
    lambda item, price, qty: f"{item}: {qty} x ${price:.2f} = ${price * qty:.2f}",
    items, prices, quantities
))

#invoice_lines = list(map(lambda item, price, qty: f"{item}: {qty} x ${price:.2f} = ${price * qty:.2f}",items, prices, quantities))

for line in invoice_lines:
    print(line)
    
    
# Basic filtering
numbers = list(range(-5, 6))  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Traditional approach
positive_traditional = []
for num in numbers:
    if num > 0:
        positive_traditional.append(num)
        

#Syntax for filter:
# filter(function, list) Where the function returns a boolean (T/F) for every item, 
# True means the item passes through, false means the item is filtered out.

#NOTE: Filter returns a filter object that should be converted to a list with list()

# Functional approach
positive_functional = list(filter(lambda x: x > 0, numbers))

print(f"Traditional: {positive_traditional}")  # [1, 2, 3, 4, 5]
print(f"Functional:  {positive_functional}")   # [1, 2, 3, 4, 5]


# Real-world example: Data validation and filtering
transactions = [
    {'id': 1, 'amount': 100.0, 'type': 'debit', 'valid': True},
    {'id': 2, 'amount': -50.0, 'type': 'credit', 'valid': False},
    {'id': 3, 'amount': 200.0, 'type': 'debit', 'valid': True},
    {'id': 4, 'amount': 0.0, 'type': 'debit', 'valid': True},
    {'id': 5, 'amount': 75.0, 'type': 'credit', 'valid': True}
]

# Filter valid transactions
valid_transactions = list(filter(lambda t: t['valid'], transactions))

# Filter by transaction type
debits = list(filter(lambda t: t['type'] == 'debit', valid_transactions))
credits = list(filter(lambda t: t['type'] == 'credit', valid_transactions))

# Filter by amount threshold
large_transactions = list(filter(lambda t: t['amount'] >= 100.0, valid_transactions))

print(f"Valid debits: {len(debits)}")
print(f"Valid credits: {len(credits)}")
print(f"Large transactions: {[t['id'] for t in large_transactions]}")

# Advanced filtering with multiple conditions
def is_significant_debit(transaction):
    return (transaction['valid'] and 
            transaction['type'] == 'debit' and 
            transaction['amount'] > 50.0)
    
significant_debits = list(filter(is_significant_debit, transactions))
print(f"Significant debits: {[t['id'] for t in significant_debits]}")

# for t in significant_debits:
#     t['id']


# Chaining map and filter operations
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get squares of even numbers
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Squares of even numbers: {even_squares}")  # [4, 16, 36, 64, 100]

# Real-world example: Processing sales data
sales_data = [
    {'region': 'North', 'sales': 10000, 'units': 50},
    {'region': 'South', 'sales': 15000, 'units': 75},
    {'region': 'East', 'sales': 12000, 'units': 60},
    {'region': 'West', 'sales': 18000, 'units': 90}
]

# Get regions with high sales (> 12000) and calculate per-unit value
high_performing_regions = list(
    map(lambda region: {
        **region,
        'per_unit_value': region['sales'] / region['units']
    }, filter(lambda region: region['sales'] > 12000, sales_data))
)

print(high_performing_regions)

print("High-performing regions:")
for region in high_performing_regions:
    print(f"  {region['region']}: ${region['per_unit_value']:.2f} per unit")
    
total_sales = sum(region['sales'] for region in sales_data)
print(f"Total sales: ${total_sales:,}")  # $55,000

# Find top region using built-in max()
top_region = max(sales_data, key=lambda region: region['sales'])
print(f"Top region: {top_region['region']} with ${top_region['sales']:,}")