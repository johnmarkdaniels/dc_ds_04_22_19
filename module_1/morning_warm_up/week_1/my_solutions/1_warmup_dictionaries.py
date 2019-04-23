#!/usr/bin/env python
# coding: utf-8

# In[13]:


### 1. Create a dictionary where each object contains a list of one float (Age) and one string (Family name) (at least 5 objects)
### Example: `{Charles: [23.4, "Darwin"], Alan: [42.5, "Turing"]}`

Family_Ages = {'Dara': [40.1, "Duncan"], 'Mark': [44.5, "Daniels"], 'Estel': [74.5, "Daniels"], 'Marilyn': [64.5, "Wilson"], 'Sebastian': [7.7, "Daniels"], 'Elias': [9.7, "Daniels"]}

print(Family_Ages)


# In[14]:


### 2. Delete one object from the dictionary

del(Family_Ages['Mark'])
print(Family_Ages)


# In[15]:


### 3. Replace the float number of one of your objects - we are changing a list entry inside a dictionary record! look at Darwin's new age
### Example: `{Charles: [99.73, "Darwin"], Alan: [42.5, "Turing"]}`

Family_Ages['Dara'][0] = 35
print(Family_Ages)


# In[33]:


### 4. write a for loop that goes through all records in the dictionary, prints the family name and assigns the float numbers into one merged list (see ages)
### `ages = [23.4, 22.9, 552.9]`

ages = []
for key, value in Family_Ages.items():
    print(value[1])
    ages.append(value[0])
    
print(ages)


# In[ ]:


### 5. Download your notebbok as a .py (regular python script) save it somewhere you know


# In[ ]:


### 6. Go to terminal, navigate to the folder where you have saved the script and execute it through the terminal
### `use commandds: 
###  cd and 
###  python your_script.py`


# In[ ]:


### [optional] Calculate with a for loop the median and mean of the ages list

