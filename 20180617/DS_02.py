x={}

for i in range(5,15): # in range function, last value is n-1 and NOT n...
    x["item_"+str(i)]=int(i)*2

for k,v in x.items():
    print(k+":"+str(v))

print(x)
print(x.keys())
print(x.values())
