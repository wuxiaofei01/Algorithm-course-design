#!/usr/bin/env python
# coding: utf-8

# In[35]:


import random
import sys
from math import pow
import math


# In[33]:


def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c

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


# In[23]:


trans_tab = {'0':0, '1':1, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
             'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20,
             'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31,
             'W':32, 'X':33, 'Y':34, 'Z':35, 'a':36}


def str2int(s):
    ans = 0
    for c in s:
        ans = ans * 37 + trans_tab[c]
    return ans


# In[ ]:


print("请输入两人成绩，只有优良中差")
A_grade=0
B_grade=0
while(1):
    print("请输入A的成绩！")
    A_grade=input()
    if(A_grade=="优"):
        break
    elif(A_grade=="良"):
        break
    elif(A_grade=="中"):
        break
    elif(A_grade=="差"):
        break
    else:
        print("成绩只有优良中差别乱输入")

while(1):
    print("请输入B的成绩！")
    B_grade=input()
    if(B_grade=="优"):
        break
    elif(B_grade=="良"):
        break
    elif(B_grade=="中"):
        break
    elif(B_grade=="差"):
        break
    else:
        print("成绩只有优良中差别乱输入")
        

if(A_grade=="优"):
    A_grade=1
elif(A_grade=="良"):
    A_grade=2
elif(A_grade=="中"):
    A_grade=3
elif(A_grade=="差"):
    A_grade=4

if(B_grade=="优"):
    B_grade=1
elif(B_grade=="良"):
    B_grade=2
elif(B_grade=="中"):
    B_grade=3
elif(B_grade=="差"):
    B_grade=4
with open("A/A的成绩.txt","w") as f:
    f.write(str(A_grade))
with open("B/B的成绩.txt","w") as f:
    f.write(str(B_grade))


# In[12]:


with open("Elgamal_g.txt", "r") as f:  # 打开文件
    data_g = f.read()
#print(data_g)


# In[13]:


elgamal_g=str2int(data_g)
#print(elgamal_g)


# In[27]:


with open("p.txt", "r") as f:  # 打开文件
    data_p = f.read()
#print(data_p)


# In[28]:


p=str2int(data_p)
#print(p)


# In[29]:


with open("A/A的成绩.txt", "r") as f:  # 读取A的成绩
    grade_A = f.read()
with open("B/B的成绩.txt", "r") as f:  # 读取B的成绩
    grade_B = f.read()


# In[30]:


if (grade_A==grade_B):
    x=random.randint(2,p-1)
    y=power(elgamal_g,x,p) 
    x_strA=str(x)
    y_strA=str(y)
    x_strB=str(x)
    y_strB=str(y)
else:
    x_A=random.randint(2,p-1)
    y_A=power(elgamal_g,x_A,p)
    x_B=random.randint(2,p-1)
    y_B=power(elgamal_g,x_B,p)
    x_strA=str(x_A)
    y_strA=str(y_A)
    x_strB=str(x_B)
    y_strB=str(y_B)


# In[31]:


with open("A/A_messege_公钥B.txt","w") as f:
    f.write(y_strB)
with open("A/A_messege_私钥A.txt","w") as f:
    f.write(x_strA)
with open("B/B_messege_公钥A.txt","w") as f:
    f.write(y_strA)
with open("B/B_messege_私钥B.txt","w") as f:
    f.write(x_strB)


# In[32]:


print("已经成功分配密钥，请执行另外两个程序")


# In[ ]:




