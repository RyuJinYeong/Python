def pow_xy(x,y):
    sum=1
    for i in range(y) :
        sum=sum*x
    return sum

x=pow_xy(2,4)
print("3 * 2**4 + 5 = ",(3*x+5))
