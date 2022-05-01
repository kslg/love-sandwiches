# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Essentially this import, imports the entire gspread library,  
# so that we can access any function, class or method within it.  
import gspread
# While this import, imports the Credentials class,  
# which is part of the service_account function from the Google auth library.  
from google.oauth2.service_account import Credentials

# The scope lists the APIs that the  program should access in order to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# Can access our love_sandwiches sheet
# Using the open() method on our client object and passing it the spreadsheet
SHEET = GSPREAD_CLIENT.open('love_sandwiches')
# AS A TEST - Define a new variable and using the worksheet method of the sheet,
# we can call our “sales” tab in the worksheet.  
# sales = SHEET.worksheet('sales')
# AS A TEST - Now let’s define a variable named  data, we’ll use the gspread method
# get_all_values() to pull all the values from our sales worksheet.  
# data = sales.get_all_values()
# print(data)

# Create our first function to  collect the sales data from our user.  
def get_sales_data():
    """
    Get sales figures imput from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")
get_sales_data()