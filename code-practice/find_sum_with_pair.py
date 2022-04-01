arr = [6,6,4,3,2,1,7]
sum = 9

# Brute Force - O(n^2)
# def hasPairWithSum(arr, sum):
#     for i in range(0, len(arr)):
#         for j in range(1, len(arr)):
#             if i + j == sum:
#                 return True
#     return False
            
# O(n)
# def hasPairWithSum(arr, sum):
#     myset = set()
#     for num in arr:
#         if num in myset:
#             return True
#         else:
#             myset.add(sum-num)
#     return False
# print(hasPairWithSum(arr, sum))
