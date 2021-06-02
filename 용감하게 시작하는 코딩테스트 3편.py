############ 1. 순열, 조합 ##############

# 1 - 1 순수한 방법
# for 문 2개 사용해서 nC2 구하기

# N = int(input())

# for i in range(0, N-1):
#     for j in range(i+1, N):
#         print(i, j)

# 1 - 2 itertools을 사용한 조합
from itertools import combinations

N , M = list(map(int, input().split()))
arr = [str(i+1) for i in range(N)]

print(arr)

for e in list(combinations(arr, M)):
    print(" ".join(e))

# for e in list(combinations(arr, M)):
#     print(" ".join(e))






