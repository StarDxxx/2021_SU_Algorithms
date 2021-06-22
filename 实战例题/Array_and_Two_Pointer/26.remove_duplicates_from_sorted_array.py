# Author: Zhengqi Dong
# Date: 6/19/2021
# Tag: Array, Sorting, Two_pointers
# Question: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
# Solution: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shuang-zhi-zhen-shan-chu-zhong-fu-xiang-dai-you-hu/

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(nums == None or len(nums) == 0):
            return
        f, s = 0, 1
        while s < len(nums):
            if(nums[f] != nums[s]):
                if nums[f + 1] != nums[s]:
                    nums[f + 1] = nums[s]
                f+=1
                s+=1
            else:
                s+=1
        print(f"f: {f}, s: {s}")
        print(f"Result: {nums}")
        return f+1
        
    def removeDuplicates_v2(self, nums: List[int]) -> int:
        # 思考1: 什么时候要这个数？==》1)当它和前面的数不一样的时候，2)当它是第一个数时
        # 思考2：如果时in-place, 这array可不可以覆盖，什么时候可以？==》这个题可以覆盖，因为n的位置是永远less than or equal to i 的

        n = 0   # 跟踪最后一个valid的数。 
        for i in range(len(nums)):
            if i==0 or nums[i] != nums[i-1]: # 第一个肯定要。
                nums[n] = nums[i]
                n += 1
        
        return n

"""
   s
[0,0,1,1,1,2,2,3,3,4]
 f
"""