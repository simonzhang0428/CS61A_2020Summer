lst = [6, 1, 'a']
# TypeError: 'list' object is not an iterator
# print('next(lst):', next(lst))

lst_iter = iter(lst)
print('next(lst_iter):', next(lst_iter))
print('next(lst_iter):', next(lst_iter))
print('next(iter(lst)):', next(iter(lst)))
print('[x for x in lst_iter]:', [x for x in lst_iter])


def gen_naturals():
    current = 0
    while True:
        yield current
        current += 1


gen = gen_naturals()
print('next(gen):', next(gen))
print('next(gen):', next(gen))


# def generate_subsets():
#     """Return all subsets from 1 to n."""
#     pass
#
#
# subsets = generate_subsets()
# for _ in range(3):
#     print(next(subsets))


# [[]]
# [[], [1]]
# [[], [1], [2], [1, 2]]

# • class: a template for creating objects
# • instance: a single object created from a class
# • instance attribute: a property of an object, specific to an instance
# • class attribute: a property of an object, shared by all instances of a class
# • method: an action (function) that all instances of a class may perform
class Student:
    students = 0

    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        Student.students += 1
        print('There are now', Student.students, 'students')
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print('Thanks, ' + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


# what would Python display:
# callahan = Professor('Callahan')
# elle = Student('Elle', callahan)
# elle.visit_office_hours(callahan)
# elle.visit_office_hours(Professor("Paulette"))
# elle.understanding
# [name for name in callahan.students]
# x = Student("Vivian", Professor("Stromwell")).name
# x
# [name for name in callahan.students]

class Email:
    """Every email object has 3 instance attributes: the message,
    the sender name, and recipient name.
    """

    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associated client names with client objects.
    """

    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        client = self.clients[email.recipient_name]
        client.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them to
        the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is used for
    addressing emails to the client), server (which is used to send emails
    out to other clients), and inbox (a list of all emails the client has received).
    """

    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        self.inbox.append(email)


# Inheritance
class Pet():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.is_alive = True

    def eat(self, thing):
        print(self.name + ' ate a ' + str(thing) + '!')

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        print(self.name + ' says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive' becomes
        False. If this is called after lives has reached zero, print out that
        the cat has no more lives to lose.
        """
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print('the cat has no more lives to lose.')


class NoisyCat(Cat):
    def talk(self):
        """Talks twice as much as a regylar cat."""
        Cat.talk(self)
        Cat.talk(self)


# what would Python display:
class A:
    def f(self):
        return 2

    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)


class B(A):
    def f(self):
        return 4


# x, y = A(), B()
# x.f()
# x.g(x, 1)
# y.g(x, 2)
