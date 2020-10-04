# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:05:49 2020

@author: GopalKrishna
"""

def sort(array):
    print(array)
    print('Sorting...')
    merge_sort(array, 0, len(array)-1)

def merge_sort(array, l, h):
    if l < h:
        mid = (l+h)/2
        merge_sort(l, mid -1)
        merge_sort(mid + 1, h)
        merge(array, l, mid, h)


def merge(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    
    temp = []
    i=0 
    j=0 
    k=0
    while True:
        if left[i] < right[j]:
            temp[k] = left[i]
            ++i,  ++k
        else:
            temp[k] = right[j]
            ++j,  ++k
    
    while i < len(left):
        temp[k] = left[i]
        ++i, ++k
        
    while j <len(right):
        temp[k] = right[j]
        ++j, ++k


if __name__ == '__main__':
    arr = [4,5,7,6,3,2,6,3,9,1]
    merge(arr, 0, 4, 9)