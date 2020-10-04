# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:07:52 2020
3Sum
@author: GopalKrishna
"""

#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
#Find all unique triplets in the array which gives the sum of zero.
#
#Note:The solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums):
        result = []
        count = len(nums)
        for i in range(count - 2):
            l = None
            a = nums[i]
            for j in range(i+1, count - 1):
                b = nums[j]
                for k in range(j+1, count):
                    c = nums[k]
                    if a+b+c == 0:
                        l = [a,b,c]
                        if l not in result:
                            result.append(l)
#            if l and l not in result:
#                result.append(l)
        
        return result
        
        
        
        
if __name__ == '__main__':
#    nums = [-1, 0, 1, 2, -1, -4]
    nums = [0,0,0,0]
#    nums = [-2,0,1,1,2]
    sol = Solution()
    r = sol.threeSum(nums)
    print(r)