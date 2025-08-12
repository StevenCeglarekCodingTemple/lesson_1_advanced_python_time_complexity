#========== List Time Complexity =================

my_list = ["Eggs", "Milk", "Energy Drink", "Coffee", "Juice"]

#================== Accessing Items - Happens in Constant Time - 0(1)

print(my_list[0])

#=================== Adding Items to our list ===============

#.append() adds items to the end of the list - 0(1) Constant
my_list.append("Chicken")
print(my_list)

#.insert(n) - insert an item, and moves the other items around to accomodate  - O(n) Linear
my_list.insert(2, "Beef")
print(my_list)

#=================== Removing Elements ==================

#.remove() - all the items that come after what is removed, must shift over - O(n) Linear
my_list.remove("Milk")
print(my_list)

#.pop(n) or .pop() - With index is O(n) , without the index, it removes the last item in the list - O(1)
my_list.pop(3) # O(n)
my_list.pop() # O(1)

print(my_list)

#================ Membership checks ==================
#'in' - Linear Time Complexity, needs to check each item in the list to find what it is looking for (Loop through list) - O(n)
find = "Beef"

if find in my_list:
    print("You found the Beef!")

word = "chicken"

if word[2] == 'i':
    print("There is an i in the word")
    
    
#===================== Other List methods =======================

#.count() - counts how many times an item occurs in a list and returns the int - O(n)

def count(new_list, target):
    counter = 0
    for item in new_list:
        if item == target:
            counter += 1
    return counter

print(count(["Eggs", "Bacon", "Eggs", "Chicken", "Milk"], "Eggs"))

#.index() - returns the index of a target in a list - O(n)
# new_list.index(target)