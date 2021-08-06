#!/usr/bin/env python
# coding: utf-8
import os

p = 132082441570557374456290732908446702676403844238487778883679093167409086673634190476213774909368271577496725810325765003972550423256627127248970492959802414014369226782639132063334038120109344801309525843090719418377786034230671255685046416802808673125217380814645238907503914645341273166021467622477351442455
g = 57174151330986521449965108919968959071435159831931495070564694885999877847690108769876753674753886598857483773480514498343388333316639366330220521415595523434043562075022671721344189605951112515367787580957010248523037973495152570353204405872550288633108876378486310678315235976745445737751704596028749090700
def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
    return x % c



C_info = 1024
# 3、利用a发过过来的内容计算
with open("C/C_dh_recive_from_A.txt", "r") as f:
    a_send_c = int(f.read())
f.close()
S_ac = power(a_send_c,  C_info, p)

print("AC已获得dh密钥")

# B C 进行DH密钥交换
# 3、利用b发过过来的内容计算
with open("C/C_dh_recive_from_B.txt", "r") as f:
    b_send_c = int(f.read())
f.close()
S_bc = power(b_send_c,  C_info, p)
print("BC已获得dh密钥")



#####以上均算初始化


## 17

# C比较结果并加密发回
with open("C/C_recive_A_encrypted.txt", "r") as f:
    A = f.read()
f.close()
with open("C/C_recive_B_encrypted.txt", "r") as f:
    B = f.read()
f.close()
#print(A)
#print(B)
A = A.replace(str(S_ac),'')
B = B.replace(str(S_bc),'')
#print(A)
#print(B)

res = int((A == B)) + 5     # +5 只是想避免不相等时res=0，下面计算的b为0
#print(res)

print("C比较得到结果")



elgamal_g = 58915722462978682534126247597454067955853336194376986361024501907189851818542729349015243532285142254309917038527760480288965375502923681203720322102110510143690634732096092436946408002757529613271536307927837223545322777240018954252741320474283752983445102922773653761893093283466588488022478739526104458288
k1 = p - 2  # 与p - 1互素的随机数
with open('C/C_elg_y_A.txt', 'r') as f:
    ya = int(f.read())
#print(ya)
f.close()
a1 = power(elgamal_g, k1, p)
b1 = power(ya, k1, p) * res % p
#print(a1)
#print(b1)
with open("A/res.txt", "w") as f:
    f.write(str(a1) + ',')
    f.write(str(b1))
f.close()

k2 = p - 4  # 与p - 1互素的随机数
with open('C/C_elg_y_B.txt', 'r') as f:
    yb = int(f.read())
f.close()
a2 = power(elgamal_g, k2, p)
b2 = power(yb, k2, p) * res % p

with open("B/res.txt", "w") as f:
    f.write(str(a2) + ',')
    f.write(str(b2))
f.close()

print("C将比较结果分别用两个ELGAMAL公钥加密发回")
print("> 切给A")

# In[ ]:


os.system('pause')

