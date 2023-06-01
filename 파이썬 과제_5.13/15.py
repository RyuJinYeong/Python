mm=1
n=1
while True:
    mm*=2
    print(n,"번 접으면",mm,"mm")
    if(mm>=100000):
        break
    n+=1

print("횟수 :",n,"두께 :",mm)
