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

