#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Create a function that takes a list of numbers as input and returns the sum and average of those numbers.
def sum_and_average(data):
    average = sum(data)/ len(data)
    total = sum(data)
    return (total, average)

input_data = [23.5, 22.4, 21.7, 24.3, 25.0]

data_sum, data_average  = sum_and_average(input_data)
print('The sum of the data is {:.3f} and the average is {:.3f}'.format(data_sum, data_average))








