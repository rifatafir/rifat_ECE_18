#!/usr/bin/env python
# coding: utf-8

# In[1]:


List = [1,2,3,4,5,6,7]
print(List[2])


# In[3]:


first_number = int(input("Enter the first number: "))
secound_number = int(input("Enter the secound number: "))
print("The sum of two number is ", first_number+secound_number)
print("The difference of two number is ",first_number-secound_number)
print("The product of two number is ",first_number*secound_number)


# In[4]:


a = int(input("Enter the first number: "))
b = int(input("Enter the secound number: "))
print(int(a/b))
print(float(a/b))


# In[5]:


color_list = ["Red","Green","White" ,"Black"]
print("The first element is: ",color_list[0])
print("The last element is: ",color_list[-1])


# In[7]:


print(''' a string that you "don't" have to escape
                    This
             is a ...........multi-line
    heredoc string .............>example''')


# In[8]:


base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
print("The area of tringle is  ", 0.5*base*height)


# In[10]:


print("My name is Rifat")
print("I am 22 years old")
print("I live in Fulbari in Dinajpur district")


# In[11]:


P = int(input("Enter the Principle Amount: "))
R = int(input("Enter the rate: "))
T = int(input("Enter the Time span: "))
A = float(R/100)
A = A +1
A = A * P
print("Compound interest = ", A-P)


# In[46]:


list = "* "
space = " "
for i in range(5,0,-1):
    print(space*(5-i),list*i)


# In[47]:


celcious = float(input("Enter celcious: "))
fernheight = float((celcious * 1.8)+ 32)
print(fernheight)


# In[ ]:




