import sys
max=-sys.maxsize - 1
min=sys.maxsize
for num in [8,7,3,2,9,4,1,6,5]:
    if(min>num):
        min=num
    if(max<num):
        max=num

print("최댓값 :",max)
print("최솟값 :",min)
