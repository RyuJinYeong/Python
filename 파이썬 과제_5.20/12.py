def vsum(*num):
    sum=0
    for i in num :
        sum=sum+i
    return sum

n=vsum(2, 3)
print("2+3=",n)

n=vsum(2,3,4)
print("2+3+4=",n)

n=vsum(2,3,4,5)
print("2+3+4+5=",n)
