employees = [
    {'name': 'Alice Johnson', 'job': 'Developer', 'salary': 75000},
    {'name': 'Bob Smith', 'job': 'Designer', 'salary': 65000},
    {'name': 'Carol Davis', 'job': 'Manager', 'salary': 85000},
    {'name': 'David Wilson', 'job': 'Analyst', 'salary': 55000},
    {'name': 'Emma Brown', 'job': 'Developer', 'salary': 72000}
]

# TODO: Use map() with lambda to create new employee dicts with 7% salary raise
updated_employees = list(map(
    lambda e: {
        'name': e['name'],
        'job': e['job'],
        'salary': round(e['salary'] * 1.07, 2)
    },
    employees
))

# Test your result
print("Original employees:")
for emp in employees:
    print(f"  {emp['name']} ({emp['job']}): ${emp['salary']:,}")

print("\nAfter 7% raise:")
for emp in updated_employees:
    print(f"  {emp['name']} ({emp['job']}): ${emp['salary']:,.2f}")