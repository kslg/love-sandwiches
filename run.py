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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        #print(f"The data provided is {data_str}")
        
        # sales_data is data from the user
        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid!")
            break
        
    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    
    For the except statement, here we will except ValueError as e: The ValueError class here contains the  
    details of the error triggered by the code in our  try statement here, and by using the as keyword,  
    we're assigning that ValueError object to the e variable, which is standard Python shorthand for “error”.
   
    Use List Comprehension to convert strings into integers:
    For each individual value in the values  list, convert that value into an integer.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

# For this function to work, I need to pass it the data  to insert, so we’ll name this parameter data.  
def update_sales_worksheet(data):

    print("Updating sales worksheet...\n")
    # Need to access our sales  worksheet from our Google Sheet so we can add data to it.
    # Use the gspread worksheet() method to access our sales worksheet.  
    # The value we put in here relates to the name of our worksheet tab.
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


# Calling the "get_sales_data" function.
data = get_sales_data()

# Using List Comprehension, converting the data into integer format.
sales_data = [int(num) for num in data]

# Calling the "update_sales_worksheet" function.
update_sales_worksheet(sales_data)
