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
#csv file
data = pd.read_csv("sample_data.csv")

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


#### Removing NA from the data set:

~~~python
 df=df.dropna(axis=0, how='any')
~~~

##### dropna function here yields a dataframe as its output, and you can save it either as a DataFrame.
