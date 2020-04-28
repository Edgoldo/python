Coding for Entrepreneurs - 30-Days-of-Python 
============================================

Tutorial with some useful commands and examples of how strings and string functions works in Python. See more in https://github.com/codingforentrepreneurs/30-Days-of-Python

Day 6 - String Formatting & F-Strings
-------------------------------------

Python has ways to make writing text a bit more programmic and helps systematically remove repeating youself.

Also, check out:

    pyformat
    strftime.org

String Formatting

Basic formatting:

#: Write a comment # this is a comment

\n: New Line

\t: Tab

\\ or //: Allowed Slash

\': Allowed Single Quote

\": Allowed Double quote

{{ or }}: Allowed signle curly bracket in formatted strings

"your single-line text": Wrap a single quote (') or double quote (") around text / numbers to make it a string.

\: A slash in front of a return/enter will escape that. Allowing for multi-line strings without the triple quotes. Such as:

"this is my string example\
when I close it here"

""" your multi-line text""": Wrap 3x single quotes (```) or 3x double quotes (") around a lot of text to allow for multi-line strings. Such as:

"""this is my string example
when I close it here"""

The .format() method

Empty

"{} {}".format("Hello", "World")

Positional

"{0} {1} {0}".format("Hello", "World")

Keyword

"{first} {second} {first}".format(first="Hello", second="World")

Positional & Keyword

"{0} {second} {0}".format("Hello", second="World")

"{0} {1} {2['hello']}".format("Hello", "World", {'hello': 'sup'})

Unpacking a Dictionary

data = {'name': 'Hodor', 'email': 'holdthe@door.com'}
txt = 'Name: {name}\nEmail: {email}'.format(**data)
print(txt)

Numbers, Floats & Decimals

Number / Integer

"{:d}".format(32)

or

"{}".format(32)

Float / Decimal

"{:f}".format(32)

pi = 3.14159265359
"{:f}".format(pi)

Limit to n decimal places. Replace 4 below with the number of decimal places to round to.

pi = 3.14159265359
"{:.4f}".format(pi)

The % method

Positional - Strings or Numbers

"%s %s %s %s" % ("Hello", 12, 131.312, {'hello': 'sup'})

Keyword / Dictionary

"%(first)s %(second)s" % {"first":"Hello", "second":"World"}

Keywords (Also known as named placeholders)

data = {'name': 'Hodor', 'email': 'holdthe@door.com'}
txt = 'Name: %(name)s\nEmail: %(email)s' % data
print(txt)

Numbers, Floats & Decimals

Number

"%d" % (32)

or

"%s" % (32)

Float

"%f" % (32)

pi = 3.14159265359
"%f" % (pi)

Limit to n decimal places. Replace 2 below with the number of decimal places to round to.

pi = 3.14159265359
"%.2f" % (pi)

f Strings (aka f-string)

Strings or Number variables

first = "Hello"
second = "World"
third = 32.3122
fourth = "{:.2f}".format(third)
f"{first} {second} {first.upper()} {third} {fourth}"

Dictionary

data = {'name': 'Hodor', 'email': 'holdthe@door.com'}
txt = f'Name: {data["name"]}\nEmail: {data["email"]}'
print(txt)

Inline Math

hours = 21
seconds = 32
f"{hours} {seconds * 10} {seconds}"

Inline Formatting

pi = 3.14159265359
f"{format(pi, '.2f')}"