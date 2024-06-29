# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:34:41 2024

@author: frank
"""
http://localhost:5006/FInance_trial2
import os

#Running the Dashboard

# Change the working directory to where the Excel file is located
os.chdir("C:/Users/frank/OneDrive/Escritorio/Frankdiaz1194/Python")

# Start the Panel server with autoreload enabled
!panel serve --autoreload --show FInance_trial2.py

# Find the process ID (PID) of the process using port 5006
!netstat -ano | findstr :5006

# Kill the process using the specified PID (replace 1234 with the actual PID)
!taskkill /PID 42632 /F
