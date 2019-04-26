#!/usr/bin/env python
# coding: utf-8

# In[144]:


Discussion session
1. How will you read the following data into a pandas data frame ? ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt

2. How would you pick columns 0,1,3 ?
[[0, 1, 3]]

3. Use a for loop to find all rows where Co2 (column 3) enteries with the value -99.99 (these are missing values) and replace them with NaN values (try using np.nan - do you know what it is? )

4. Change names of columns to year, month, and CO2 (use colnames)

5. Add a column 'Day' and specifiy the day 15 for all enteries

6. Add a date column according to the 'year', 'month' and 'day' columns (options: use apply with lambda or for loop together with datetime.date (make sure to import it))

7. Drop the 'Day' column

8. use pandas groupby to print the yeaerly avg. of co2 per year.

9. Pick columns that you think could be used to build a model and store them in numpy array (Answer why do we do that?)

10. repeat step (3) but this time using the np.where command.

11. Download the notebook as .py script and run it from your terminal.

12. Create a branch in github repository called warm_up_draft

13. push the notebook with the name CO2 to your new branch on github.


# In[146]:


# Question 1

import pandas as pd
co2_data = pd.read_csv('co2_mm_mlo.csv', delim_whitespace=True, header=None)


# In[147]:


# Question 2

#co2_data[[0,1,3]]


# In[148]:


# Question 3

idx = range(len(co2_data[3]))

for i in idx:
    if co2_data[3][i] == -99.99:
        co2_data[3][i] = 'NaN'


# In[149]:


# Question 4

co2_data.columns = ['year', 'month', 'CO2', 'x', 'y', 'z', 'w']


# In[150]:


# Question 5

#dayslist = list(('15,' * len(co2_data['w'])).split(','))
#print(dayslist)
e = 15

co2_data['days'] = e
#co2_data.head()


# In[162]:


# Question 6 Add a date column according to the 'year', 'month' and 'day' columns (options: use apply with lambda or for loop together with datetime.date (make sure to import it))

import datetime

datelist = []
for i in idx:
    month = co2_data['month'][i]
    #print(month)
    year = co2_data['year'][i]
    #print(year)
    days = co2_data['days'][i]
    #print(days)
    datelist.append(datetime.datetime(year, month, days))

co2_data['date'] = datelist
    
#co2_data.head()


# In[164]:


# Question 7
del co2_data['days']


# In[182]:


# Question 8
co2_data.groupby('year').CO2.mean()
#co2_data.head()


# In[180]:


# Question 9 Pick columns that you think could be used to build a model and store them in numpy array (Answer why do we do that?)
import numpy as np

# We could use CO2 and date to build a very simple linear regression model.

co2_array = np.asarray(co2_data['CO2'])
co2_array


# In[187]:


# Question 10
import numpy as np
npmethod = pd.read_csv('co2_mm_mlo.csv', delim_whitespace=True, header=None)
c_array=np.asarray(npmethod[3])

result = np.where(c_array == -99.99)
print(result)



# In[ ]:


# 11. Download the notebook as .py script and run it from your terminal.


# In[ ]:


# 12. Create a branch in github repository called warm_up_draft


# In[ ]:


# 13. push the notebook with the name CO2 to your new branch on github.

