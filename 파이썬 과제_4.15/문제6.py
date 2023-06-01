a,b,c=3,2,4

print("a =",a," b =",b," c =",c)

a+=b
print("(a=a+b) == (a+=b) -> a =",a)

a,b,c=3,2,4
a*=b
print("(a=a*b) == (a*=b) -> a =",a)

a,b,c=3,2,4
a*=(b+c)
print("(a=a*(b+c) == (a*=(b+c)) -> a =",a)

a,b,c=3,2,4
a-=(b*c)
print("(a=a-b*c) == (a-=(b*c)) -> a =",a)



