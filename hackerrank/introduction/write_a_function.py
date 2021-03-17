"""
Every year that is exactly divisible by four es a leap year, 
except for years that are exactly divisible by 100, but these
centurial years are leap years if they are exactly divisible by
400.
The input are the value of the year to evaluate
The output is True if that input is leap year or False in oposite case
"""
def is_leap(year):
    leap = False
    # Verifying constraints
    if (year >= 1900 and year <= 10**5):
    	if (year % 4 == 0) and (year % 100 != 0):
    		leap = True
    	if  (year % 100 == 0) and (year % 400 == 0):
    		leap = True
    
    return leap

if __name__ == '__main__':
	year = int(raw_input())
	print is_leap(year)