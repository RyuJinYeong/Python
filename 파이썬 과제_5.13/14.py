sum=0
while True:
    n=int(input("정수 : "))

    if(n>0):
        sum+=n
    elif(n==0):
        break
print("합 :",sum)
