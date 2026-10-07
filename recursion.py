'''def sum(num):
    n=0
    for i in range(num+1):
        n=n+i
    return n
print(sum(5))
'''

def sum(num):
    if num==0:
        return num
    else:
        return num+sum(num-1)
print(sum(5))

def factorial(n):
    if n == 1 or n==0:
        return 1
    else:
        return n*(factorial(n-1))
print(factorial(54))

'''def factorial(n):
    t=1
    for i in range(1,n+1):
        t=t*i
    return t
print(factorial(5))'''