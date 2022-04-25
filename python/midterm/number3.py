



def A(a,b):
    result = int(a+b)
    return result

def S(a,b):
    
    result = int(a-b)
    return result

def M(a,b):
    
    result = int(a*b)
    return result

def D(a,b):
    
    result = int(a/b)
    return result

select = input()
a,b = input().split()
a = int(a)
b = int(b)

if select == 'A':
        print(A(a,b))
elif select == 'S':
        print(S(a,b))  
elif select == 'M':
        print(M(a,b))
elif select == 'D':
        print(D(a,b))                   
        