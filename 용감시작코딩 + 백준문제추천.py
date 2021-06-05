# 덱 
# 덱은 데크라고도 하며 double-ended queue의 약자입니다. 선입선출의 개념인 FIFO와 더불어
# 나중에 온값을 먼저 처리하는 LIFO 연산도 가능합니다. 즉 양방향에서 데이터를 처리할 수있다.
# 스택문제를 풀때는 deque를 사용해야한다.

# from collections import deque
# deq = deque() # 덱 초기화
# deq = deque([i for i in range(1, 5)]) # 덱의 1~4까지 저장
# deq.appendleft(10) # 덱의 왼쪽에 저장 
# deq.append(-10) #덱의 오른쪽에 저장
# deq.pop() # 덱이 오른쪽에서 값을 제거후 리턴한ㄷ다.
# deq.popleft() # 왼쪽에서 제거한다.

# print(deq) # 길이구하기

# print(deq) 

# #덱을 회전하는 방법
# deq.rotate(-1)
# print(deq)

## 기본문제 ###
# from collections import deque
# deq = deque()
# N = int(input())
# deq = deque([i for i in range(1, N + 1)])

# for _ in range(N-1):

#     deq.popleft()
#     deq.rotate(-1)

# print(deq[0])

# 
###################### 10828 스택 ############################

# from collections import deque
# import sys

# N = int(sys.stdin.readline())
# deq = deque()


# def empty() :
#     if len(deq) == 0 :
#         return 1
#     else :
#         return 0

# def size():
#     return len(deq)

# for i in range(N):
#     cmd = list(sys.stdin.readline().split())

#     if cmd[0] == 'push' :
#         deq.append(cmd[1])
#     elif cmd[0] == 'top' :
#         if empty() == 1 :
#             print(-1)
#         else :
#             print(deq[-1])
#     elif cmd[0] == 'pop' :
#         if empty() == 1:
#             print(-1)
#         else :    
#             print(deq.pop())
    
#     elif cmd[0] == 'empty' :
#         print(empty())
#     elif cmd[0] == 'size' :
#         print(size())




# from collections import deque
# import sys
# deq = deque()
# N = int(sys.stdin.readline())
# def empty():
#     if len(deq) == 0 :
#         return 1
#     else :
#         return 0
# def size():
#     return len(deq)

# for i in range(N) :
#     cmd = list(sys.stdin.readline().split())

#     if cmd[0] == 'push_front' :
#         deq.appendleft(cmd[1])
#     elif cmd[0] == 'push_back' :
#         deq.append(cmd[1])
#     elif cmd[0] == 'pop_front' :
#         if empty() == 1:
#             print("-1")
#         else :
#             tmp = deq.popleft()
#             print(tmp)
#     elif cmd[0] == 'pop_back' :
#         if empty() == 1:
#             print("-1")
#         else : 
#             tmp = deq.pop()
#             print(tmp)
#     elif cmd[0] == 'front' :
#         if empty() == 1 :
#             print("-1")
#         else :
#             print(deq[0])
#     elif cmd[0] == 'back' :
#         if empty() == 1 :
#             print("-1")
#         else :
#             print(deq[-1])
    
#     elif cmd[0] == 'size' :
#         print(size())
#     elif cmd[0] == 'empty' :
#         print(empty())

## 우선 순위 큐 

# from queue import PriorityQueue
# que = PriorityQueue() # 우선순위큐

# que.put(4)
# que.put(10)
# que.put(2)

# for i in range(len(que.queue)):
#     # print(i)
#     print(que.queue[i], end=" ")

# que.get() # 우선순위 큐에 저장된 값을 제거. 리턴받고 왼쪽부터 제거된다.

### 덤
#문제를 풀다보면 실행시간을 알고 싶을 때가 있습니다. 이럴 때 다음과 같이 구현해 주세요.

# import time
# def some_func() : 

#     start_time = int(round(time.time() * 1000))
#     end_time = int(round(time.time() * 1000))
    
#     return print('some_func()의 실행 시간 : %d(ms' % (end_time - start_time))

# from queue import PriorityQueue
# que = PriorityQueue() # 우선순위큐

# que.put(4)
# que.put(10)
# que.put(2)

# for i in range(len(que.queue)):
#     # print(i)
#     print(que.queue[i], end=" ")

# print(some_func())

### ### 실버 5 N번째 큰수 ### ###

# import sys
# ROW = range(int(sys.stdin.readline()))

# # board = [[0 for i in range(10)] for j in range(ROW)]
# # for i in range(ROW) :

# li = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(ROW)]

# for i in ROW :
#     li[i].sort()
#     print(li[i][-3])

# import time

# start_time = int(round(time.time() * 1000))
# end_time = int(round(time.time() * 1000))
    
# print('some_func()의 실행 시간 : %d(ms' % (end_time - start_time))

########### 소수 찾기 ############

# n = 100

# def isPrime(a):
#     if (a<2) :
#         return False
#     for i in range(2, a):
#         if (a % i == 0) :
#             return False
#     return True

# for i in range(n+1):
#     if(isPrime(i)):
#         print(i)

##소수의 정의에 충실한 방법 ##

## 에라토스테네스의 체 ##
# 효율적인 방법
# 1. 1은 제거한다.
# 2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.
# 3. 나머지 3의 배수를 모두 지운다.
# 4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다.
# 5. 반복

## 찾고자 하는 수(n) 까지 True로 채운 리스트를 생성 한 후 2를 제외한 2의배수, 3을 제외한 3의배수,
## 5를 제외한, 5의배수, 7을 제외한 7의배수,....sqrt(n)의 배수는 모두 False로 바꾼다.
## 결국, 2~n까지 숫자들 중 True인 숫자들이 소수가 된다.

### code ####

# import sys

# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True설정(소수로 간주)
#     sieve = [True] * n

#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)
#     m = int(n ** 0.5)
#     for i in range(2, m + 1) :
#         if sieve[i] == True:  # i가 소수인 경우라면?
#             for j in range(i+i, n, i): # i 이후 i의 배수들을 False 판정해준다.
#                 sieve[j] = False
    
#     # 소수 목록 산축
#     return [ i for i in range(2, n) if sieve[i] == True]

# N = int(sys.stdin.readline())

# li1 = set(prime_list(1000))
# li2 = set(list(map(int, sys.stdin.readline().rsplit())))
# li3 = len(list(li1 & li2))

# print(li3)


#### 쉽게 푸는 문제 ####

# '1' * 1 , '2' * 2 ,'3' * 3 ,,,,,, n 이 되면 합을구한다.

# # 3 7 을 입력 1, 2, 2, 3, 3, 3, 4, 4, 4, 4
# import sys
# a, b = map(int, sys.stdin.readline().rsplit())
# # section = [[i]* i for i in range(1, 46)]
# # section = [0] + sum(section, [])
# # print(sum(section[a:b+1]))

# section = [[i] * i for i in range(1, 46)]
# section = [0] + sum(section, [])
# print(section)
# print(sum(section[a:b+1]))

## 풀이 2번 ##

# import sys
# a, b = map(int, sys.stdin.readline().rsplit())

# res, curr, cnt = 0, 1, 1

# for i in range(1, b+1):
#     if i >= a:
#         res += curr
#         # print(res)
#     if cnt >= curr:
#         cnt = 0
#         curr += 1
#         # print(cnt)
#         # print(curr)
#     cnt += 1
# #     print(cnt)
# print(res)

# # print(res)

############### 튼튼한 기본기
import sys

# M = int(sys.stdin.readline())
# N = int(sys.stdin.readline())

def prime_list(n) :
    sieve = [True] * n

    m = int(n ** 0.5) # n의 최대 약수가 sqrt(n) 이하이므로 i-sqrt(n)
    for i in range(2, m + 1) :
        if sieve[i] == True :
            for j in range(i+i, n, i) : # i 이후 i 의 배수들을 False 판정해준다.
                sieve[j] == False
    
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

print(prime_list(100))



# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True설정(소수로 간주)
#     sieve = [True] * n

#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)
#     m = int(n ** 0.5)
#     for i in range(2, m + 1) :
#         if sieve[i] == True:  # i가 소수인 경우라면?
#             for j in range(i+i, n, i): # i 이후 i의 배수들을 False 판정해준다.
#                 sieve[j] = False
    
#     # 소수 목록 산축
#     return [ i for i in range(2, n) if sieve[i] == True]

# N = int(sys.stdin.readline())

# li1 = set(prime_list(1000))
# li2 = set(list(map(int, sys.stdin.readline().rsplit())))
# li3 = len(list(li1 & li2))

# print(li3)