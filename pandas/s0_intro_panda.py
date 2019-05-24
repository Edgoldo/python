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