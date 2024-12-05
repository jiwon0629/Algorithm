# 별찍기 피라미드
# 입력
print("밑변의 별 길이 : ",end="")
num = int(input())

# 별 찍기
for i in range (0,num,2):
    print(" "*int((num-(i+1))/2)+"*"*(i+1))