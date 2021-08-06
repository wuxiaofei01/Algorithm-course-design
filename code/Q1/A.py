#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import sys
import os
from math import pow
import math


# In[2]:


def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c

def power1(a, b, c,m):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return (x*m) % c

def EX_GCD(a,b,arr): #扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = EX_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return g

def ModReverse(a,n): #ax=1(mod n) 求a模n的乘法逆x
    arr = [0,1,]
    gcd = EX_GCD(a,n,arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1

#ax = power(a, x, p)
#ia = ModReverse(ax, p)

#msg = b * ia % p

#print(msg)


# In[3]:


with open("A/A_messege_公钥B.txt", "r") as f:  # 读取A要用的公钥
    Pub_key = f.read()
with open("A/A_messege_私钥A.txt", "r") as f:  # 读取A要用的私钥
    Pri_key = f.read()
with open("A/A的成绩.txt", "r") as f:  # 读取A的成绩
    grade = f.read()


# In[4]:


grade=int(grade)
#print(grade)


# # 加密

# In[5]:


p=132082441570557374456290732908446702676403844238487778883679093167409086673634190476213774909368271577496725810325765003972550423256627127248970492959802414014369226782639132063334038120109344801309525843090719418377786034230671255685046416802808673125217380814645238907503914645341273166021467622477351442455
g=58915722462978682534126247597454067955853336194376986361024501907189851818542729349015243532285142254309917038527760480288965375502923681203720322102110510143690634732096092436946408002757529613271536307927837223545322777240018954252741320474283752983445102922773653761893093283466588488022478739526104458288


# In[6]:


k = random.randint(pow(10, 2), pow(10, 20))
while(1):
    ran_num=math.gcd(k,p-1)
    if(ran_num==1):
        break
    k=k+1
#print(k)


# In[7]:


y=int(Pub_key)
x=int(Pri_key)
#print(x)


# In[11]:


a=power(g,k,p)
b=power1(y,k,p,grade)
#print(a)


# In[12]:


ax = power(a, x, p)
ia = ModReverse(ax, p)

msg = b * ia % p


# In[14]:


if(msg==grade):
    print("成绩相同")
else:
    print("成绩不相同")
os.system("pause")


# In[ ]:




