# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 09:52:55 2020

@author: GopalKrishna
"""


def sort(lst):
    print(lst)
    print('Sorting...')
    
    low_index = 0
    high_index = len(lst) - 1
    quick_sort(lst, low_index, high_index)
    
    print(lst)


def quick_sort(array, l, h):
    if l < h:
        p = partition(array, l, h)
        quick_sort(array, l, p-1)
        quick_sort(array, p+1, h)


def partition(array:list, l, h) -> int:
    
    pivot = array[l]
    i = l+1
    j = h
    
    while i < j:
        while array[i] < pivot:
            i+=1
            
        while array[j] > pivot:
            j-=1
            
        if i < j:
            array[i], array[j] = array[j], array[i]
        
    array[l], array[j] = array[j], array[l]
    return j


if __name__ == '__main__':
    arr = [4,5,7,6,3,2,6,3,9,1]
    sort(arr)