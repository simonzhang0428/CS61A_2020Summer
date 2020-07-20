# A class serves as a template for all objects whose type is that class.
# Every object is an instance of some particular class.

# An attribute of an object is a name-value pair associated with the object, which is accessible via dot notation.
# The attributes specific to a particular object, as opposed to all objects of a class, are called instance
# attributes. Instance attributes may also be called fields, properties, or instance variables.

# Functions that operate on the object or perform object-specific computations are called methods.


class Account:
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance -= amount
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


a = Account('Simon')
print('a.balance', a.balance)
print('a.holder', a.holder)

b = Account('Helen')
b.balance = 200
print([acc.balance for acc in (a, b)])

print('a is b', a is b)
c = a
print('c is a', c is a)

print('a.deposit(100):', a.deposit(100))
print('a.withdraw(90):', a.withdraw(90))
print('a.withdraw(90):', a.withdraw(90))

# The central idea in message passing was that data values should have behavior by responding to messages that are
# relevant to the abstract type they represent. Dot notation is a syntactic feature of Python that formalizes the
# message passing metaphor.

# The attributes of an object include all of its instance attributes, along with all of the attributes
# (including methods) defined in its class.
# Methods are attributes of the class that require special handling.
print('getattr(a, \'balance\'):', getattr(a, 'balance'))
print('hasattr(a, \'deposit\'):', hasattr(a, 'deposit'))

print('type(Account.deposit):', type(Account.deposit))
print('type(a.deposit):', type(a.deposit))

# We can call deposit in two ways: as a function and as a bound method.
# In the former case, we must supply an argument for the self parameter explicitly.
# In the latter case, the self parameter is bound automatically.
print('Account.deposit(a, 1001):', Account.deposit(a, 1001))
print('a.deposit(1000):', a.deposit(1000))

print('getattr(Account, \'deposit\'):', getattr(Account, 'deposit'))

# Python's convention dictates that if an attribute name starts with an underscore, it should only be accessed
# within methods of the class itself, rather than by users of the class.

# <expression> . <name>
# To evaluate a dot expression:
#
# Evaluate the <expression> to the left of the dot, which yields the object of the dot expression.
# <name> is matched against the instance attributes of that object; if an attribute with that name exists, its value is returned.
# If <name> does not appear among instance attributes, then <name> is looked up in the class, which yields a class attribute value.
# That value is returned unless it is a function, in which case a bound method is returned instead.
a.interest = 0.5
print('a.interest:', a.interest)
print('Account.interest:', Account.interest)

Account.interest = 1.0
print('Account.interest:', Account.interest)
print('a.interest:', a.interest)
print('b.interest:', b.interest)