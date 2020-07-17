from datetime import date

saturday = date(2020, 7, 11)
print('today ->', saturday)
print('date(2020, 7, 30) - saturday ->', date(2020, 7, 30) - saturday)
print('saturday.year ->', saturday.year)
print(saturday.strftime('%A, %B %d'))  # %A means that the day of the week should be spelled out in full

# string
s = 'Hello'
print('s.upper():', s.upper())
a = 'a'
print('ord(a):', ord(a))
print('hex(ord(a)):', hex(ord(a)))
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

# is and is not, test whether two expressions in fact evaluate to the same object.
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
print(lookup('SNOWMAN'))
print(lookup('white smiling face'))
print(lookup('baby'))
print(lookup('BABY'))
print(lookup('baby').encode())
print(lookup('girl'))

# Tuples
a = 1, 2 + 3
print('a:', a)
b = ('the', 1, ('and', 'only'))
print('b', b)
print('type(())', type(()))
print('type((10))', type((10)))
print('type((10,))', type((10,)))

code = ("up", "up", "down", "down") + ("left", "right") * 2
print('code:', code)
print('len(code):', len(code))
print('code.count(\'down\'):', code.count('down'))
print('code.index(\'left\'):', code.index('left'))

# Dictionaries
# The purpose of a dictionary is to provide an abstraction for storing and retrieving values
# that are indexed not by consecutive integers, but by descriptive keys.

# Strings commonly serve as keys, because strings are our conventional representation for names of things.
# This dictionary literal gives the values of various Roman numerals.
numerals = {'I': 1.0, 'V': 5, 'X': 10}
print('numerals:', numerals)
print('numerals[\'V\']:', numerals['V'])
numerals['I'] = 1
numerals['L'] = 50
print('numerals:', numerals)  # Since Python 3.6, their contents will be ordered by insertion.
print('sum(numerals.values()):', sum(numerals.values()))
print('numerals.keys():', numerals.keys())
print('numerals.values()', numerals.values())
print('numerals.items():', numerals.items())
dogs = dict([('dudu', 3), ('penny', 6)])  # list convert to dictionary
print('dogs:', dogs)

# Dictionaries do have some restrictions:
#
# A key of a dictionary cannot be or contain a mutable value.
# There can be at most one value for a given key.

# get, which returns either the value for a key, if the key is present, or a default value.
print('numerals.get(\'A\', 0):', numerals.get('A', 0))
print('numerals.get(\'X\', 0):', numerals.get('X', 0))

d = {x: x * x for x in range(3, 6)}
print(d)


# Ever since we first encountered nested def statements, we have observed that a locally defined function can look up
# names outside of its local frames. No nonlocal statement is required to access a non-local name. By contrast,
# only after a nonlocal statement can a function change the binding of names in these frames.

# The key to correctly analyzing code with non-local assignment is to remember that only function calls can introduce
# new frames. Assignment statements always change bindings in existing frames.

# Some important things to keep in mind when using nonlocal:
#   nonlocal cannot be used with global variables (names defined in the global frame).
#   If no nonlocal variable is found with the given name, a SyntaxError is raised.
#   A name that is already local to a frame cannot be declared as nonlocal.

def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds.'
        balance = balance - amount
        return balance

    return withdraw


withdraw = make_withdraw(100)
print(withdraw(25))


def make_withdraw_list(balance):
    b = [balance]

    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds.'
        b[0] = b[0] - amount
        return b[0]

    return withdraw


withdraw = make_withdraw_list(100)
print(withdraw(25))


def f(x):
    x = 4

    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z

        return h

    return g


a = f(1)
b = a(2)
total = b(3) + b(4)


# An expression that contains only pure function calls is referentially transparent;
# its value does not change if we substitute one of its subexpression with the value of that subexpression.

def oski(bear):
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk + 1, berk - 1]
        bear = lambda ley: berk - ley
        return [berk, cal(berk)]

    return cal(2)


print(oski(abs))

# iterator, position in container
primes = [2, 3, 5, 7]
print('prime:', primes)
print('type(primes):', type(primes))
iterator = iter(primes)
print('type(iterator):', type(iterator))
print('next(iterator):', next(iterator))
print('next(iterator):', next(iterator))
print('next(iterator):', next(iterator))
print('next(iterator):', next(iterator))
# print('next(iterator):', next(iterator))  # raising a StopIteration exception

# Two separate iterators can track two different positions in the same sequence.
# However, two names for the same iterator will share a position
# because they share the same value.
r = range(3, 13)
s = iter(r)
print('next(s):', next(s))
print('next(s):', next(s))
t = iter(r)
print('next(t):', next(t))
print('next(t):', next(t))
u = t  # another name for iterator t
print('next(u):', next(u))
print('next(u):', next(u))
print('next(s):', next(s))
print('next(t):', next(t))

