def primefactors(n):
    factors=[]
    i=2
    while i*i<=n:
        factors.append(i)
        n//=i
    i+=1
    if n>1:
        factors.append(n)
    return factors

a=int(input("enter first number"))
b=int(input("enter second number"))

factors_a=primefactors(a)
factors_b=primefactors(b)

common=[]
for x in factors_a:
    if x in factors_b:
        common.append(x)
        factors_b.remove(x)

gcd=1
for x in common:
    gcd=x

print("primefactors of",a,":",primefactors(a))
print("primefactors of",b,":",primefactors(b))


print("gcd is :",gcd)