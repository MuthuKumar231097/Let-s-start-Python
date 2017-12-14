
# coding: utf-8

# In[1]:


#List of Datatypes in Python are
 # 1.Number(int,float,compex)
 # 2.String(Immutable)
 # 3.List[Mutable]
 # 4.Tuple(Immutable)
 # 5.Sets{Eleminates the duplicate}
 # 6.Dictinary{key:Value}


# In[3]:


# 1.Number
a=5
b=6.5
c=2+6j
d,e,f=-2987,-67.9876,400-599j
print(a,b,c)
print(d,e,f)


# In[12]:


# 2.String
name="Hey hello"
print(name)
print(name[5])
name[5]="s"
print(name[5])


# In[13]:


# 3.Tuple
mylist=[1,2.5,4+6j,"Python"]
print(mylist)
mylist[3]="Easy to Learn"
print(mylist)


# In[14]:


# 4.List
mytuple=(a,5,-200+600j,"Python")
print(mytuple)
mytuple[3]="East to learn"
print(mytuple)


# In[15]:


# 5.Sets
myset={1,2,1,2,3+6j,3+6j,"Hello","Hello"}
print(myset)


# In[25]:


# 6.Dictionary
mydict={1:10,2:20,3:"Hey"}
mydict1={5:"Hii","Python":6}
print("mydict[3]= ",mydict[3])
print("mydict[Python]= ",mydict1["Python"])


# In[33]:


# Identify DataTypes
print(type(a))
print(type(b))
print(type(c))
print(type(name))
print(type(mytuple))
print(type(mylist))
print(type(myset))
print(type(mydict))


# In[35]:


# use of .format
print("Hey lets start {0}".format(mydict1))
print("Hey lets start {name} " .format(name="Python"))


# In[36]:


# use sep and end
print(10,20,30,40)
print(10,20,30,40,sep=",",end="---")


# In[40]:


#Getting user input and add number
num1=input("Enter first number")
num2=input("Enter second number")
print(num1 + num2)

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
print(num1 + num2)


# In[43]:


# Import
import math
print(math.pi)

from math import pi
print(pi)


# In[44]:


#Python Operators

#Arithmetic - +,-,*,/,%,//,**

a = 10
b = 3
a/b # float -3.33333
a%b
print(a//b) #- 3
print(a**b)

#Comparison operator <,>,==,!=,>=,<=

#Logical operator  and, or ,not

a = 5
b = 6

if((a==3) or (b==6)):
    print("Condition satisfied")

if(not (a ==1)):
    print("in if")
    
#Bitwise operator &,|,~,^,>>,<<

x = 10 #(0000 1010)
y = 4  #(0000 0100)

print(x & y)  #(0000 0000)
print(x | y)  #(0000 1110)
~x     #(1111 0101)

print(x>>2)   #(0000 0010)
print(x<<2)   #(0010 1000)

#Assigngment operator

# =,+=,-=,*=,/=


#Identity operator

# is, is not

x1 = 5
y1 = 5

print(x1 is not y1)

#Membership operator

# in , not in
x = 'Hello world'

print('H' not in x)

y =[1,2,3,7,5]

print(5 in y)


# In[45]:


# Use of range function
  # range(startvalue,endvalue,inc(optional))
for i in range(10,20,2):
    print(i)


# In[47]:


# Break and Continue
for val in "Python":
    if val == "t":
        break
    print(val)
    
print('\n')
for val in "Python":
    if val == "t":
        continue
    print(val)


# In[51]:


# Pass Statement(To create empty body)
for i in range(-100,100,5):
    pass
    
    

