#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os

from initialization import get_p
from initialization import dict
from initialization import main
from initialization import encode
from initialization import init
import elgamal
import sys
main();

p = get_p()
x = elgamal.get_elgamal_x()

with open("grade_A.txt", "r") as f:    #得到A的成绩
    grade_a = dict [str(f.read())]

cnt = 0

for line in open('A.txt'):
    if cnt == 0:
        key_h = int(line)
    elif cnt == 1:
        key_f = int(line)
    cnt += 1
#得到 公钥

f_grade_a = encode(key_f,grade_a,p)

hf_grade_a = encode(key_h,f_grade_a,p)  #要传给B的信息


a , b = elgamal.encrypt(hf_grade_a)

f = open('B.txt', 'a')  # 输出到 B  

print(a,file=f)
print(b,file=f)

f.close()
print("转到B")
input()


# In[2]:


with open('A.txt', 'r') as fp:
    lines = fp.readlines()
    g_grade_b_b = int(lines[-1])
    g_grade_b_a = int(lines[-2])

grade_b = elgamal.decrypt(x,g_grade_b_a,g_grade_b_b)

g_x , f_x , hf_x = init()
if grade_b not in g_x:
    print("B发送错误信息")
    os.system('pause')
else:
    print("B发送正确信息\n")
    print("转到C")
    f = open('C.txt', 'a')  
    print(1,file=f)
    f.close()

input()


# In[3]:


with open('A.txt', 'r') as fp:
    lines = fp.readlines()
    g_grade_a_b = int(lines[-1])
    g_grade_a_a = int(lines[-2])

grade_a = elgamal.decrypt(x,g_grade_a_a,g_grade_a_b)
if grade_a == grade_b:
    print("相同")
else:
    print("不相同")


# In[ ]:
os.system('pause')