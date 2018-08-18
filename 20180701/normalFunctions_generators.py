
def oddeven(myList):

    for elem in myList:
        if elem%2==0:
            yield 'e'
        else:
            yield 'o'
    
print('I am inside prod code')
print(__name__)

if __name__ == '__main__':
    m=oddeven([1,2,3,4])
    print(m)