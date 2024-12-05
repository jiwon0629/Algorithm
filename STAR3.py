# 별찍기 삼각형
# 입력
print("높이의 별 길이 : ",end="")
num = int(input())

# 별 찍기
for i in range (0, num) : 
    print("*" * (i+1))
for i in range (num-1, 0, -1):
    print("*" * i)