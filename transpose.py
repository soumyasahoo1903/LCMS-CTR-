import pandas as pd

# Read the Excel file
df = pd.read_excel(r'F:\NISER internship\Sristi_di\final_data.xlsx', header=None)

# Transpose the DataFrame
transposed_df = df.transpose()

# Set the first row as column headers
transposed_df.columns = transposed_df.iloc[0]
transposed_df = transposed_df[1:]

# Save the transposed data to a new Excel file
transposed_df.to_excel('transposed_data.xlsx', index=False)
