#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.14%)
# Likes:    1764
# Dislikes: 0
# Total Accepted:    598.9K
# Total Submissions: 905.2K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 
# 
# 示例 2：
# 
# 
# 输入：l1 = [], l2 = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 两个链表的节点数目范围是 [0, 50]
# -100 
# l1 和 l2 均按 非递减顺序 排列
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
            Idea: The intuition is similar to two pointer array.
        """
        protect = ListNode(0, None)
        last = protect

        while l1!=None and l2!=None:
            if l1.val > l2.val:
                last.next = l2
                l2 = l2.next
            else:
                last.next = l1
                l1 = l1.next
            last = last.next

        # Append the rest of node to the end
        last.next = l1 if l2==None else l2

        return protect.next
# @lc code=end

