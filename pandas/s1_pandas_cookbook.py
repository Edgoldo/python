import pandas as pd

registers = pd.read_csv("acrftreg.csv")

# Initialize a series (column data) in a variable
model = registers['Model']
model = registers.Model

# Get name of that series (column data)
print("Name of column data", model.name)

# Convert a column Series to column DataFrame
model_frame = model.to_frame()

# Get numbers of appears of each value in Series
num_model_values = model.value_counts()

# Count number of elements in Series with size, shape and len
num_model = model.size
num_model = model.shape
num_model = len(model)

# Count number of non-missing values in Series
num_model_non_miss = model.count()

# Basic statistics in Series with int64 data type
engnum = registers.engnum
engnum.min(), engnum.max(), engnum.mean(), engnum.median(), engnum.std(), engnum.sum()

# Get principal characteristics and statistics data with a single step
engnum.describe()

# Get an exact quantile of numeric data
engnum.quantile([.1,.2,.3,.4,.5,.6,.7,.8,.9])

# Get a Series of boolean with info of each individual value is missing or not
engnum.isnull()

# To replace all misssing values in a Series
suspenddate = registers.suspenddate
suspendate.count() # 17
suspendate.fillna('01 January 1000')
suspendate.count() # 15618

# To remove all missing values
suspendate.dropna()

# To check if Series has missing (nan) values
suspenddate.hasnans

# Get a Series of boolean with shows what elements are not missing by his position
suspenddate.notnull()

"""
	We can use operator like plus (+), minus (-), multiplication (*), division (/) and
	exponentiation (**), floor division (//) and modulus (%), to alter a Series.
"""
alter_engnum = engnum + 1 	# Add 1 to each element of Series
alter_engnum = engnum * 2.5 # Multiplies 2.5 to each element of Series
alter_engnum = engnum // 7	# Floor division with each elemenent of Series

"""
	And using greater than ( > ), less than ( < ), greater than or equal to ( >= ),
	less than or equal to ( <= ), equal to ( == ), and not equal to ( != ) over a Series
	can get a Series with the result of the operation.
"""
boolean_engnum = engnum > 7	# Compare each element of Series an return True or False
boolean_engnum = engnum == 0	# Verify if each element of Series is 0

""" 
	Pandas have methods equivalent ot each operator:
	Operator 		Group operator 				Series method name
	Arithmetic 		+, -, *, /, //, %, ** 		add, sub, mul, div, floordiv, mod, pow
	Comparison 		<, >, <=, >=, ==, != 		lt , gt , le , ge , eq , ne
"""
alter_engnum = engnum.add(1)
alter_engnum = engnum.mul(2.5)
alter_engnum = engnum.floordiv(7)
boolean_engnum = engnum.gt(7)
boolean_engnum = engnum.eq(0)

# We can chain Series methods
suspenddate.fillna('01 January 1000').astype('O').head()

# Setting column index
registers_2 = pd.read_csv("acrftreg.csv", index_col="Mark")

# Alternative way to set column index
registers_2 = registers.set_index('Mark')

# Set column index without erase column of DataFrame
registers_2 = registers.set_index('Mark', drop=False)

# Turn the index into a column. This method fails if the column in index exist in DataFrame
registers_2 = registers.set_index('Mark').reset_index()

# Change index and column names
index_rename = {'AAA': 'aaa', 'AAD': 'aad', 'AAE': 'aae'}
column_rename = {'Type': 'Tipo', 'Model': 'Modelo'}
registers_2 = registers_2.rename(index=index_rename, columns=column_rename)

"""
	Another way to change index and column name is using lists (must have the same 
	number of elements)
"""
reg2_inds = registers_2.index.tolist()
reg2_cols = registers_2.columns.tolist()

reg2_inds[0] = 'aaa'
reg2_inds[1] = 'aad'
reg2_inds[2] = 'Tipo'
reg2_inds[3] = 'Modelo'

registers_2.index = reg2_inds
registers_2.columns = reg2_cols

# Create a new column in DataFrame
registers_2['Status'] = 0

# Delete a column
registers_2 = registers_2.drop('Status', axis='columns')

# Alternatively
del registers_2['Status']

# Get index of column
registers.columns.get_loc('suspenddate')

# Insert column in indicated index
registers.insert(42, column="suspendmotive", value="Wether")