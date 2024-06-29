# FInance_plots.py

import os
import panel as pn
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category10

pn.extension()

# def generatePortfolio_of_debtandassets(df1):
#     # Extract the data in cells F70 to K71
#     portfolio_data = df1.iloc[69:71, 5:11].copy()
    
#     # Set the column names to the values in the first row (index 69)
#     portfolio_data.columns = portfolio_data.iloc[0]

#     # Remove the first row (index 69) since it's now the column names
#     portfolio_data = portfolio_data.iloc[1:]

#     # Remove leading/trailing whitespaces from column names
#     portfolio_data.columns = portfolio_data.columns.str.strip()

#     # Reset the index of the DataFrame
#     portfolio_data.reset_index(drop=True, inplace=True)

#     # Fill missing values with zeros
#     portfolio_data = portfolio_data.fillna(0)

#     # Create a Bokeh figure
#     p = figure(title='Portfolio of Debt and Assets', x_axis_label='Category', y_axis_label='Amount')

#     # Plot each category as a bar
#     categories = portfolio_data.columns.tolist()
#     amounts = portfolio_data.iloc[0].tolist()
#     source = ColumnDataSource(data=dict(Category=categories, Amount=amounts))
#     p.vbar(x='Category', top='Amount', width=0.9, source=source, legend_label='Category', color=Category10[len(categories)])

#     # Add a legend
#     p.legend.click_policy = "hide"

#     # Return the Bokeh figure
#     return p

def generate_monthly_projections_plot(df):
    # Extract the data in cells D33 to I44
    monthly_projections_data = df.iloc[30:43, 3:9].copy()
    
    # Set the column names to the values in the first row (index 31)
    monthly_projections_data.columns = monthly_projections_data.iloc[0]

    # Remove the first row (index 31) since it's now the column names
    monthly_projections_data = monthly_projections_data.iloc[1:]

    # Reset the index of the DataFrame
    monthly_projections_data.reset_index(drop=True, inplace=True)

    # Exclude rows with NaN in the 'Month' column
    monthly_projections_data = monthly_projections_data[monthly_projections_data['Month'].notna()]

    # Fill missing values with zeros
    monthly_projections_data = monthly_projections_data.fillna(0)

    # Remove leading/trailing whitespaces from column names
    monthly_projections_data.columns = monthly_projections_data.columns.str.strip()

    # Convert 'Month' column to datetime format
    monthly_projections_data['Month'] = pd.to_datetime(monthly_projections_data['Month'])

    # Melt the DataFrame to have a single 'value' column for all variables
    melted_data = monthly_projections_data.melt(id_vars='Month', var_name='Variable', value_name='Amount')

    # Create a Bokeh figure
    p = figure(title='Monthly Progression', x_axis_label='Month', y_axis_label='Amount', x_axis_type='datetime')

    # Plot each variable as a separate line
    for i, variable in enumerate(melted_data['Variable'].unique()):
        source = ColumnDataSource(melted_data[melted_data['Variable'] == variable])
        p.line(x='Month', y='Amount', source=source, legend_label=variable, color=Category10[10][i])

    # Add a legend
    p.legend.click_policy="hide"

    # Return the Bokeh figure
    return p