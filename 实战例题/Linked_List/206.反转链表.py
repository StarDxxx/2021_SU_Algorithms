#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    """
    思路一：迭代
        1. 迭代需要三个指针，pre，cur，nxt，分别按顺序指向三个节点
        2. 三个指针的初始化：pre指向空节点，cur指向头结点head，nxt指向head.next 因为head.next可能不存在，nxt在循环中定义，这样如果head为空就不会进入循环 
        3. 迭代过程
            - nxt指向cur.next
            - cur.next指向pre
            - pre移动到cur位置
            - cur移动到nxt位置
        4. 当cur为空时，返回pre
    
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        """
            Case 1: If list is empty ==> return immediately

            Normal Case: 
                Need a new node to store the last node

        """
        # head = [1,2,3,4,5]
        pre = None
        while(head != None):
            print(head.val)
            next_head = head.next
            head.next = pre
            
            # Advance pre, and head
            pre = head
            head = next_head
        return pre

# @lc code=end

