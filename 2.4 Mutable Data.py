from datetime import date

saturday = date(2020, 7, 11)
print('today ->', saturday)
print('date(2020, 7, 30) - saturday ->', date(2020, 7, 30) - saturday)
print('saturday.year ->', saturday.year)
print(saturday.strftime('%A, %B %d'))  # %A means that the day of the week should be spelled out in full

print('\'1234\'.isnumeric() ->', '1234'.isnumeric())
print('\'rOBERT dE nIRO\'.swapcase() ->', 'rOBERT dE nIRO'.swapcase())
print("'eyes'.upper().endswith('YES') ->", 'eyes'.upper().endswith('YES'))

chinese = ['coin', 'string', 'myriad']  # A list literal
suits = chinese  # Two names refer to the same list
print('suits:', suits)
print('suits.pop():', suits.pop())  # Remove and return the final element
suits.remove('string')  # Remove the first element that equals the argument
suits.append('cup')  # Add an element to the end
suits.extend(['sword', 'club'])  # Add all elements of a sequence to the end
suits[2] = 'spade'  # Replace an element
print('suits:', suits)
suits[0:2] = ['heart', 'diamond']  # Replace a slice
print('suits:', suits)

# Methods also exist for inserting, sorting, and reversing lists.
# All of these mutation operations change the value of the list;
# they do not create new list objects.
print('chinese:', chinese)
nest = list(suits)
nest[0] = suits
suits.insert(2, 'Joker')  # Insert an element at index 2, shifting the rest
print('nest:', nest)
print('nest[0].pop(2):', nest[0].pop(2))

# is and is not, test whether two expressions in fact evaluate to the identical object.
# Two objects are identical if they are equal in their current value,
# and any change to one will always be reflected in the other.
# Identity is a stronger condition than equality.
print('suits is nest[0]:', suits is nest[0])
print("suits is ['heart', 'diamond', 'spade', 'club']:", suits is ['heart', 'diamond', 'spade', 'club'])
print("suits == ['heart', 'diamond', 'spade', 'club']:", suits == ['heart', 'diamond', 'spade', 'club'])

# The append method of a list takes one value as an argument and adds it to the end of the list. The argument can be
# any value, such as a number or another list. If the argument is a list, then that list (and not a copy) is added as
# an item in the list. The method always returns None, and it mutates the list by increasing its length by one.

# The extend method of a list takes an iterable value as an argument and adds each of its elements to the end of the
# list. It mutates the list by increasing its length by the length of the iterable argument. The statement x += y for
# a list x and iterable y is equivalent to x.extend(y), aside from some obscure and minor differences beyond the
# scope of this text. Passing any argument to extend that is not iterable will cause a TypeError. The method does not
# return anything, and it mutates the list.

# The pop method removes and returns the last element of the list. When given an integer argument i, it removes and
# returns the element at index i of the list. This method mutates the list, reducing its length by one. Attempting to
# pop from an empty list causes an IndexError.

# The remove method takes one argument that must be equal to a value in the list. It removes the first item in the
# list that is equal to its argument. Calling remove on a value that is not equal to any item in the list causes a
# ValueError.

# The index method takes one argument that must be equal to a value in the list.
# It returns the index in the list of the first item that is equal to the argument.
# Calling index on a value that is not equal to any item in the list causes a ValueError.
a = [13, 14, 13, 12, [13, 14], 15]
print('a:', a)
print('a.index([13, 14]):', a.index([13, 14]))
print('a.index(13):', a.index(13))

# The insert method takes two arguments: an index and a value to be inserted. The value is added to the list at the
# given index. All elements before the given index stay the same, but all elements after the index have their indices
# increased by one. This method mutates the list by increasing its size by one, then returns None.

# The count method of a list takes in an item as an argument and returns how many times an equal item appears in the
# list. If the argument is not equal to any element of the list, then count returns 0.
a = [1, [2, 3], 1, [4, 5]]
print('a:', a)
print('a.count([2, 3]):', a.count([2, 3]))
print('a.count(1):', a.count(1))
print('a.count(5):', a.count(5))

from unicodedata import lookup

# A list comprehension always creates a new list.
# the unicodedata module tracks the official names of every character in the Unicode alphabet.
# We can look up the characters corresponding to names, including those for card suits.
print([lookup('WHITE ' + s.upper() + ' SUIT') for s in suits])

