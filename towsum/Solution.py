# -*- coding:utf-8 -*-
__author__ = "ethan"

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
#    Given nums = [2, 7, 11, 15], target = 9,
#    Because nums[0] + nums[1] = 2 + 7 = 9,
#    return [0, 1].
import time

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(0, len(nums)):
            x = nums[i]
            if target-x in nums_dict:
                return [nums_dict[target-x], i]
            nums_dict[x] = i

            
if __name__ == "__main__":
    s = Solution()
    
    test_nums = [3, 2, 4, 7, 13]
    target = 17

    start = time.time()
    ret = s.twoSum(test_nums, target)
    end = time.time()

    print("nums: %s, target:%d" % (test_nums, target))
    print("answer: %s" % ret)
    print("run time: %s" % (end-start))
