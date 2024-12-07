# 제0항을 0, 제1항을 1로 두고, 둘째 번 항부터는 바로 앞의 두 수를 더한 수로 놓는다. 
# 1번째 수를 1로, 2번째 수도 1로 놓고, 3번째 수부터는 바로 앞의 두 수를 더한 수로 정의하는 게 좀더 흔하게 알려져 있는 피보나치 수열이다.
# 1번째 값 입력
n1 = int(input("1번째 값 입력 : "))
# 2번째 값 입력
n2 = int(input("2번째 값 입력 : "))
# 배열의 길이 값 입력
len = int(input("마지막 순서 입력 : "))
arr = [0] * len
arr[0] = n1
arr[1] = n2
for i in range(len) : 
    if(i==len-3) : 
        arr[i+2] = arr[i] + arr[i + 1]
        break
    else : 
        arr[i + 2] = arr[i] + arr[i + 1]
# 배열 출력 
for a in range(len) : 
    print(arr[a])