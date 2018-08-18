
def oddeven(myList):
    mapping=[]

    for elem in myList:
        if elem%2==0:
            mapping.append('e')
        else:
            mapping.append('o')
    return mapping
    
print('I am inside prod code')
print(__name__)

if __name__ == '__main__':
    m=oddeven([1,2,3,4])
    print(m)