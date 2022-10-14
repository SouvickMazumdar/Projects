# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 00:12:57 2022

@author: Souvick
"""

import random
t=[]
T=[]
X=[]
n=[]
a=[]
for i in range(1,100):
    t.append(i)
for i in range(1,1000):
    T.append(i)
    
for i in range(1,1000):
    X.append(i)

for i in range(1,1000):
    n.append(i)
    
for i in range(1,1000):
    a.append(i)
    
file=open('test_case2.txt','w')
g=random.choice(t)
file.write(str(g))
file.write("\n")

file=open('test_case2.txt','a')
print(g)
for i in range(g):
    T_k=random.choice(T)
    X_k=random.choice(X)
    n_k=random.choice(n)
    file.write(str(T_k))
    file.write(" ")
    file.write(str(X_k))
    file.write(" ")
    file.write(str(n_k))
    file.write("\n")
    print(T_k,X_k,n_k)
    ans_r=[]
    for j in range(n_k):
        v=random.choice(a)
        ans_r.append(v)
        file.write(str(v))
        file.write(" ")
    file.write("\n")
    print(ans_r)
file.close()
        


   