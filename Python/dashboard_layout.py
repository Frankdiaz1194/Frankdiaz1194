#DAshboard LAyout
import panel as pn
import pandas as pd
from plot_functions import generate_monthly_projections_plot, generate_individual_purchases_plot

pn.extension()

# Load the Excel data into a DataFrame
df = pd.read_excel('/mnt/data/Monthly_Expenses.xlsx')

# Generate the monthly projections plot
monthly_projections_plot = generate_monthly_projections_plot(df)

# Generate the individual purchases plot
individual_purchases_plot = generate_individual_purchases_plot()

# Wrap the plots in Panel objects
monthly_projections_pane = pn.pane.Bokeh(monthly_projections_plot)
individual_purchases_pane = pn.pane.Bokeh(individual_purchases_plot)

# Create a Panel dashboard layout with tabs
dashboard_layout = pn.Tabs(
    ("Monthly Projections", monthly_projections_pane),
    ("Individual Purchases", individual_purchases_pane)
)

# Serve the dashboard
dashboard_layout.servable()

