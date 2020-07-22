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


# Inheritance
# A subclass inherits the attributes of its base class, but may override certain attributes, including certain methods.
# With inheritance, we only specify what is different between the subclass and the base class.
# Anything that we leave unspecified in the subclass is automatically assumed to behave just as it would for the base class.
# (The terms parent class and superclass are also used for the base class, while child class is also used for the subclass.)

class CheckingAccount(Account):
    """A bank account that charges for withdrawal."""
    withdraw_charge = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)


checking = CheckingAccount('Sam')
print('checking.deposit(10):', checking.deposit(10))
print('checking.withdraw(5):', checking.withdraw(5))
print('checking.interest:', checking.interest)


# To look up a name in a class.
#
# If it names an attribute in the class, return the attribute value.
# Otherwise, look up the name in the base class, if there is one.

# An object interface is a collection of attributes and conditions on those attributes.
def deposit_all(winners, amount=5):
    for account in winners:
        account.deposit(amount)


class SavingsAccount(Account):
    deposit_charge = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)


# multiple inheritance
# Method Resolution Order: Python resolves names from left to right, then upwards
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # A free dollar!


such_a_deal = AsSeenOnTVAccount('John')
print('such_a_deal.balance:', such_a_deal.balance)
print('such_a_deal.deposit(20):', such_a_deal.deposit(20))
print('such_a_deal.withdraw(5):', such_a_deal.withdraw(5))
print('such_a_deal.deposit_charge:', such_a_deal.deposit_charge)
print('such_a_deal.withdraw_charge:', such_a_deal.withdraw_charge)

print([c.__name__ for c in AsSeenOnTVAccount.mro()])  # Method Resolution Order


# Learning to identify when to introduce a new class, as opposed to a new function, in order to simplify
# or modularize a program, is an important design skill in software engineering that deserves careful attention.

class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1


bank = Bank()
john = bank.open_account('john', 10)
jack = bank.open_account('jack', 5, CheckingAccount)
print('john.interest:', john.interest)
print('jack.interest:', jack.interest)
bank.pay_interest()
print('john.balance:', john.balance)
print('bank.too_big_to_fail():', bank.too_big_to_fail())

# practice
class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    def f(self, x):
        return x

a = A()
b = B(1)
b.n = 5

print('C(2).n:', C(2).n)
print('a.z == C.z:', a.z == C.z)
print('a.z == b.z:', a.z == b.z)