#===================Dictionary Methods with Time Complexity

cars = {
    "Honda": "Civic",
    "Hyundai": "Santa Fe",
    "Toyota": "Supra"
}

#===================== Accessing an item in the dictionary   - O(1)

#Keying into a dictionary - constant time O(1)
print(cars['Honda'])
#.get(key) - constant O(1) (safe way to get info from a dictionary while avoiding keyerrors (accessing a key that doesnt exist))
print(cars.get('Toyota'))

#=================== Adding items to a dictionary ======================

cars["Ford"] = 'Focus'   # Happens in constant time - O(1) -- Note: Dictionaries are not orders. So there is not need for reordering anything 

#============== Removing items from a dictionary

del cars['Ford'] # Constant O(1) time
print(cars)

#======================== Membership checks =============

if 'Honda' in cars:  # Constant time O(1) - Once again, dictionaries are not ordered, so this is not iterating through the dictionary, but using the key to get the item
    print("Found Honda!")
    
#==========Iteration ===============

for key in cars:  # O(n) Linear time. Has to iterate through the dictionary to print out the key for each of the items
    print(f"{key}")
    
    
#=================== Length of Dictionary

print(len(cars))  # O(1) the dictionary stores its size, so it is a constant time operation