# ### [[공부할 내용]] ###

# #[정수], [문자열], [배열 자료형]

# # 1 정수 최대 최소

# # 예제
# # 배열 arr 에 있는값을 for 문으로 순회한다.
# # ans 에 arr에 저장되어 있는 값 중 최소값이 저장되게 한다.
# # 그렇다면 첫번쨰 줄 ans 무엇을 저장해야 할까? 정답은 arr에 있는 최댓값보다 큰 수가 오게한다.

# # 이 경우 우아한 방법
# import sys
# ans = sys.maxsize # 이 경우에도 ans + 1 은 가능하다
# arr = [1, 2, 3]
# for num in arr :
#     if ans > num :
#         ans = num
# print(ans)

# # 진법
# #진법은 입사 코딩테스트에서 빈도가 떨어지지만 쉬운 문제로는 많이 나온다.

# # 2-1. 10진수 => 2, 8, 16진수 변환
# a = bin(42) # 2진수
# print(a)
# b = oct(42) # 8진수
# print(b)
# c = hex(42) # 16진수
# print(c)

# # 2-2. 2, 8, 16진수 -> 10진수 변환
# d = int('0o52', 8)
# print(d)

# # 2-3 진법 연산 예제 이진수 덧셈
# # 3
# # 1001101 10010
# # 1001001 11001
# # 10000111 1010110

# for _ in range(int(input())) :
#     A, B = map(int, input().split())
#     print(bin(A)+bin(B))

# 백준 11005 진법변환
# 10진법 수 n이 주어진다 이수를 b 진법으로 바꿔 출력하는 프로그램을 작성하시오.

# print()
# 10진수를 36진수까지 변환가능하게하는 변환기 #

## 1212번 8 진수 12진수
# 8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시b오

### 3-1 문자열을 거꾸로 ###

# alph = "ABCD"
# print(alph[::-1])

# word = input()
# print(word)
# print(type(word))

# if word == word[::-1]:
#     print(1)
# else:
#     print(0)

### 3-2 문자열 <--> 아스키코드 ###
# ord() 문자를 아스키코드로 변환
# chr() 아스키코드를 문자로 변환


### 4-1 배열 초기화 ###

# 3 5
# 3 = 배열의 가로크기 5 = 배열의 세로크기 
# 이것을 초기화된 상태로 만들어보자.

# N, M = map(int, input().split())
# arr = [[0] * N for _ in range(M)]

# # Tip 배열의 가로,세로를 N, M으로 설정한다.
# # i의 값을 이용할 필요가 없는 경우 _ 를 사용하기도 한다.

# print(arr)

# 4-2 배열의 원소를 거꾸로
# 배열의 원소를 거꾸로 하려면 reverse()를 사용하면 됩니다. 반환 값이 없으니 이점 유의!

# A = int(input())
# B = int(input())

# arr_B = [int(i) for i in str(B)]
# arr_B.reverse()

# for i in range(len(arr_B)):
#     print(A * arr_B[i])
# print(A * B)

# print(A)
# print(B)
# print(arr_B)

### 4-3 배열 원소 갯수 ###
# list.count(찾는 값)
# str.count(찾는 값)

## 백준 2490번 윷놀이 정답 코드 일분 ##


# arr = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# arr3 = list(map(int, input().split()))

# def check(arr):
#     num_of_zero = arr.count(0)
    
#     if num_of_zero == 0: # 모
#         print("E")
#     elif num_of_zero == 1: # 도
#         print("A")
#     elif num_of_zero == 2: # 개
#         print("B")
#     elif num_of_zero == 3: # 걸
#         print("C")
#     elif num_of_zero == 4: # 윷
#         print("D")

# for i in range(3):
#     arr = list(map(int, input().split()))
#     check(arr)

# print(check(arr))
# print(check(arr2))
# print(check(arr3))


# def check(arr):
#     num_of_zero = arr.count(0)

#     if num_of_zero == 0:
#         print("E")
#     elif num_of_zero == 4:
#         print("D")
#     elif num_of_zero == 3:
#         print("C")
#     elif num_of_zero == 2:
#         print("B")
#     elif num_of_zero == 1:
#         print("A")
 
# for _ in range(3):
#     arr = list(map(int, input().split()))
#     check(arr)

### 4-4 원소 중복 제거
# alpha = ["a", "b", "c", "d", "a", "b", "c", "d"]
# alpha = list(set(alpha)) # set(list) 중복없이 원소가 저장된다.
# print(alpha)

# lst = [[1,2], [1,2], [1]]
# print(list(set(map(tuple, lst)))) # 2차원리스트 중복제거

# arr.sort() 오름차순 정렬
# arr.sort(reverse=True) 내림차순 정렬

# 원소가 한개가 아닌 리스트라면?
# arr.sort(key=lambda x:(x[0], x[1]))

## 11650 좌표 정렬하기 ##

# arr = [] # 빈list
# for _ in range(int(input())):
#     arr.append(list(map(int, input().split())))

# arr.sort(key=lambda x:(x[0], x[1])) # x[0] (x 좌표)을 정렬하고, 
# # x[0]값이 같다면 x[1] (y좌표)을 기준으로 오름차순 정렬합니다.

# for e in arr:
#     print(str(e[0]) + " " + str(e[1]))

# print(arr)


# #### 국영수 백준 문제 ###
# N = int(input())

# score_list = []

# for i in range(N):
#     [name, kor, eng, math] = map(str, input().split())

#     score_list.append([name, int(kor), int(eng), int(math)])

# sorted_score_list = sorted(score_list, key=lambda x : (-x[1], x[2], -x[3], x[0]))

# print(sorted_score_list)

# for score in sorted_score_list:
#     print(score[0])


