def calc(num1,num2,act="+"):
    if(act=="+"):
        print(num1+num2)
    elif(act=="-"):
        print(num1-num2)
    elif(act=="*"):
        print(num1*num2)
    elif(act=="/"):
        print(num1/num2)
    else:
        print("잘못된 연산기호입니다.")
        
n1=int(input("정수1:"))
n2=int(input("정수2:"))

calc(n1,n2)
calc(n1,n2,"*")
calc(n1,n2,"^")
