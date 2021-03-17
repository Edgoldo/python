## https://datawhatnow.com/things-you-are-probably-not-using-in-python-3-but-should/
"""
    f-strings (3.6+)

    It is difficult to do anything without strings in any programming language and in order to stay sane, you want to have a structured way to work with strings. Most people using Python prefer using the format method.
"""
user = "Jane Doe"
action = "buy"
log_message = 'User {} has logged in and did an action {}.'.format(
  user,
  action
)
print(log_message)
# User Jane Doe has logged in and did an action buy.

"""
    Alongside of format, Python 3 offers a flexible way to do string interpolation via f-strings. The same code as above using f-strings looks like this:
"""
user = "Jane Doe"
action = "buy"
log_message = f'User {user} has logged in and did an action {action}.'
print(log_message)
# User Jane Doe has logged in and did an action buy.

"""
Pathlib (3.4+)

f-strings are amazing, but some strings like file paths have their own libraries which make their manipulation even easier. Python 3 offers pathlib as a convenient abstraction for working with file paths. If you are not sure why you should be using pathlib, try reading this excellent post – Why you should be using pathlib – by Trey Hunner.
"""
from pathlib import Path
root = Path('post_sub_folder')
print(root)
# post_sub_folder
path = root / 'happy_user'
# Make the path absolute
print(path.resolve())
# /home/weenkus/Workspace/Projects/DataWhatNow-Codes/how_your_python3_should_look_like/post_sub_folder/happy_user

"""
Type hinting (3.5+)

Static vs dynamic typing is a spicy topic in software engineering and almost everyone has an opinion on it. I will let the reader decide when they should write types, but I think you should at least know that Python 3 supports type hints.
"""
def sentence_has_animal(sentence: str) -> bool:
  return "animal" in sentence
sentence_has_animal("Donald had a farm without animals")
# True

"""
Enumerations (3.4+)

Python 3 supports an easy way to write enumerations through the Enum class. Enums are a convenient way to encapsulate lists of constants so they are not randomly located all over your code without much structure.
"""
from enum import Enum, auto
class Monster(Enum):
    ZOMBIE = auto()
    WARRIOR = auto()
    BEAR = auto()
    
print(Monster.ZOMBIE)
# Monster.ZOMBIE

"""
    An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
    https://docs.python.org/3/library/enum.html
"""
for monster in Monster:
    print(monster)
# Monster.ZOMBIE
# Monster.WARRIOR
# Monster.BEAR

"""
Built-in LRU cache (3.2+)

Caches are present in almost any horizontal slice of the software and hardware we use today. Python 3 makes using them very simple by exposing an LRU (Least Recently Used) cache as a decorator called lru_cache.

Below is a simple Fibonacci function that we know will benefit from caching because it does the same work multiple times through a recursion.
"""
import time
def fib(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1
    
    return fib(number-1) + fib(number-2)
start = time.time()
fib(40)
print(f'Duration: {time.time() - start}s')
# Duration: 30.684099674224854s

"""
Now we can use the lru_cache to optimize it (this optimization technique is called memoization). The execution time goes down from seconds to nanoseconds.
"""
from functools import lru_cache
@lru_cache(maxsize=512)
def fib_memoization(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1
    
    return fib_memoization(number-1) + fib_memoization(number-2)
start = time.time()
fib_memoization(40)
print(f'Duration: {time.time() - start}s')
# Duration: 6.866455078125e-05s

"""
Extended iterable unpacking (3.0+)

I will let the code speak here (docs).
"""
head, *body, tail = range(5)
print(head, body, tail)
# 0 [1, 2, 3] 4
py, filename, *cmds = "python3.7 script.py -n 5 -l 15".split()
print(py)
print(filename)
print(cmds)
# python3.7
# script.py
# ['-n', '5', '-l', '15']
first, _, third, *_ = range(10)
print(first, third)
# 0 2

"""
Data classes (3.7+)

Python 3 introduces data classes which do not have many restrictions and can be used to reduce boilerplate code because the decorator auto-generates special methods, such as __init__() and __repr()__. From the official proposal, they are described as “mutable named tuples with defaults”.
"""
class Armor:
    
    def __init__(self, armor: float, description: str, level: int = 1):
        self.armor = armor
        self.level = level
        self.description = description
                 
    def power(self) -> float:
        return self.armor * self.level
    
armor = Armor(5.2, "Common armor.", 2)
armor.power()
# 10.4
print(armor)
# <__main__.Armor object at 0x7fc4800e2cf8>

"""
The same implementation of Armor using data classes.
"""
from dataclasses import dataclass
@dataclass
class Armor:
    armor: float
    description: str
    level: int = 1
    
    def power(self) -> float:
        return self.armor * self.level
    
armor = Armor(5.2, "Common armor.", 2)
armor.power()
# 10.4
print(armor)
# Armor(armor=5.2, description='Common armor.', level=2)

"""
Implicit namespace packages (3.3+)

One way to structure Python code is in packages (folders with an __init__.py file). The example below is given by the official Python documentation.

    sound/                          Top-level package
          __init__.py               Initialize the sound package
          formats/                  Subpackage for file format conversions
                  __init__.py
                  wavread.py
                  wavwrite.py
                  aiffread.py
                  aiffwrite.py
                  auread.py
                  auwrite.py
                  ...
          effects/                  Subpackage for sound effects
                  __init__.py
                  echo.py
                  surround.py
                  reverse.py
                  ...
          filters/                  Subpackage for filters
                  __init__.py
                  equalizer.py
                  vocoder.py
                  karaoke.py
                  ...

In Python 2, every folder above had to have an __init__.py file which turned that folder into a Python package. In Python 3, with the introduction of Implicit Namespace Packages, these files are no longer required.

    sound/                          Top-level package
          __init__.py               Initialize the sound package
          formats/                  Subpackage for file format conversions
                  wavread.py
                  wavwrite.py
                  aiffread.py
                  aiffwrite.py
                  auread.py
                  auwrite.py
                  ...
          effects/                  Subpackage for sound effects
                  echo.py
                  surround.py
                  reverse.py
                  ...
          filters/                  Subpackage for filters
                  equalizer.py
                  vocoder.py
                  karaoke.py
                  ...

EDIT: as some people have said, this is not as simple as I pointed it out in this section, from the official PEP 420 Specification – __init__.py is still required for regular packages, dropping it from the folder structure will turn it into a native namespace package which comes with additional restrictions, the official docs on native namespace packages show a great example of this, as well as naming all the restrictions.
"""