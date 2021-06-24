#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (65.08%)
# Likes:    1143
# Dislikes: 0
# Total Accepted:    185.2K
# Total Submissions: 284.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 进阶：
# 
# 
# 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
# 
# 
# 示例 4：
# 
# 
# 输入：head = [1], k = 1
# 输出：[1]
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 列表中节点的数量在范围 sz 内
# 1 
# 0 
# 1 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        """
            Idea:
                1. Seperate all nodes to K groups
                    - For each group, the head node points to the end node of next groups 
                2. Reverse nodes inside of each group
                3. handle号头，尾node与下一组之间的关系

            Implementation:
                1. group内部之间的关系
                2. group headNode与上一组的关系
                3. group endNode与下一组的关系  
        """
        # 因为第一组的lastNode不存在，所以要建立个保护点（0）指向head，这样就避免了last为None的情况
        protect_node = ListNode(0, head)
        # last是作为上一组的最后一个点。
        last = protect_node
        while(head!=None):

            thisGroupHead = head # Python is call by reference ==> Actually python is call by sharing, the 
            # print("==Begin==")
            # print(f"head: {head.val}")
            end = self.__getEnd(thisGroupHead, k)
            # print("==After==")
            # print(f"end: {end.val}, head: {head.val}")
            if (end==None): # Reached the ending group
                break
            # 保存next group head, 因为之后本组的新结尾（旧head）要跟下一组建立联系
            nextGroupHead = end.next

            # 处理head到end之间的k-1条边==》反转之后end就是新的head
            thisGroupHead = head
            self.__reverseList(thisGroupHead, end)

            # 让上一组跟本组的新head（旧end）建立联系
            last.next = end

            # 让本组的新结尾（旧head）要跟下一组建立联系
            head.next = nextGroupHead

            # 开始新的分组遍历
            last = head
            head = nextGroupHead
     
        return protect_node.next

    def __getEnd(self, head, k):
        # 从一个头开始，往回走k步，然后返回个endNode, 不足k步，就返回None
        # Becareful, There is k element in the group, but you only need to reverse k-1 edge
        # print("==Begin==")
        # print(f"head: {head.val}")

        while (head != None):
            # Put 'k-=1' first, so we can prevent the case for k==1
            k-=1
            if(k==0): 
                break
            head = head.next 
        # print("==After==")
        # print(f"head: {head.val}")
        return head

    # 不同于206. reverse list的是，这里不是把整个list反转过来，而是从head to end 这个group里的
    def __reverseList(self, head, end):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If a group has one node
        if head == end: 
            return
            
        # 这里暂时不需要处理head与上一组之前的关系，所以advance pre, and head pointer
        pre = head
        head = head.next
        # 改每条边，所以需要访问整个链表
        while(head != end):
            next_node = head.next
            # 改一条边
            head.next = pre
            # Advance pre, and head
            pre = head
            head = next_node
        
        # EndNode points to last one
        end.next = pre

        # Now, head and end all poinst to the largest node of a group
        # return head, end

# @lc code=end

