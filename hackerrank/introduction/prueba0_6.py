def is_leap(year):
    leap = False
    # Verifying constraints
    if (year >= 1900 and year <= 10**5):
    	if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
    		leap = True
    
    return leap

if __name__ == '__main__':
	year = int(raw_input())
	print is_leap(year)