# Author: Zhengqi Dong
# Date: 6/19/2021
# Tag: Array, Sorting, Two_pointers
# Category: Easy_Level_Coding_Question
# Title: LeetCode Question: 88.Merged Sorted Array
# Question: https://leetcode-cn.com/problems/merge-sorted-array/
# Solution: https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/

from typing import List
class Solution:
    """ Idea
    Detailed Implementation: Create a copy of nums1, and use it to compare with nums2. The intuition is similar to two pointer sliding over two array. Since, we know the elements in both array were sorted, so it's ok two use two pointer strategy. If the value in nums1_copy is greater than nums2, and copy it to nums1(because the question will check it for answer), otherwie we will copy the value from nums2, and advance the pointer. There are two special cases we need to consider. First, what happen if nums1 is shorter than nums2? what if nums2 is shorter than nums1? In other word, what happen if one array is shorter than the other. ==> The answer to that is we need to two if condition to handle those cases.
    """
    
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_copy = nums1[:]
        p1, p2 = 0, 0
        for i in range(len(num1_copy)):
            if p1 == m:
                nums1[i] = nums2[p2]
                p2+=1
            elif p2 == n:
                nums1[i] = num1_copy[p1]
                p1+=1
            elif num1_copy[p1] <= nums2[p2]:
                nums1[i] = num1_copy[p1]
                p1+=1
            else:
                nums1[i] = nums2[p2]
                p2+=1
        # print(f"num1_copy")
        return nums1
    """
    Analysis:
    # Time Complexity: O(m+n), because the p1 must traverse m element in nums1, and p2 must traverse n element in nums2, and perform the data read and copy operation.
    # Space complexity: O(m+n), because, we need create extra copy of nums1 ==> There is way to reduce to O(1), check solution3, the inverse double pointer solution.

    """

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        """Idea:
            主题思路：i，j两个索引，从尾部开始，睡大放谁
            细节：处理边界问题

            Input:
            nums1_copy = [1,2,3,0,0,0]
                            f
            nums2 = [2,5,6]
                       s

            Output:
            nums1 = [1,2,2,3,5,6]
                               ^
        """
        p1, p2 = m-1, n-1
        tail = m+n-1
        while p1>=0 or p2>=0:
            if p1 == -1: # If p1 reach the head of nums
                nums1[tail] = nums2[p2]
                p2-=1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1-=1
            elif nums1[p1]> nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2-=1
            tail-=1
        # print(f"num1_copy")
        return nums1

    def merge3_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Method 1: In place, 
        Cost: Time: O(m+n), Space: O(1)
        Idea: use two pointers (named p1 and p2). p1 started from last element in nums1 and p2 started from the last element in nums2. Use another pointer(named i) traverse through nums1 in reverse order. If the element p1 points two greater than p2, put nums1[p1] to the nums1[i], otherwise put nums2[p2] to the nums1[i]. For the edge case, where m != n, and one pointers will reach to the end before other. 
        Q1: 
            Why cannot use for loop? ==> Because this case won't pass, 
        merge([0], 0, [1], 1). ==> Because for(0, 0, -1) won't get executed.
        Q2:
            Why use this for condition statement? ''if p2<0 or (p1>=0 and nums1[p1]>nums2[p2]):''
            First, be careful for the out of index error, when accessing array, you need to make sure you use the valid index values.
            Second, we only copy from nums1[p1], if p2 reached the edge case, or p1 is not reached end yet and has element greater than nums2[p1]. ==> We need ''p1>=0'' this condition, that covers the based case, that decides when the loop will stop.

        
        """
        p1, p2 = m-1, n-1
        i=m+n-1
        while p1>=0 or p2>=0: # Traver from tail to the head
            if p2<0 or (p1>=0 and nums1[p1]>nums2[p2]):
                nums1[i] = nums1[p1]
                p1-=1
            else:
                nums1[i] = nums2[p2]
                p2-=1
            i-=1

# Note1: you need ''len(nums1)-1'' is because, for reverse operation, if you use ''len(nums1)'', then python will start counting from len(nums) to 0 ==> Then you will got ''IndexError: list assignment index out of range''


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution.merge3(..., nums1, m, nums2, n) # ... means ignore the self argument
    print(nums1)