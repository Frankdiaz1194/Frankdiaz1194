# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Activate the environment
!conda activate myenv

# Install bokeh
!conda install bokeh

# Alternatively, use pip
pip install bokeh
pip install pandas openpyxl bokeh


import os

# Set the working directory
os.chdir(r'G:\My Drive\school\ecc fresman and sophommore\Personal Finance\FrankNance')

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
import pandas as pd


# Load the data from the spreadsheet
df = pd.read_excel('expenses (version 1)1.xlsx')


import pandas as pd

# Assuming df is your DataFrame loaded from an Excel file
excel_file_path = r'G:\My Drive\school\ecc fresman and sophommore\Personal Finance\FrankNance\expenses (version 1)1.xlsx'
xls = pd.ExcelFile(excel_file_path)

# Get the sheet names (tabs)
sheet_names = xls.sheet_names

# Print the number of tabs
print("Number of tabs (sheets):", len(sheet_names))
print("Sheet names:", sheet_names)


# Create some example plots
plot1 = figure(width=400, height=400)
plot1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=15, color="navy", alpha=0.5)

plot2 = figure(width=400, height=400)
plot2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2, color="green")

# Arrange the plots in a column layout
layout = column(plot1, plot2)

# Output the result to a static HTML file
output_file("column_layout.html")

# Display the layout in the browser
show(layout)

