def gcd(m,n):
    i=min(m,n)
    while i>0:
        if m%1==0 and n%1==0:
            return i 
        i-=1
a=int(input("enter first number"))
b=int(input("enter second number"))

print("gcd is :",gcd(a,b))