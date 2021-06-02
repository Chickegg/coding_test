# 최소, 최대 

# N = [list(map(int,input().split())) for _ in range(int(input()))]

# def min_max() :


#     N = int(input())
#     M = list(map(int, input().split()))
#     li = []
#     li.append(min(M))
#     li.append(max(M))

#     return li

# print(*min_max())

# 지능형 기차 #

# people_nums = []
# people = 0

# for _ in range(10) :
#     out_num, in_num = map(int, input().split())
#     people += in_num
#     people -= out_num

#     people_nums.append(people)

# print(max(people_nums))



## 피보나치 수 5 ##

# N = int(input())
# li = [0, 1]

# for i in range(1, N) :
#     if i == 1 :
#         li.append(li[0]+li[i])
#     else :
#         li.append(li[i-1] + li[i])


# print(li[N])

### 일곱 난쟁이 ###

# from sys import stdin

# list = [int(stdin.readline()) for _ in range(9)]
# total = sum(list)

# for i in range(9) :
#     for j in range(i+1, 9):
#         if 100 == total - (list[i] + list[j]) :
#             joker1, joker2 = list[i], list[j]
#             list.remove(joker1)
#             list.remove(joker2)
#             list.sort()
        

#             break
    
#     if len(list) < 9 :
#         break
            
# for i in range(len(list)) :
#     print(list[i])


### 최대 공약수, 최소 공배수 ### 
# math 라이브러리를 사용하면 매우 쉽다.

import sys
# import math

# A, B = map(int, sys.stdin.readline(). rsplit())
# gcd = math.gcd(A, B)
# lcm = math.lcm(A, B)

# print(gcd)
# print(lcm)

### N 번째 큰수 ###
arr = range(int(input()))

N = [list(map(int, sys.stdin.readline().rsplit())) for _ in arr ]

for i in arr :
    N[i].sort()
    print(N[i][-3])

