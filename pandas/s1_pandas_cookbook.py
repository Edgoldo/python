import pandas as pd

registers = pd.read_csv("acrftreg.csv")

# Initialize a series (column data) in a variable
model = registers['Model']
model = registers.Model

# Get name of that series (column data)
print("Name of column data", model.name)

# Convert a column Series to column DataFrame
model_frame = model.to_frame()

