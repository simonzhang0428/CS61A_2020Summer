# 06/23/2020

# uniform resource locator (URL), a location of something on the Internet.

# Programming is about a person using their real insight to build something useful,
# constructed out of these teeny, simple little operations that the computer can do.

# Incremental testing, modular design, precise assumptions, and teamwork
# are themes that persist throughout this text.


from urllib.request import urlopen

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

words = set(shakespeare.read().decode().split())

spellReverse = {w for w in words if len(w) == 6 and w[::-1] in words}
print(spellReverse)

"""
{'diaper', 'drawer', 'repaid', 'reward', 'redder'}
"""