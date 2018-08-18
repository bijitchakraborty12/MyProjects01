
## All types of DS are preaseable i,e., convertable to each other, as these are functions in themselves too.

# converting a list into a set...
x=[1,2,3,4,5,3,2,7,1]
print(x)
y=set(x)
print(y) 

# converting a set into a list...
x={4,3,2,6,7}
print(x)
y=list(x)
print(y)

# converting a touple into a set...
x=(1,2,3,4,5)
print(x)
y=set(x)
print(y)
z=list(x)
print(z)

# converting into a Dictionary...
x=[[1,2],(3,4)]
print(x)
y=dict(x)
print(y)

x=[1,2]
y=("Bijit","Sujit")
z=dict(zip(x,y))
print(z)
k={3:'Chetan',4:"Bhagat"}
z.update(k)
print(z)
del z[3] # you define a disctionary with {}, but access it's items with []. But, this is not adviseable, as this is an EXPENSIVE operation...
print(z)
