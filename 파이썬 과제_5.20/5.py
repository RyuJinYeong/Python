def welcome(name,msg="환영합니다."):
    print(msg+name+"님")

n=input("이름 :")
msg=input("환영메세지:")
if(msg==""):
    welcome(n)
else :
    welcome(n,msg)
