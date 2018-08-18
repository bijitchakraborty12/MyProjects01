
with open('C:\\Python Practice\\MyProjects01\\MyProjects01\\20180707\\Commands_List.txt','r') as fl:
    p=fl.readlines()

l=[]
for k in p:
    #print(k)
    j=k.strip().split(' ') # default is space as an argument to split()... strip() is python quivalent of CLEAN() in Excel...
    if j[0]=='insert':
        # print("~~~~~~~~~~~~~")
        # print(j)
        # print()
        # print()
        # print()
        # print("~~~~~~~~~~~~~")    
        l.insert(int(j[1]),int(j[2]))
    elif j[0]=='print':
        print(l)
    elif j[0]=='remove':
        l.remove(int(j[1]))
    elif j[0]=='append':
        l.append(int(j[1]))
    elif j[0]=='sort':
        l.sort()            
    elif j[0]=='pop':
        l.pop()
    elif j[0]=='reverse':
        l.reverse()
        