#!/usr/bin/env python
# coding: utf-8

# In[21]:


print("----Calculadora----")
print("Ingrese el primer numero: ")
a=int(input())
print("Ingrese el primer numero: ")
b=int(input())
print("La suma es ",suma(a,b))
print("La resta es ",resta(a,b))
print("La multiplicacion es ",multi(a,b))
print("La division es ",division(a,b))


# In[19]:


def suma(a,b):
    return (a+b)
def resta(a,b):
    return (a-b)
def multi(a,b):
    return (a*b)
def division(a,b):
    return (a/b)

