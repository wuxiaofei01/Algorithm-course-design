#!/usr/bin/env python
# coding: utf-8
import os
import random

trans_tab = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20,
             'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31,
             'W': 32, 'X': 33, 'Y': 34, 'Z': 35, 'a': 36}

def str2int(s):
    ans = 0
    for c in s:
        ans = ans * 37 + trans_tab[c]
    return ans

str_g = '2GRWLNCa06869POBMQPGOM5TUXC1A60O0WGPZOG2DRWLPH1KXGFHXOGL94KYRO4431UM5U5VC2ZZPTHFV5J9P9DWBJ8IS8S1CGO0UO86562F08PWTJHBIKFELY6JKQ15IQCJOO3CLO7RQIKAO6KT83KaP3XARZFXRIC9205GQE086GIU0AWD8QLN02LMQHNISTYYL'
str_p = '5OOB4HVPX0KW90a54EOJ8Q944007aM6JPBQZMaCU41ACSJ46Y9a2RYUXUZPQ07QMFSS84QXHMDHSTCUIR7aTODQ1AM62XVaV4IGN28VBOBGZSK92OaPFGZ2ORVB1CAXV0CLQWTAMHD6FXW5J0MAKK1PIQaFQCM19QBOADLYP0P5APBL7322256NT6QGEN13GNZ786'
p = str2int(str_p)
g = str2int(str_g)
#print(p)
#print(g)

grade_map = {'优':78, '良':59, '中':57, '差':28}

with open("B/B_grade.txt", "r", encoding='utf-8') as f:  # 读取B成绩
    B_grade = f.read()

#print(B_grade)
B_grade = grade_map[B_grade]
#print(B_grade)
f.close()

print("已读取B的成绩")

## 5
def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c

# B C间elgamal加密结果
elgamal_g = 58915722462978682534126247597454067955853336194376986361024501907189851818542729349015243532285142254309917038527760480288965375502923681203720322102110510143690634732096092436946408002757529613271536307927837223545322777240018954252741320474283752983445102922773653761893093283466588488022478739526104458288
x = random.randint(66, 666)
y = power(elgamal_g, x, p)
with open('C/C_elg_y_B.txt', 'w') as f:
    f.write(str(y))
f.close()



B_rand = 171

# 3、利用a发过过来的内容计算
with open("B/B_dh_recive_from_A.txt", "r") as f:
    a_send_b = int(f.read())
f.close()
S_ab = power(a_send_b, B_rand, p)

print("AB已获得dh密钥")

# 3、利用c发过过来的内容计算
with open("B/B_dh_recive_from_C.txt", "r") as f:
    c_send_b = int(f.read())
f.close()
S_bc = power(c_send_b, B_rand * 5, p)
#print(S_bc)

print("BC已获得dh密钥")




##### 以上均算初始化

# B将成绩用S_ab和S_bc加密后发给C

import hashlib
sha = hashlib.sha256()
sha.update(bytes(str(S_ab*100 + B_grade), encoding='utf-8'))
t1 = sha.hexdigest()
#print(t1)

with open("C/C_recive_B_encrypted.txt", "w") as f:
    t2 = str(S_bc) + t1
    #print(t2)
    f.write(t2)
f.close()

print("B将成绩加密发给C")
print("> 切到C")
input()



with open("B/res.txt", "r") as f:
    a, b = map(int, f.read().split(','))
#print(a, '\n', b)
f.close()

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

ax = power(a, x, p)
ia = ModReverse(ax, p)

msg = int(b * ia % p) - 5

print("B解密得结果")
print("SAME" if msg == 1 else "NOT SAME")

os.system('pause')
