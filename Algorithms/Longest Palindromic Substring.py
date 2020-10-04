# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 06:59:22 2020

5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

@author: GopalKrishna
"""



class Solution:
    def my_longestPalindrome(self, s: str) -> str:
        longestString = ''
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if(s[i:j] == s[i:j][::-1]):
                    if len(s[i:j]) > len(longestString):
                        longestString = s[i:j]
        
        return longestString
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Return if string is empty
        if not s: return s

        res = ""
        for i in range(len(s)):
            j = i + 1
            # While j is less than length of string
            # AND res is *not* longer than substring s[i:]
            while j <= len(s) and len(res) <= len(s[i:]):
                # If substring s[i:j] is a palindrome
                # AND substring is longer than res
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    s = 'babad'
    print(sol.longestPalindrome(s))