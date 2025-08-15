lambda x: x**2

def square(num):
    return num ** 2


# Lambda Function Anatomy:

# lambda argumnents: expression

# keyword  input       what to return

# Examples:
lambda x: x * 2                   # Double a number
lambda x, y: x + y                # Add two numbers
lambda name: name.upper()         # Convert to uppercase
lambda item: item['price'] > 10   # Check if price > 10


# Traditional function approach
def calculate_tax(price):
    return price * 0.08

def is_adult(age):
    return age >= 18

def format_name(first, last):
    return f"{last}, {first}"

# Equivalent lambda functions
calculate_tax2 = lambda price: price * 0.08
is_adult2 = lambda age: age >= 18
format_name2 = lambda first, last: f"{last}, {first}"


products = [
    {"name": 'laptop', "price": 999.99},
    {"name": 'mouse', "price": 25.99},
    {"name": 'keyboard', "price": 89.99}
]

sorted_products = sorted(products, key = lambda product: product['price'])
print(f"Cheapest: {sorted_products[0]['name']}")


# Pattern 1: Sorting with custom keys
students = [
    {'name': 'Jerry', 'grade': 93, 'age': 21},
    {'name': 'Marie', 'grade': 75, 'age': 24},
    {'name': 'Anna', 'grade': 75, 'age': 35},
    {'name': 'Frank', 'grade': 80, 'age': 23},
    {'name': 'Mark', 'grade': 80, 'age': 50}
]

# Sort by grade (descending)
# by_grade = sorted(students, key=lambda s: s['grade'], reverse=True)

# Sort by multiple criteria
# by_grade_then_age = sorted(students, key=lambda s: (-s['grade'], s['age']))

# Pattern 2: Conditional logic in lambdas
assign_letter_grade = lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'


# by_grade = sorted(students, key=lambda s: s['grade'], reverse=True)
# by_grade2 = sorted(students, key=lambda s: -s['grade'])

# print(by_grade)
# print(by_grade2)

by_grade_then_age = sorted(students, key=lambda x: (-x['grade'], -x['age']))
# by_grade_then_age2 = sorted(students, key=lambda s: (s['grade'], s['age']))

print(by_grade_then_age)
# print(by_grade_then_age2)