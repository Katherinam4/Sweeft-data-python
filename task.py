# exercise1
# from collections import Counter
#
# N = int(input())
# LIST = []
#
# for i in range(N):
#     LIST.append(input().strip())
#
# COUNT = Counter(LIST)
#
# print(len(COUNT))
# print(*COUNT.values())


# exercise2
# def biggerIsGreater(w):
#     arr = list(w)
#
#     i = len(arr) - 1
#     while i > 0 and arr[i - 1] >= arr[i]:
#         i -= 1
#
#     if i <= 0:
#         return "no answer"
#
#     j = len(arr) - 1
#     while arr[j] <= arr[i - 1]:
#         j -= 1
#     arr[i - 1], arr[j] = arr[j], arr[i - 1]
#
#     arr[i:] = arr[len(arr) - 1: i - 1: -1]
#     return "".join(arr)
#
#
# for _ in range(int(input())):
#     print(biggerIsGreater(input()))
