# ===== Introduction ====================================================================
#   The following exercises will guide you in the process of installing and importing
#   libraries into your Python script. With pandas, matplotlib, and the sqlite3 libraries
#   you will learn how to load data from a CSV file, transform and analyze that data, and
#   visualize the results using plots. Additionally, you will also save the results into
#   a SQLite database.

# ===== Exercise 1) =====================================================================
#   Install the required libraries in a virtual environment in your local machine

# 1.1) Create a new Python virtual environment
pass

# 1.2) Create a `requirements.txt` file with the `pandas` and `matplotlib` libraries
pass

# 1.3) Install the required libraries using PIP and the `requirements.txt` file
pass

# 1.4) Create a Python script with the name `basic_script.py` in your local directory
pass


# ===== Exercise 2) =====================================================================
#   Import the required libraries into your Python script
import sqlite3 
import pandas as pd
from matplotlib import pyplot as plt

# 2.1) Open the script in your code editor and import the required libraries as such:

# Import the `pandas` library with a `pd` alias:
pass

# Import the `pyplot` submodule from the `matplotlib` library:
pass

# Import the `sqlite3` library:
pass

# 2.2) Print a message to confirm that the libraries were imported successfully
print("Libraries imported")

# ===== Exercise 3) =====================================================================
#   Load the data from the CSV file, display dataframe information and transform the data

# 3.1) Load the 'sales_data.csv' data file into a pandas dataframe
df = pd.read_csv("sales_data.csv")

# 3.2) Explore the data by displaying the dataframe information
print(df.head())

print(df.describe())

print(df.dtypes)

# 3.3) Transform the data by converting the data colum to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 3.4) Transform the data by creating a new column named `TotalSales`
# that calculates the total sales by multiplying the `Quantity` and `UnitPrice` columns
df['TotalSales'] = df['Quantity'] * df['UnitPrice']


# 3.5) Group the data by the `Date` column and sum the `TotalSales` values
date_sales = df.groupby('Date')['TotalSales'].sum()


# 3.6) Display the resulting dataframe results
print("\nDate Sales:")
print(date_sales)


# ===== Exercise 4) =====================================================================
#  Save the results to a SQLite database and read the database results

# 4.1) Connect to a SQLite database named `sales_data.db`
# Connect to the SQLite database
conn = sqlite3.connect('sales_data.db')

# 4.2) # Write the dataframe to SQLite database:
df.to_sql('sales_table', conn, if_exists='replace', index=False)

# 4.3 (Optional)) # Create a cursor object to execute SQL queries
cur = conn.cursor()

# 4.4 (Optional)) # Execute a SELECT query to retrieve all rows from the `sales` table
cur.execute("SELECT * FROM sales_table")

# 4.5 (Optional)) # Fetch all rows from the result of the SELECT query
rows =  cur.fetchall()

# 4.6 (Optional)) # Display the first few rows of the result
print("\nFirst few rows from SQLite database:")
for row in rows[:5]:
    print(row)

# 4.7) Close the connection to the SQLite database
cur.close()


# ===== Exercise 5) =====================================================================
#   Plot the previous dataframe that you transformed
# print(date_sales.keys)
# exit()
# Adjust the following code snippet to your pandas dataframe and the correct labels
plt.figure(figsize=(10, 6))               # Set the size of the plot (width, height)
date_sales.plot(kind= "area")                    # Create line plot with circular markers at data points
date_sales.plot(kind="line", marker="^")        # Create line plot with circular markers at data points
plt.title("Sales Data")                          # Set the title of the plot
plt.xlabel("Date")                         # Set the x-axis label
plt.ylabel("Number of Sales")                         # Set the y-axis label
plt.grid(True)                            # Display a grid on the plot
plt.xticks(rotation=45)                   # Rotate the x-axis labels by 45 degrees
plt.tight_layout()                        # Adjust plot to ensure everything fits without overlapping
plt.show()                                # Display the plot


# ===== Outro ===========================================================================
#   Hopefully, you learned how to install and import required libraries in your Python
#   scripts. Moreover you got to use some of these libraries to do some data-related
#   tasks. These skills are essential for working with data in Python. Keep practicing!