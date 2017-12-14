
# coding: utf-8

# In[1]:


#Function with 1,2 and arbitrary arguments
def func1(a):
    print("Square of " +str(a)+ " is" ,a**2)

def func2(fname,lname):
    print(fname +" "+ lname)

def funca(*x):
    for i in x:
        print("Square of " +str(i)+ " is" ,i**2)

func1(10)
func2("Hello","Python")
funca(1,2,3,4,5)


# In[6]:


#Factorial of a number using function
def fact(num):
    value=1
    for i in range(1,num+1):
        value=value*i
    print("Factorial of " +str(num)+ " is " +str(value))
val=int(input("Enter a number to find factorial "))
fact(val)


# In[18]:


def square(num):
    return num**2


# In[25]:


#Use of Lambda Function
  #1.map(to map functions and inputs)
    
arr=list((1,2,3,4,5)) 
list(map(lambda x:square(x),arr))


# In[28]:


#2.filter(filter input based on conditions)

a={1,1,2,3,4,5,6,6,8,10}
set(filter(lambda x:(x%2==0),a))


# In[36]:


#3.reduce(Performs computation on a list)
from functools import reduce
f = lambda x,y: x if(x > y) else y
(reduce(f,[1,5,8,2,4,23,20,21,17,16]))

