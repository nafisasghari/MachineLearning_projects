
# coding: utf-8

# In[7]:

# importing data & spliting it:
import numpy as np
def split_X_y (dataset):
    X = dataset.drop ("Target", axis=1) 
    y = dataset["Target"]
    return X, y

def test_case ( test_set, num_instances =100): 
    case_index= np.random.randint(0,len(test_set),num_instances)
    case =test_set.iloc[case_index]
    return case

