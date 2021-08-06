# -*- coding: utf-8 -*-
from dh import DH
import random
# 优78 良59 中57 差28
dict = {"优": 78, '良': 59, '中': 57, '差': 28}
p = 132082441570557374456290732908446702676403844238487778883679093167409086673634190476213774909368271577496725810325765003972550423256627127248970492959802414014369226782639132063334038120109344801309525843090719418377786034230671255685046416802808673125217380814645238907503914645341273166021467622477351442455

hf_x = set()
g_x = set()
f_x = set()


def encode(a , b ,c):
    return (a + b) %c;

def get_p():
    return p


def init():

    cnt = 0

    for line in open('A.txt'):
        if cnt == 0: 
            key_h = int(line)
        elif cnt == 1:
            key_f = int(line)
        cnt += 1

    cnt = 0
    for line in open('B.txt'):
        if cnt == 0:
            h = int(line)
        elif cnt == 1:
            key_g = int(line)
        cnt += 1
    
    grade_g1 = encode(key_g, 78, p)
    grade_g2 = encode(key_g, 59, p)
    grade_g3 = encode(key_g, 57, p)
    grade_g4 = encode(key_g, 28, p)

    g_x.add(grade_g1)
    g_x.add(grade_g2)
    g_x.add(grade_g3)
    g_x.add(grade_g4)

    grade_f1 = encode(key_f, 78, p)
    grade_f2 = encode(key_f, 59, p)
    grade_f3 = encode(key_f, 57, p)
    grade_f4 = encode(key_f, 28, p)

    f_x.add(grade_f1)
    f_x.add(grade_f2)
    f_x.add(grade_f3)
    f_x.add(grade_f4)

    grade_hf1 = encode(key_h, grade_f1, p)
    grade_hf2 = encode(key_h, grade_f2, p)
    grade_hf3 = encode(key_h, grade_f3, p)
    grade_hf4 = encode(key_h, grade_f4, p)

    hf_x.add(grade_hf1)
    hf_x.add(grade_hf2)
    hf_x.add(grade_hf3)
    hf_x.add(grade_hf4)

    return g_x , f_x , hf_x

def get_keys():

    a = random.randint(1, pow(10, 30))
    b = random.randint(1, pow(10, 30))
    key = DH(a, b)
    return key



def main():
        
    key_f = get_keys()
    key_g = get_keys()
    key_h = get_keys()
    f = open('A.txt', 'w+')  # 输出到 A应该有的密钥文件
    print(key_h, file=f, end='\n')
    print(key_f, file=f, end='\n')
    f.close()

    f = open('B.txt', 'w+')  # 输出到 B应该有的密钥文件
    print(key_f, file=f, end='\n')
    print(key_g, file=f, end='\n')
    f.close()

    f = open('C.txt', 'w+')  # 输出到 C应该有的密钥文件
    print(key_h, file=f, end='\n')
    print(key_g, file=f, end='\n')
    f.close()
