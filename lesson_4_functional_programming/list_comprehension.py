# These are equivalent:
numbers = [1, 2, 3, 4, 5]

# Using map and filter
squares_of_evens_functional = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# Using comprehension
squares_of_evens_comprehension = [x**2 for x in numbers if x % 2 == 0]

# Both produce: [4, 16]


 # Comprehension Anatomy
# [expression for item in iterable if condition]
#     ↓         ↓         ↓              ↓
#   what       loop      data          filter
# to create variable source  (optional)

# Basic transformations
numbers = range(1, 6)  # [1, 2, 3, 4, 5]

# Simple transformation
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# With filtering
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16]

# String operations
words = ['hello', 'world', 'python', 'programming']
capitalized = [word.upper() for word in words]
long_words = [word for word in words if len(word) > 5]

print(capitalized)  # ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']
print(long_words)   # ['python', 'programming']

# Real-world example: Processing employee data
employees = [
    {'name': 'Alice Johnson', 'department': 'Engineering', 'salary': 85000, 'years': 3},
    {'name': 'Bob Smith', 'department': 'Marketing', 'salary': 65000, 'years': 1},
    {'name': 'Carol Davis', 'department': 'Engineering', 'salary': 92000, 'years': 5},
    {'name': 'David Wilson', 'department': 'Sales', 'salary': 58000, 'years': 2}
]

# Filter high earners only
high_earners = [emp for emp in employees if emp['salary'] > 70000]
print(f"High earners: {len(high_earners)} employees")

# Transform employees into new dictionary format with calculated fields
employee_reports = [
    {
        'full_name': emp['name'],
        'dept': emp['department'],
        'annual_salary': emp['salary'],
        'monthly_salary': emp['salary'] // 12,
        'experience_level': 'Senior' if emp['years'] >= 4 else 'Junior',
        'bonus_eligible': emp['salary'] > 60000 and emp['years'] >= 2
    }
    for emp in employees
]

# Display the transformed data
print("Employee Report Summary:")
for report in employee_reports:
    status = "✓" if report['bonus_eligible'] else "✗"
    print(f"{report['full_name']} ({report['dept']}) - {report['experience_level']} - Bonus: {status}")

# Filter and transform in one step - senior engineers only
senior_engineers = [
    {
        'name': emp['name'],
        'salary_with_bonus': emp['salary'] * 1.15,  # 15% bonus
        'years': emp['years']
    }
    for emp in employees 
    if emp['department'] == 'Engineering' and emp['years'] >= 4
]

print(f"\nSenior Engineers with bonus: {len(senior_engineers)} found")