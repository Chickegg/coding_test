# 백준 1000

# A+B 출력 Program

# a, b= map(int, input().split())
# c = a + b
# print(c)

# 입력값이 많은 경우 시간 단축방법한 코드

# # 1번
# import sys
# N = int(sys.stdin.readline())
# sys.stdout.write(N)

# print(N)
# # 2번

# from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write

# #결과

# N = int(sys.input)
# sys.print(N)

# 2. 배열 입력

#Bad Code
# MAP = []
# for i in range(int(input())):
#     inputStr = input()
#     arr = list(inputStr)
#     MAP.append(arr)


# Map = [list(map(int, input().split())) for _ in range(int(input()))]


# Map1 = sum(Map)
# print(Map1)

#Good code

# Map = [list(map(int, input().split())) for _ in range(int(input()))]
# print(Map)


# MAP = [list(map(int, input().split())) for _ in range(int(input()))]
# print(MAP)
# 9613 문제

# 3 케이스의 갯수
# 4 10 20 30 40            4 개 10 20 30 40 
# 3 7 5 12                 3개 7 5 12
# 3 125 15 25              3 개 125 15 25

# N, *arr = map(int, input().split()) # *변수는 뒤에 입력값들이 배열로 저장된다.

# for i in N, arr:
#     print(N, arr)

# N, *arr = map(int, input().split())
# print(N, arr)
# print(sum(arr))
# print(type(sum(arr)))
# for i in range(len(N)) :
#     print(i)

# A = [list(map(int, input().split())) for _ in range(int(input()))]
# print(A)
# print(type(A))


# 문자열을 한 글자씩 배열에 저장
# bad code

# N =[]
# arr = [input() for _ in range(N)]
# print(arr)

# arr = [list(map(int,input())) for _ in range(3)]
# print("".join(map(str, arr)))

# a = list(map(int, input().split()))
# print(a) 
# print("".join(map(str, a))) # 연결해서 출력
# print(*a) # [ 와 , 을 없애고 출력


# A = [list(map(int, input().split())) for _ in range(int(input()))]
# # for i in --- :
# #     print(i)
# print(type(A))
# # A_SUM = sum(A)
# # print(A_SUM)
# B = sum(A)
# # sum(a) # 리스트요소들의 합


# n = int(input()) # 젤 느린 입력값 

from sys import stdin
# n = int(stdin.readline()) # 빠른입력값

li = list(map(int, stdin.readline().split())) # 값이 여러개 input 보다 readline이 빠르다.

# 뒤에 .split()까지 사용하면 아예list로 받을 수 있고 map함수를 이용해 int 값으로 저장할수있다.



# 입력값이 여러개라면?
n, m = list(map(int, stdin))


# import sys 
# N = int(sys.input())
# sys.print(N)

# from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write


