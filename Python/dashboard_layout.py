#DAshboard_LAyout
import panel as pn
import pandas as pd
from FInance_plots import generate_monthly_projections_plot#, generatePortfolio_of_debtandassets

pn.extension()

# Load the Excel data into DataFrames from different sheets
df = pd.read_excel('C:/Users/frank/OneDrive/Escritorio/Frankdiaz1194/Monthly_Expenses.xlsx')
df1 = pd.read_excel('C:/Users/frank/OneDrive/Escritorio/Frankdiaz1194/Monthly_Expenses.xlsx', sheet_name='JUN')

# Generate the monthly projections plot
monthly_projections_plot = generate_monthly_projections_plot(df)

# Generate the portfolio of debt and assets plot
# portfolio_plot = generatePortfolio_of_debtandassets(df1)

# Wrap the plots in Panel objects
monthly_projections_pane = pn.pane.Bokeh(monthly_projections_plot)
# portfolio_pane = pn.pane.Bokeh(portfolio_plot)

# Create a Panel dashboard layout with tabs
dashboard_layout = pn.Tabs(
    ("Monthly Projections", monthly_projections_pane),
    # ("Portfolio of Debt and Assets", portfolio_pane)
)

# Serve the dashboard
dashboard_layout.servable()

# if monthly_projections_plot and portfolio_plot:
#     # Wrap the plots in Panel objects
#     monthly_projections_pane = pn.pane.Bokeh(monthly_projections_plot)
#     # portfolio_pane = pn.pane.Bokeh(portfolio_plot)

#     # Create a Panel dashboard layout with tabs
#     dashboard_layout = pn.Tabs(
#         ("Monthly Projections", monthly_projections_pane),
#         # ("Portfolio of Debt and Assets", portfolio_pane)
#     )

#     # Serve the dashboard
#     dashboard_layout.servable()
# else:
#     print("Failed to generate one or both plots.")
