def pzn(num):
    if(num>0):
        r=1
    elif(num<0):
        r=-1
    else:
        r=0
         
    return r


while True:
    n=int(input("정수 :"))
    r=pzn(n)

    if(r==1):
        print("양수")
    elif(r==-1):
        print("음수")
    else:
        print("0")
        break
