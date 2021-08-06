#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os
import sys

from initialization import get_p
from initialization import dict
from initialization import encode
from initialization import hf_x
from initialization import init
import elgamal

x = elgamal.get_elgamal_x()
p = get_p()

with open("grade_A.txt", "r") as f:    #得到A的成绩
    grade_a = dict [str(f.read())]
cnt = 0

for line in open('C.txt'):
    if cnt == 0:
        key_h = int(line)
    elif cnt == 1:
        key_g = int(line)
    elif cnt == 2:
        f_grade_b_a = int(line)
    elif cnt ==3 :
        f_grade_b_b = int(line)
    cnt += 1
#得到 公钥
f_grade_b = elgamal.decrypt(x,f_grade_b_a,f_grade_b_b)

g_x , f_x , hf_x = init()
if f_grade_b not in f_x:
    print("B发送错误信息")
    os.system('pause')
else:
    print("B发送正确信息\n")
    print("请转到A，检查接收信息是否正确\n")
input()


# In[2]:




with open('C.txt', 'r') as fp:
    lines = fp.readlines()
    check = int(lines[-1])
if check != 1:
    sys.exit(0)
    
g_grade_a = encode(key_g,grade_a,p)
a , b = elgamal.encrypt(g_grade_a)

f = open('A.txt', 'a')  
print(a,file = f)
print(b,file = f)
f.close()

hf_grade_b = encode(key_h,f_grade_b,p)
a , b = elgamal.encrypt(hf_grade_b)


f = open('B.txt', 'a')  
print(a,file = f)
print(b,file = f)
f.close()
print("转到 A B，进行验证")


# In[ ]:




os.system('pause')