####### 1. 순열, 조합 ######
# N = int(input())
# for i in range(0, N-1) :
#     for j in range(i+1, N) :
#         print(i, j)

# for _ in range(input()) :

### 쉽게 하는 법 ####

# from itertools import combinations
# print(list(combinations([1, 2, 3, 4], 3)))

# # print(list(combinations([0, 1, 2, 3], 2)))

# from itertools import combinations
# import sys
# N, M = map(int, sys.stdin.readline(). rsplit())
# arr = [str(i+1) for i in range(N)] # 1부터 N까지의 수를 저장

# for e in list(combinations(arr, M)):
#     print(" ".join(e))

### 순열 ###

# 1 ~ N까지의 자연수 중에서 중복 없이 M개를 고른 수열
# import sys
# from itertools import permutations

# N, M = map(int, sys.stdin.readline(). rsplit())
# arr = [str(i+1) for i in range(N)]

# for e in list(permutations(arr, M)):
#     print(" ".join(e))

## permutations 중복이 없는 수열 ##
## product ## 중복이 있는 수열
## 중복 조합 combinations_with_replacement

##### 2. 빈도 계산 #### (Counter)

# import sys
# from collections import Counter

# N = [int(input()) for _ in range(10)]
# val = Counter(N).most_common()
# print(sum(N) // 10)
# print(val[0][0])

## 가장 많이 나오는 단어는?

# from collections import Counter
# import sys

# N = str(sys.stdin.readline().strip())
# N = N.upper()
# arr = Counter(N).most_common()

# if len(arr) >=2 and arr[0][1] == arr[1][1] :
#         print('?')
# else :
#     print(arr[0][0])


### 3 힙
### 3-1 최소힙, 최대힙

import sys, heapq
heap = []

# for i in range(int(sys.stdin.readline())) :
#     N = int(sys.stdin.readline()) * -1
# if N == 0 :
#     if len(heap) == 0:
#         print(0)
#     else :
#         print(heapq.heappop(heap) * -1)
# else :
#     heapq.heappush(heap, N)

for i in range(int(sys.stdin.readline())) :
    N = int(sys.stdin.readline())
if N == 0:
    print