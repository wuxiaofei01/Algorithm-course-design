#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os
import sys

from initialization import get_p
from initialization import dict
from initialization import encode
from initialization import init
import elgamal
p = get_p()
x = elgamal.get_elgamal_x()
with open("grade_B.txt", "r") as f:    #得到A的成绩
    grade_b = dict [str(f.read())]
cnt = 0

for line in open('B.txt'):
    if cnt == 0:
        key_f = int(line)
    elif cnt == 1:
        key_g = int(line)
    elif cnt == 2:
        hf_grade_a_a = int(line)
    elif cnt ==3 :
        hf_grade_a_b = int(line)
    cnt += 1
#得到 公钥
#解析
hf_grade_a = elgamal.decrypt(x,hf_grade_a_a,hf_grade_a_b)

g_x , f_x , hf_x = init()
if hf_grade_a not in hf_x:
    print("A发送错误信息")
    os.system('pause')
else :
    print("A发送正确信息")

#发送给C
f_grade_b = encode(key_f,grade_b,p) #发给C

a , b = elgamal.encrypt(f_grade_b)

f = open('C.txt', 'a')  

print(a,file=f)
print(b,file=f)

f.close()


#发送给A

g_grade_b = encode(key_g,grade_b,p) #发给A
a , b = elgamal.encrypt(g_grade_b)

f = open('A.txt', 'a')  

print(a,file=f)
print(b,file=f)

f.close()
print("转到C， 若C 没问题 进行下一步")
input()


# In[2]:


with open('B.txt', 'r') as fp:
    lines = fp.readlines()
    hf_grade_b_b = int(lines[-1])
    hf_grade_b_a = int(lines[-2])

hf_grade_b = elgamal.decrypt(x,hf_grade_b_a,hf_grade_b_b)
if hf_grade_b == hf_grade_a:
    print("相同")
else:
    print("不相同")


# In[ ]:



os.system('pause')
