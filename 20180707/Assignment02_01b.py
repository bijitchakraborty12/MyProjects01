
def openFile(flName):
    with open(flName,'r') as fl: # 'r' is the default mode, need not be explicitly mentioned...
        p=fl.readlines()
    return p

def processCommands(p):
    l=[]
    for k in p:
        #print(k)
        j=k.strip().split(' ') # default is space as an argument to split()... strip() is python quivalent of CLEAN() in Excel...
        if j[0]=='insert':
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

    return l
            
def main():
    p=openFile('C:\\Python Practice\\MyProjects01\\MyProjects01\\20180707\\Commands_List.txt')
    processCommands(p)

if __name__ == '__main__':
    main()