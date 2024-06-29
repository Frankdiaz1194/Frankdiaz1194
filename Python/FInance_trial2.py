import os
import panel as pn
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category10
from bokeh.layouts import column

pn.extension()

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

# Change the working directory to where the Excel file is located
os.chdir("C:/Users/frank/OneDrive/Escritorio/Frankdiaz1194")

# Load the Excel data into a DataFrame
df = pd.read_excel('Monthly_Expenses.xlsx')

# Generate the monthly projections plot
monthly_projections_plot = generate_monthly_projections_plot(df)

# Wrap the plot in a Panel object
plot_pane = pn.pane.Bokeh(monthly_projections_plot)

# Create a Panel dashboard layout
dashboard_layout = pn.Column(
    "# Monthly Projections Dashboard",
    plot_pane
)

# Serve the dashboard
dashboard_layout.servable()
