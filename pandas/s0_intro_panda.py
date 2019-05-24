import pandas as pd

registers = pd.read_csv('acrftreg.csv')

# Get the first 5 registers in file
first_5 = registers.head(5)

# Show the type of register is a pandas DataFrame
print("Type of element: ", type(first_5))

# Get the last 10 registers in file
last_10 = registers.tail(10)
last = registers.tail(1)
print(last)
# Get the keys (columns names) of registers
columns_name = registers.keys()
print(columns_name)

# Get the first 6 registers in column 2
column_2 = registers[registers.keys()[1]].head(6)

# Show the type element of column is Series
print("Type of element: ", type(column_2))

# Get all datatypes of each column in file
data_types = registers.dtypes

# Get row by number or by id, where [row, column], accept :
row_1 = registers.loc[1]

# Similar to last command. Get row by number or by id, where [row, column], accept :
#row_1 = registers.iloc[1]

# To convert any column data type in date, can use parse_date while read csv file,
# passing the columns names by a list. If the column is not a date format then fails
registers_2 = pd.read_csv("acrftreg.csv", parse_dates=['regopCommdate', 'Datefirstreg'])

# Get number of columns an rows
col_rows_number = registers.shape

# Number of rows can be getted with size too
#rows_number = register.size

# Info of total rows in each column with total number and total of non-null objects
register_info = register.info()

# To get total memory usage with info function, can use the parammeter memory_usage="deep"
register_info = register.info(memory_usage="deep")