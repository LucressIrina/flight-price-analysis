import pandas as pd
import sqlite3

# Allows Python to read my CSV file
df = pd.read_csv("Flight Prices - Resume Project - Sheet2.csv")


# Removes $ from Avg_Price column 
df['Avg_Price'] = df['Avg_Price'].str.replace('$', '', regex = False)

# Removes , from Avg_Price column 
df['Avg_Price'] = df['Avg_Price'].str.replace(',', '', regex = False)


# Converts Avg_Price data type from string values into numerical decimal values
df['Avg_Price'] = df['Avg_Price'].astype(float)


### Question - What is the cheapest month to visit each city?

## Step 1: Filter for Palmero prices for each month

Palermo_df = df[df['City'] == 'Palermo']

## Step 2: Find the cheapest flight price of Palermo using pandas' built-in aggregation function to find the minimum value

Palermo_min_price = Palermo_df['Avg_Price'].min()

### Now we know the cheapest average price for Palmero but not the month associated with it

# Setp 3: Pull the whole row with the cheapest price for Palmero

Palermo_min_month = Palermo_df [Palermo_df['Avg_Price'] == Palermo_min_price]


### Now repeat these 3 steps for all the cities (Manual Version)

"""" 
# Montevideo
Montevideo_df = df[df['City'] == 'Montevideo']
Montevideo_min_price = Montevideo_df['Avg_Price'].min()
Montevideo_min_month = Montevideo_df [Montevideo_df['Avg_Price'] == Montevideo_min_price]

# Shanghai
Shanghai_df = df[df['City'] == 'Shanghai']
Shanghai_min_price = Shanghai_df['Avg_Price'].min()
Shanghai_min_month = Shanghai_df [Shanghai_df['Avg_Price'] == Shanghai_min_price]

# Lima
Lima_df = df[df['City'] == 'Lima']
Lima_min_price = Lima_df['Avg_Price'].min()
Lima_min_month = Lima_df [Lima_df['Avg_Price'] == Lima_min_price]

# Bangkok
Bangkok_df = df[df['City'] == 'Bangkok']
Bangkok_min_price = Bangkok_df['Avg_Price'].min()
Bangkok_min_month = Bangkok_df [Bangkok_df['Avg_Price'] == Bangkok_min_price]

# Johannesburg
Johannesburg_df = df[df['City'] == 'Johannesburg']
Johannesburg_min_price = Johannesburg_df['Avg_Price'].min()
Johannesburg_min_month = Johannesburg_df [Johannesburg_df['Avg_Price'] == Johannesburg_min_price]

# Copenhagen
Copenhagen_df = df[df['City'] == 'Copenhagen']
Copenhagen_min_price = Copenhagen_df['Avg_Price'].min()
Copenhagen_min_month = Copenhagen_df [Copenhagen_df['Avg_Price'] == Copenhagen_min_price]

# Nairobi
Nairobi_df = df[df['City'] == 'Nairobi']
Nairobi_min_price = Nairobi_df['Avg_Price'].min()
Nairobi_min_month = Nairobi_df [Nairobi_df['Avg_Price'] == Nairobi_min_price]

"""""

# Advanced Method - Step 1: Group dataframe into one group per city and return the min prices for each row within each city
idx = df.groupby('City')['Avg_Price'].idxmin()

# Advanced Method - Step 2: Pull the rows from the original dataframe
cheapest_months = df.loc[idx]

# Advanced Method - Step 3: Print Results
print(cheapest_months)
