import pandas as pd

# List of Excel file paths
excel_files = [
    r'F:\NISER internship\Sristi_di\column_1.xlsx',
    r'F:\NISER internship\Sristi_di\column_2.xlsx',
    r'F:\NISER internship\Sristi_di\column_3.xlsx',
    r'F:\NISER internship\Sristi_di\column_4.xlsx',
    r'F:\NISER internship\Sristi_di\column_5.xlsx'
]

# Column names
metabolite_column = 'MB NAME'
area_column = 'Area'

# Initialize an empty dictionary to store the metabolite areas
metabolite_areas = {}

# Iterate over each Excel file
for file in excel_files:
    # Read the Excel file
    df = pd.read_excel(file)
    
    # Iterate over each row in the dataframe
    for index, row in df.iterrows():
        # Get the metabolite name and area
        metabolite = row[metabolite_column]
        area = row[area_column]
        
        # Check if the metabolite is already present in the dictionary
        if metabolite in metabolite_areas:
            # Append the area to the existing list
            metabolite_areas[metabolite].append(area)
        else:
            # Create a new list with the area
            metabolite_areas[metabolite] = [area]

# Create a new DataFrame from the dictionary
final_data = pd.DataFrame.from_dict(metabolite_areas, orient='index').transpose()

# Save the final data to a new Excel file
final_data.to_excel('final_data.xlsx', index=False)
