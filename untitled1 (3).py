# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HJPSizfkY-Yz9BMCCIP7pu_cV5fKbySG
"""

def maximum100():
   a=input()
   a=int(a)
   max=a
   for i in range(99):
      a=int(input())
      if a>max:
         max=a
         return max