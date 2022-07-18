#!/usr/bin/env python
# coding: utf-8

# In[1]:


def checkIfNotNumeric(*args):
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True

def checkIfNotNumericList(L):
    for x in L:
        if not(isinstance(x,(int,float))):
            return False
    return True

def swapValues(L,idx1,idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L

def addAllNumerics(*args): #sum
    s= 0
    for x in args:
        s+=x
    return s

def findMin(L,startIndx): 
    m = L[startIndx] #zero
    idx = startIndx
    for i in range(startIndx,len(L)):
        x = L[i] #zero
        if x<m:
            m = x
            idx = i #idx from for for
        else:
            pass
    return m,idx

def myName()
print( "Franco Ortiz")

