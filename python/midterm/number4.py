
def factorial(k):
    fact = 1
    for i in range(1,k+1):
        fact *= i
    return fact    
def permutation(n,r):
    return factorial(n) / factorial(n-r)


n,r = input().split()
n = int(n)
r = int(r)    
print("n's value:",n)
print("r's value:",r)
print('Result of Permutation:',permutation(n,r))    