d = {'one': 1, 'two': 2, 'three': 3}
k = iter(d)
print('next(k)', next(k))
print('next(k)', next(k))
print('next(k)', next(k))
v = iter(d.values())
print('next(v)', next(v))
print('next(v)', next(v))
print('next(v)', next(v))
d.pop('two')
# RuntimeError: dictionary changed size during iteration
# print('next(k)', next(k))

r = range(3, 6)
s = iter(r)
print('next(s)', next(s))
for x in s:
    print(x)
print('list(s)', list(s))
for x in r:
    print(x)


def double_and_print(x):
    print('***', x, '=>', 2 * x, '***')
    return 2 * x


s = range(3, 6)
doubled = map(double_and_print, s)
a = next(doubled)
print(a)
a = next(doubled)
print(a)
lst = list(doubled)  # what left in a list
print(lst)

# The filter function returns an iterator over a subset of the values in another iterable.
# The zip function returns an iterator over tuples of values that combine one value from each of multiple iterables.

letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


filteredVowels = filter(filterVowels, letters_list)
print(next(filteredVowels))
print(next(filteredVowels))
print(next(filteredVowels))
print(next(filteredVowels))

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)  # empty


# Generator
# When called, a generator function doesn't return a particular yielded value,
# but instead a generator (which is a type of iterator) that itself can return the yielded values.
# Calling next on the generator continues execution of the generator function from wherever it left off previously
# until another yield statement is executed.

#  yield statements do not destroy the newly created environment; they preserve it for later.
#  When next is called again, execution resumes where it left off.
def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current) + 1)


for letter in letters_generator():
    print(letter)

letters = letters_generator()
print('type(letter)', type(letters))
print('next(letters)', next(letters))
print('next(letters)', next(letters))
print('next(letters)', next(letters))
print('next(letters)', next(letters))

# Linked List
empty = 'empty'


# the function is a dispatch function and its arguments are first a message, followed by additional arguments to
# parameterize that method. This message is a string naming what the function should do. Dispatch functions are
# effectively many functions in one: the message determines the behavior of the function, and the additional
# arguments are used in that behavior.

# encapsulates the logic for all operations on a data value within one function that responds to different messages,
# is a discipline called message passing. A program that uses message passing defines dispatch functions,
# each of which may have local state, and organizes computation by passing "messages" as the first argument to those
# functions. The messages are strings that correspond to particular behaviors.

# def mutable_link():
#     """Return a functional implementation of a mutable linked list."""
#     contents = empty
#     def dispatch(message, value=None):
#         nonlocal contents
#         if message == 'len':
#             return len_link(contents)
#         elif message == 'getitem':
#             return getitem_link(contents, value)
#         elif message == 'push_first':
#             contents = link(value, contents)
#         elif message == 'pop_first':
#             f = first(contents)
#             contents = rest(contents)
#             return f
#         elif message == 'str':
#             return join_link(contents, ", ")
#     return dispatch

def dictionary():
    """Return a functional implementation of a dictionary."""
    records = []

    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value

    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)

    return dispatch


d = dictionary()
d('setitem', 3, 9)
d('setitem', 4, 16)
print('d(\'getitem\', 3):', d('getitem', 3))
print('d(\'getitem\', 4):', d('getitem', 4))
print('d(\'getitem\', 0):', d('getitem', 0))


def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']

    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']

    dispatch = {'deposit': deposit,
                'withdraw': withdraw,
                'balance': initial_balance}
    return dispatch


def withdraw(account, amount):
    return account['withdraw'](amount)


def deposit(account, amount):
    return account['deposit'](amount)


def check_balance(account):
    return account['balance']


a = account(20)
deposit(a, 5)
withdraw(a, 17)
check_balance(a)


# Expressing programs as constraints is a type of declarative programming, in which a programmer declares the
# structure of a problem to be solved, but abstracts away the details of exactly how the solution to the problem is
# computed.

# Constraints and connectors are both abstractions that are manipulated through messages. When the value of a
# connector is changed, it is changed via a message that not only changes the value, but validates it (checking the
# source) and propagates its effects (informing other constraints).

# generator pause when reach yield
def evens(start, end):
    even = start + start % 2
    while even < end:
        yield even
        even += 2


t = evens(1, 10)
print('type(t)', type(t))
print('next(t)', next(t))
print('next(t)', next(t))
print('next(t)', next(t))
print('next(t)', next(t))
print('list(evens(1, 10))', list(evens(1, 10)))


def countdown(k):
    if k > 0:
        yield k
        # for x in countdown(k-1):
        #     yield x
        yield from countdown(k - 1)  # shorthand for go through iterator
    else:
        yield 'END!'


t = countdown(3)
print('next(t)', next(t))
print('next(t)', next(t))
print('next(t)', next(t))
print('next(t)', next(t))


def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s


print('list(prefixes(\'both\'))', list(prefixes('both')))


def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])


print('list(substrings(\'tops\'))', list(substrings('tops')))
