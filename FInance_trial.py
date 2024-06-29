import os
import panel as pn
import pandas as pd
import plotly.express as px

pn.extension('plotly')

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

    # Create a line plot for each variable
    fig = px.line(melted_data, x='Month', y='Amount', color='Variable',
                  title='Monthly Progression',
                  labels={'Amount': 'Amount', 'Variable': 'Variable', 'Month': 'Month'})

    # Return the plot
    return fig

# Change the working directory to where the Excel file is located
os.chdir("G:\My Drive\school\ecc fresman and sophommore\FrankNance1")

# Load the Excel data into a DataFrame
df = pd.read_excel('Monthly_Expenses.xlsx')

# Generate the monthly projections plot
monthly_projections_plot = generate_monthly_projections_plot(df)

# Wrap the plot in a Panel object
plot_panel = pn.pane.Plotly(monthly_projections_plot)

# Create a Panel dashboard layout
dashboard_layout = pn.Column(
    "# Monthly Projections Dashboard",
    plot_panel
)

# Serve the dashboard
dashboard_layout.servable()
