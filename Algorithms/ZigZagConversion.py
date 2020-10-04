# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:00:45 2020

ZigZag Conversion

@author: GopalKrishna
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= 2:
            return s
        
        result = ''
        for i in range(numRows):
            k = i
            while k < len(s):
                print(s[k], i, k)
                result += s[k]
                k = k + 2*(numRows-1-i)
                if i != 0 and k < len(s):
                    if i != (numRows-1):
                        print(s[k], i, k)
                        result += s[k]
                    k = k + 2*i
        
        return result

if __name__ == '__main__':
    result = Solution().convert('PAYPALISHIRING',4)
    print(result)
    if result == 'PINALSIGYAHRPI':
        print('SUCCESS')
