# Author: Zhengqi Dong
# Date: 6/20/2021
# Tag: Array, Sorting, Two_pointers
# Category: Easy_Level_Coding_Question
# Title: LeetCode Question: 283. Move Zeroes
# Question: https://leetcode-cn.com/problems/move-zeroes/
# Solution: 

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Method 1: with extra space
        Cost: Time: O(len(nums)), Space: O(len（nums)
        make a copy of nums, and use one pointer traverse over the original list(named i), and two pointer start from the two end-point of copied list (named p1, and p2), and heading to middle. In origianl list, for anything that's not zero, put it up front of copied list, and advanced p1. Otherwise, put to the end, and reduce p2.

        Method 2: In place
        Cost: Time: O(len(nums)), Space: O(len（nums)
        Idea:
            主题思路：
                - 什么时候要呢？==》非零就要
                - 是否可以覆盖呢？==》可以，因为array is sorted, and n is always >= i.
                - Edge case: 因为题目要求0都要放到最后，但我们之前都跳过了，所以在最后要有个补零的操作
        Implementation: 
            Use two pointer (named n and i). i will traverse over the nums, and n will keep trace of the last valid elements. If i points to an non-zero elements, count it valid, otherwise, do nothing.

        [1,3,12,0,12]
                 i
        n
        """
        n = 0   # 跟踪最后一个valid的数。 
        for i in range(len(nums)):
            if nums[i] != 0: # 第一个肯定要。
                nums[n] = nums[i]
                n += 1
        while n < len(nums):
            nums[n] = 0
            n+=1




if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Output = [1,3,12,0,0]
    Solution.merge3(..., nums) # ... means ignore the self argument