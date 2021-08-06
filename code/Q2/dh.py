# -*- coding: utf-8 -*-

trans_tab = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20,
             'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31,
             'W': 32, 'X': 33, 'Y': 34, 'Z': 35, 'a': 36}

str_g = '2GRWLNCa06869POBMQPGOM5TUXC1A60O0WGPZOG2DRWLPH1KXGFHXOGL94KYRO4431UM5U5VC2ZZPTHFV5J9P9DWBJ8IS8S1CGO0UO86562F08PWTJHBIKFELY6JKQ15IQCJOO3CLO7RQIKAO6KT83KaP3XARZFXRIC9205GQE086GIU0AWD8QLN02LMQHNISTYYL'
str_p = '5OOB4HVPX0KW90a54EOJ8Q944007aM6JPBQZMaCU41ACSJ46Y9a2RYUXUZPQ07QMFSS84QXHMDHSTCUIR7aTODQ1AM62XVaV4IGN28VBOBGZSK92OaPFGZ2ORVB1CAXV0CLQWTAMHD6FXW5J0MAKK1PIQaFQCM19QBOADLYP0P5APBL7322256NT6QGEN13GNZ786'

def str2int(s):
    ans = 0
    for c in s:
        ans = ans * 37 + trans_tab[c]
    return ans


# Modular exponentiation
def power(a,b,c):
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans


# Driver code
def DH(A, B):
    # print(p)
    # print(g)

    a_send_b = power(g, A, p)
    # print("a send to b is : ", a_send_b)
    b_send_a = power(g, B, p)
    # print("b send to a is : ", b_send_a)
    sa = power(b_send_a, A, p)
    # print("a calculate Sa is : ", sa)
    sb = power(a_send_b, B, p)
    # print("b calculate Sb is : ", sb)

    # print("is same ? ", sa == sb)
    return  sa


def main(A, B):

    DH(A, B)
    
p = str2int(str_p)
g = str2int(str_g)

if __name__ == '__main__':
    main(1 ,2 )
