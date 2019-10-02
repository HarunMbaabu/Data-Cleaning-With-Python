# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv("property data.csv")

# Take a look at the first few rows
df.head()


# Making a list of missing value types
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property data.csv", na_values = missing_values)


# Looking at the NUM_BEDROOMS column
print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())


# Looking at the OWN_OCCUPIED column
print (df['OWN_OCCUPIED'])
print (df['OWN_OCCUPIED'].isnull())


# Detecting numbers 
cnt=0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
    except ValueError:
        pass
    cnt+=1


# Total missing values for each feature
print (df.isnull().sum())


# Any missing values?
print (df.isnull().values.any())



# Total number of missing values
print (df.isnull().sum().sum())


# Replace missing values with a number
df['ST_NUM'].fillna(125, inplace=True)



# Location based replacement
df.loc[2,'ST_NUM'] = 125



# Replace using median 
median = df['NUM_BEDROOMS'].median()
df['NUM_BEDROOMS'].fillna(median, inplace=True)