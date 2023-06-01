s=0
n=0
for i in range(1,101):
    if i%2==1:
        s=s+i
    if i%2==0:
        n=n+i
print("홀수 합 :",s)
print("짝수 합 :",n)
