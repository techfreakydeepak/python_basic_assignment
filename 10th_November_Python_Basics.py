#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PW ASS. Python_basics


"Topic:- Python Basic variable "
"Question number :1"

a=30 # We also give user defined data also . # a = int(input("enter the value of the of a"))
b=20 ## We also give user defined data also . # b = int(input("enter the value of the of b"))
a=a+b
b=a-b
a=a-b #we assign the sum of the a and b to a . at this point,a contains the sum of the original values of a and b.
print("After swapping")
print("a=",a)
print("b=",b)


# In[5]:


"Topic:- Python Basic Variable"
"Question Number: 2"
a =int(input("Enter the  length of rectangle ")) # we enter the value of the length in integer formate.
b= int(input("Enter the breadth of rectangle")) # We enter the value of the  breadth in integer formate.
z=a*b # Using Mathmatics formula ("Length*breadth")
print("Area of Rectangle:",z)# here's our output


# In[13]:


"Topic:- Python Basic Variable"
"Question Number: 3"
# Taking temperature in Celsius as input
celsius = float(input("Enter temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Displaying the result
print("Temperature in Fahrenheit:", fahrenheit)


# In[14]:


"Topic :- String Based Questions"
"Question Number: 1"
string_input=input("enter a string")# input function to get a string input by the user.
length = len(string_input) # len fucntion is used to find the length of the string.
print("length of the string",length)# here we use  to print function  to show the length of the string


# In[15]:


"Topic :- String Based Questions"
"Question Number: 2"
sentence = input("Enter a sentence")# input function here store it in the sentence variable 
vowels = "AEIOUaeiou"# I define here the vowels 
count =0 # Count function is to keep tarck  of the number the vowels found in the input sentence 
for char in sentence: # for loop is used through a each character in the sentence for checking the each characters present in the vowels
    if char in vowels: # in operator to check the vowels string using the in operator
        count +=1 # counrt+1 is to increment the count variable by1
print("Number of Vowels",count)


# In[19]:


"Topic :- String Based Questions"
"Question Number: 3"
input_string  ="Happy, Diwali "
reversed_string = input_string[::-1] # here we use slicing  notation reverse the order of the characters in the input string
print(reversed_string) # here we reversed the string to get the our answer


# In[22]:


"Topic :- String Based Questions"
"Question Number: 4"

input_string = input("enter the string") # input here a string
#l=len(str)
p=1-1
index=0 # check the index here 
while(index<p): # we using while loop here 
    if(str[index]==str[p]): # if else satement is use are there
        index=index+1 # # index+1 its means that adding 1 element in it
        p=p-1
    else:
        print("string is not a Palindrome")
        break 
else:
    print("string is a Palondrome")


# In[ ]:


"Topic :- String Based Questions"
"Question Number: 5"
input_string = input("enter the a string")
modified_string = input_string.repalce("","")
print("modified_string",modified_string)


# In[ ]:





# In[ ]:





# In[ ]:




