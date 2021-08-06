# -*- coding: utf-8 -*-
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
str_p = '5OOB4HVPX0KW90a54EOJ8Q944007aM6JPBQZMaCU41ACSJ46Y9a2RYUXUZPQ07QMFSS84QXHMDHSTCUIR7aTODQ1AM62XVaV4IGN28VBOBGZSK92OaPFGZ2ORVB1CAXV0CLQWTAMHD6FXW5J0MAKK1PIQaFQCM19QBOADLYP0P5APBL7322256NT6QGEN13GNZ786'
p = str2int(str_p)

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

elgamal_g = 58915722462978682534126247597454067955853336194376986361024501907189851818542729349015243532285142254309917038527760480288965375502923681203720322102110510143690634732096092436946408002757529613271536307927837223545322777240018954252741320474283752983445102922773653761893093283466588488022478739526104458288
x = 574
y = power(elgamal_g, x, p)
k = random.randint(1,p)  # 与p - 1互素的随机数

def get_elgamal_x():
    return x

def encrypt(m):
    a = power(elgamal_g, k, p)
    b = power(y, k, p) * m % p
    return a, b

def decrypt(x, a, b):
    ax = power(a, x, p)
    ia = ModReverse(ax, p)
    msg = int(b * ia % p)

    return msg
