# class Solution:
#     def twoSum(self, nums: List[int], target: int):
#         for v in range(0, len(nums)):
#             if (nums[v] + nums[v + 1] == target):
#                 return [v, v+1]
#             return null

# class Solution:
#     def twoSum(nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         h = {}
#         for i, num in enumerate(nums):
#             n = target - num
#             if n not in h:
#                 h[num] = i
#             else:
#                 return [h[n], i]

#     john = twoSum(nums=[1, 2, 3, 4, 5, 6], target=5)

#     print(john)
