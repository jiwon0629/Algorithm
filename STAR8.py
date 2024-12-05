# 별찍기 마르모
# 입력
print("별 길이 : ",end="")
num = int(input())

for i in range(1, num+1, 2) :
      print(" "*(num-i//2) + "*"*i)

for i in range(num-2, 0, -2) :
      print(" "*(num-i//2) + "*"*i)
