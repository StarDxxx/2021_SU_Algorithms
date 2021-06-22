#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (45.81%)
# Likes:    709
# Dislikes: 0
# Total Accepted:    305.7K
# Total Submissions: 667.1K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 
# 
# 示例 2：
# 
# 
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 
# 
# 示例 3：
# 
# 
# 输入：digits = [0]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        # Normal case: 0<= digits[-1]<9
        if digits[-1]<9 and digits[-1] >= 0:
            digits[-1]+=1
        else: # digits[-1] == 9
            # All digits are 9
            last_9 = len(digits)-1
            while last_9>=0 and digits[last_9]==9:
                digits[last_9] = 0
                last_9-=1
            # That case all digits are 9 ==> in sert 1 at begeinning and replace all 9 to 0
            print(last_9)
            if last_9==-1:
                digits.insert(0, 1)
            else: # Where we have non-9 number at front
                digits[last_9]+=1
        return digits
"""
通过枚举的方法，把所有可能的类型都列出来:
1. Normal Case:
15+1=16
5+1=5 
==> 直接在最后一位加一

2. 最后一个是9， 且全是9
9 + 1 = 10 ==> 9 become 1, and append 0
99 + 1 = 100
==》 所有9 replaced by 0, then insert 1 at the beginning

3. 最后一个是9，但前面有非9的数
19 + 1 = 20 ==> add one to previous element
1199 + 1 = 1200
==》因为不需要进位，所以直接replace all 9 by 0, and add 1 to previous digit
"""
# @lc code=end

