def gcd(m,n):
    while n!=0:
        r=m%n
        m=n
        n=r
        return m
    
a=int(input("enter first number"))
b=int(input("enter second number"))

print("gcd is :",gcd(a,b))
    