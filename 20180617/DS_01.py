x=[11,12,13,14]
y=[50,60,70]
for i in range(1,10,2):
    x.append("Item# "+str(i))

for i in x:
     print(i) 

x.extend(y)
print(x)

x.append(y)
print(x)
x.remove(y)
print(x)

""" this is multiine comment operator...
for i in x:
    #if int(i.replace("Item# ",""))%2!=0:
    if(isinstance(i,str)==False):
        if(i%2==0):
          x.remove (i)
"""          
print(x)