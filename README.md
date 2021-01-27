# Data Cleaning.


Data cleaning is the process of preparing data for analysis by removing or modifying data
that is incorrect, incomplete, irrelevant, duplicated, or improperly formatted.



Data cleaning is one those things that everyone does but no one really talks about. 
Sure, it’s not the "sexiest" part of machine
learning. And no, there aren’t hidden tricks and secrets to uncover.

 Added a data cleaning using python/ pandas library (2rd october 2019) using property data.csv  data set.
 
 
 
 The data set  is small compared to real data machine learning models data set. i kept it simple to ease coding.



### Useful Functions 

#### Loading Libraries
~~~python
import pandas as  pd 
import numpy as np 
import matplotlib.pyplot as plt
imort seabrom as sns 
%matplotlib inline 
%load_ext autoreload
%autoreload 2
~~~

#### Loading dataset with pandas 
~~~python
#csv file, we will use the property data.csv file
data = pd.read_csv("property data.csv")

#loading excel
data_from_excel = pd.read_xlxs("  path to your file ") 

#Loading a json file 
data_from_excel = pd.read_json ("Path where you saved the JSON file")

~~~

#### Viewing data 

~~~python
#Viewing the first 5 rows
data.head()

#viewing the last 5 rows
data.tail()
~~~ 

#### Inspecting the dataset
~~~python
#Dataset shape
data.shape

#Dataset basic analysis
data.describe()
~~~

####Removing NAN, N/A & na

Remember python pandas library only recognizes nan as the missing value so it will skip any missing value recorderd with na or N/A, the steps below helps us solve that problem

~~~python
#Define a list to hold all representation of missing values 

missing_values = [ np.nan, 'N/A', 'na'] 

data = pd.read_csv("sample_data.csv", missing_values")
~~~

#### Checking for any missing value:
You can use different ways to chech for missing value 

~~~python
data.isnull()
#or
data.isnull().sum() 
#or 
data.isnull().any()
~~~

#### Visualizing the missing value with seaborn 
~~~python
sns.headmap(isnull(), yticklabels=False annot=True)
~~~
#### Removing missing values from the data set:

~~~python
 df=df.dropna(axis=0, how='any')
~~~

How is used to instruct which low should be removed, that is when how is setted to all, it drops a row if all values are missing.

#### Filling the missing values:

~~~python
#Forward fill, fills the missing value with the values above it.

data.fillna(method="ffill") 

#Back fill, fills the missing value with the values below it.

data.fillna(method="bfill") 
 
#Interploation finds the average for the above and below value and uses the value to fill the missing value

data.interpolate()
~~~


#### Filling the missing values with a specific know value:

~~~python
data.fillna({
 'Column_to_substitute' : TheValue
 })
 ~~~
 
 #### Viewing columns 
 In pandas we use the code below to view all the column in our dataset
 
 ~~~python
 #Viewing columns in data dataframe
 data.column
 ~~~
 
 #### Changing the letter casing of our column
 
 ~~~python
 #to lowercase
 data.columns.str.lower()
 
 #to uppercase
data.columns.str.upper()
 ~~~
 
 #### Remaning the columns 
 Example when i have a column called Duration that i want to name to Time i will use the snippets below
 
 ~~~python
 df.rename({"Duration": "Time"})
 
 ~~~
 
 

Get the latest snippets: https://colab.research.google.com/drive/18pYbCHhTQkjBGCYF2qM0-M0_pA6DfUso#scrollTo=h5RHxT3x4A6Y
