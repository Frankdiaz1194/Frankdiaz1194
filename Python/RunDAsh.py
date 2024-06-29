#RunDAsh
http://localhost:5006/dashboard_layout

#Running the Dashboard
import os
# Change the working directory to where the Excel file is located
os.chdir("C:/Users/frank/OneDrive/Escritorio/Frankdiaz1194/Python")

# Start the Panel server with autoreload enabled
!panel serve --autoreload --show dashboard_layout.py

# Find the process ID (PID) of the process using port 5006
!netstat -ano | findstr :5006

# Kill the process using the specified PID (replace 1234 with the actual PID)
!taskkill /PID 34388 /F
