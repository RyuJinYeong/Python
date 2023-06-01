def fc(temper,action):
    if(action==1):
        tmp=(temper-32)/1.8
        tmpact="F2C"
    else:
        tmp=temper*1.8+32
        tmpact="C2F"
    return (tmp,tmpact)


t=int(input("온도 :"))
a=int(input("0:C2F, 1:F2C :"))

(rt,ra)=fc(t,a)

print(ra,":",t," => ",rt)

