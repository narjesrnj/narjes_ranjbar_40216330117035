# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HJPSizfkY-Yz9BMCCIP7pu_cV5fKbySG
"""

def b_sort (k = [], s):
    if k is not None:
        for i in range (s-1):
            for j in range (s-1-i):
                if k[j] > k[j+1]:
                    temp = k[j]
                    k[j] = k[j+1]
                    k[j+1] = temp
        return k

def mean_new ():
    k = []
    i = 0
    counter = 0

    while i != 1000:

        if i == 1000:
            break

        i = int (input ())
        k.append (i)
        counter += 1
        return k, counter

L, S = mean_new ()
if b_sort (L, S):
    print (L)
else:
    print ('is empty')