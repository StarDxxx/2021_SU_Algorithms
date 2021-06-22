from typing import List

def selection_sort_recursive(list, n):
    if n == 0:
        return
    else:
        for i in range(n):
            print(i)
            if list[i]>list[n-1]:
                temp = list[i]
                list[i] = list[n-1]
                list[n-1]=temp
        selection_sort_recursive(list, n-1)
        # for i in range(len(list), 0):
        #     for j in range(i)

def selection_sort_for_loop(list, n):
    if n == 0:
        return
    else:
        for i in range(n, 0, -1):
            print(i)
            # if list[i]>list[n-1]:
            #     temp = list[i]
            #     list[i] = list[n-1]
            #     list[n-1]=temp
        # for i in range(len(list), 0):
        #     for j in range(i)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
"""
nums1 = [1,2,3,0,0,0]
         f 
nums2 = [2,5,6]
         s


nums1_copy = [1,2,3,0,0,0]


A = [8, 7, 6, 5, 4, 3, 2, 1]
selection_sort_for_loop(A, len(A))
print(A)

"""