#1. 입력을 받을때는
# n = int(input())
#보다는
# from sys import stdin
# n = int(stdin.readline())
# # 빠르다.
# # 한 줄에 여러개인 경우 많이 빠르다.
# li = list(map(int, stdin.readline().split()))
# 뒤에 .split까지 할 경우 바로 리스트로 저장가능하다.


# 3 3
# 1 1 0
# 1 1 1
# 1 0 1
# 1 1 1
# 만일 입력값이 라면 이 코드로 입력 받을 수 있다.
# from sys import stdin

# n, m = list(map(int, stdin.readline().split()))
# # li = [] 

# for i in range(n+1):
#     li.append(list(map(int, stdin.readline().split())))

# print(li)

# 한 줄에 한개의 데이터만 주어진다면?
# 리스트를 먼저 초기화 해주고 인덱스로 접근해서 저장하자.

from sys import stdin
n = int(input())

li =[0] * n
for i in range(n):
    li[i] = int(stdin.readline())
    print(li)
