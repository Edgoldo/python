"""
Basic tests, implementation of several builded functions of Python
and free coding 
"""
print("Principal Program")
num1 = 3
num2 = 5
sum = num1+num2
print(sum)
print("hello")

# Implement for repeat
print("For repeat: ")
for i in range(1, 11):
	print(i)
	if i == 5:
		break

# Making a basic function and use of quotation marks to get
# a docstring using double.__doc__
def double(num):
	"""
    Function to get the double of a number

    @date 
    @param <b>{integer}</b> num Number used to get his double value
    @return <b>{integer}</b> Double of the param num
    """
	return 2*num
# Print the docstring of double function
print(double.__doc__)

# Testing type 
print("Testing data types: ")
a = 5
print(a, " is type: ", type(a))
a = 2.3
print(a, " is type: ", type(a))
a = 1+2j
print(a, " is a complex number?", isinstance(a,complex))

# Testing hex, oct, bin numbers
print("Conversion test 1: ")
# Output: 107
print(0b1101011)
# Output: 253 (251 + 2)
print(0xFB + 0b10)
# Output: 13
print(0o15)
# Data conversion
sum = 2 + 3.1

# Conversion functions:
print("Conversion test 2: ")
print(int(2.3))
print(int(-5.7))
print(float(12))
print(complex('3+5j'))

# Testing tuples
tup = (("One", ("First value")), ("Two", ("Second value")))
print('Tuple: ', tup)
dic = dict(tup)
print('Dictionary data: ', list(dic.values()))
