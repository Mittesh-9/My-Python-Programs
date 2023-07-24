a = [2,3,4,6,8]
# b = []

# if __name__ == '__main__':
#     # n = int(input())
#     # arr = map(int, input().split())
#     # a = max(arr)-1
#     # print(a)
#     for i in a:
#         if i <= max(a) - 1:
#             b.append(i)

# print(b[-1])

# a = [1 ,-1 ,-2 ,-1]
# b = print(sorted(a))

# print(min(a) + 1)

# for i in a:
#     if i > 0:
#         print(max(a) - 1)
#         break
#     elif i < 0:
#         print(min(a) + 1)
#         break

b = list(set(a))
if len(b) >= 2:
    b.sort()
    second_max = b[-2]
    print(second_max)