# FIFO

# 입력
print("입력할 값의 개수 : ", end="")
num = int(input())

# 배열 선언
arr = [0] * num

# 값 배열 입력
for i in range (num) : 
    print(i+1 ,"번째 값 입력 : ", end="")
    arr[i] = int(input())
print(" ")

# 입력 값 출력
print("<입력한 값 정렬>")
for b in range (num) :
        print(arr[b], end=" ")
print("")

# 값 밀어내기
for i in range (num) :
    print("")
    print(i+1 ,"번째 변화")
    
    # n+1번째 값이 n번째 값이 된다.
    # num값보다 수가 크게 되면 배열의 범위가 벗어난다. 
    for c in range (num) :
        if(c==num-1) : 
             arr[num-1]=0
             break
        else : 
           arr[c] = arr[c+1]
    
    # 결과 값 출력
    for d in range (num) : 
        print(arr[d], end = " ")
    print(" ")