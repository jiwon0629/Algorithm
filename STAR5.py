# 별찍기 직각 역삼각형
# 입력
print("밑변의 별 길이 : ",end="")
num = int(input())

# 별 찍기
for i in range (num, 0, -1):
    print(" "*(num-i)+"*"*i)