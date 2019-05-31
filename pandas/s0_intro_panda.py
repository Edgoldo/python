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

# Get row by id, where [row, column], accept :
registers_2 = registers.set_index('Mark')
row_1 = registers_2.loc['AAA']

# Get row by number where [row, column], accept :
row_1 = registers_2.iloc[0]

# To convert any column data type in date, can use parse_date while read csv file,
# passing the columns names by a list. If the column is not a date format then fails
registers_2 = pd.read_csv("acrftreg.csv", parse_dates=['regopCommdate', 'Datefirstreg'])

# Get number of columns an rows
col_rows_number = registers.shape

# Another way to get number of rows
rows_number = len(registers)

# Number of rows times number of columns can be getted with size. Is total of cells in file
cells_number = registers.size

# Info of total rows in each column with total number and total of non-null objects
register_info = registers.info()

# To get total memory usage with info function, can use the parammeter memory_usage="deep"
register_info = registers.info(memory_usage="deep")

# Setting index by specific column. Set column 0 index
registers_3 = pd.read_csv("acrftreg.csv", index_col=0)

# Get index (Index object)
registers_3_index = registers_3.index

# Access to element by index position
print("Fift element of register_3_index: ", registers_3_index[5])

# Access to element by slice index of numbers
print("Elements from index 3 to 10: ", registers_3_index[3:10])

# Access to element by slice index of numbers position
print("Elements by index 4, 10 and -2: ", registers_3_index[[4, 10, -2]])

# Get columns (Index object)
registers_3_columns = registers_3.columns

# Get values (Array object)
registers_3_values = registers_3.values

# Access to values by column name
col_model = registers_3['Model']

# To set an index to DataFrame of data in a new variable
registers_4 = registers_3.set_index('Model')

# Get options of pd module. Number of maximum columns to show
pd.get_option('display.max_columns')

# Set options of pd module. Change number of maximum columns
pd.set_option('display.max_columns', 10)

# Restart one or all options of pd module
pd.reset_option('display.max_columns')

# Selecting a list of columns from DataFrame. The order of columns is no matters
columns_list = ['Mark', 'Type']
registers[columns_list]

# Getting rows and columns with loc
"""
	registers_3.index
	Index(['AAA', 'AAB', 'AAD', 'AAE', 'AAF', 'AAG', 'AAH', 'AAI', 'AAJ', 'AAK',
           ...
           'ZZQ', 'ZZR', 'ZZS', 'ZZT', 'ZZU', 'ZZV', 'ZZW', 'ZZX', 'ZZY', 'ZZZ'],
           dtype='object', name='Mark', length=15618)

    registers_3.columns
    Index(['Manu', 'Type', 'Model', 'Serial', 'MTOW', 'engnum', 'Engmanu',
       'Engtype', 'Engmodel', 'Fueltype', 'regType', 'regholdname',
       'regholdadd1', 'regholdadd2', 'regholdSuburb', 'regholdState',
       'regholdPostcode', 'regholdCountry', 'regholdCommdate', 'regopName',
       'regopadd1', 'regopadd2', 'regopSuburb', 'regopState', 'regopPostcode',
       'regopCountry', 'regopCommdate', 'Datefirstreg', 'gear', 'Airframe',
       'CoAcata', 'CoAcatb', 'CoAcatc', 'Propmanu', 'Propmodel', 'Typecert',
       'Countrymanu', 'Yearmanu', 'Regexpirydate', 'suspendstatus',
       'suspenddate', 'ICAOtypedesig', 'IDERA_Authorised_Party',
       'IDERA_Certified_Designee'],
      dtype='object')
"""
data_rows = ['AAA', 'BBB', 'CCC']
data_cols = ['Type', 'Model', 'Airframe']
# Can use one or more elements in data_rows or data_cols lists
data_result = registers_3.loc[data_rows, data_cols]

# Can specific rows slice or column slice. To select all of that, can use :
data_result = registers_3.loc['AAA':'AAZ', 'Manu':'Model']

# Can get data distanced by n spaces
data_result = registers_3.loc['AAA':'AAZ':4]

# Gettings data with iloc
data_rows = [0, 2, 3, 4, 5]
data_cols = [2, 3, -4, 7, 10, -11]

# Can use one or more elements in data_rows or data_cols lists
data_result = registers_3.iloc[data_rows, data_cols]

# Can specific rows slice or column slice. To select all of that, can use : 
# In this case not include the last element indicated
data_result = registers_3.iloc[3:15, 10:14]

# Can get data distanced by n spaces
data_result = registers_3.iloc[1:100:4]

# A way to filter data is using a Series of boolean values
engnum = registers_3['engnum'] # Series of numbers (int64), with a total of 15618 elements
# Geting a Series of booleans where value is True if engnum in that position is greater than 1
index_gte_1 = engnum > 1
# Filtering data of values greater than 1
data_result = engnum[index_gte_1]