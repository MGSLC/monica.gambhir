#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task 1: Factorial Calculator: Write a Python program that calculates the factorial of a given number.

#Enter the number whose factorial is to be found
n = int(input("Enter input number: "))
 
factorial = 1; #initialize
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print("The factorial of",n,"is",factorial)


# In[ ]:




