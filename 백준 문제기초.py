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




people_nums = []
people = 0

for _ in range(10) :
    out_num, in_num = map(int, input().split())
    people += in_num
    people -= out_num

    people_nums.append(people)

print(max(people_nums))


