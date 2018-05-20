# coding: utf-8
print('Hello World')
print(type(5))
print(type('Bijit'))
print(type(True))
print(type(3.14))
x=1
y=x
y=2
print(x)
print(y)
x=[]
y=x
y.append(2)
print(x)
print(y)
#this is a comment
repr(x)
id(x)
x=1
y=x
x=1
id(x)
y=x
id(y)
y=10
id(x)
id(y)
# get_ipython().magic('save PythonDatatypes01 1-100')


n='my name is Bijit'
print(n.upper())
print(n.lower())
print(len(n))
print(n.split())
print(n.replace('Bijit','joydeep'))
print(n+"God Morning!")
print(n.index('name'))
print(n[n.index('name'):n.index('name')+4])
print('Bijit' in n)
print('Joydeep' in n)

