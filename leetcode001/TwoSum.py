class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_length = len(nums)

        if list_length <= 1:
            return False
        for i in range(list_length):
            if target - nums[i] in nums[i + 1:]:
                return [i, nums.index(target - nums[i], i + 1)]


s = Solution()
nums = [2, 7, 11, 15]
result = s.twoSum(nums, target=9)
print(result)