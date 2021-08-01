from typing import List
import math


def insertion_sort(array: List[int]) -> List[int]:
    
    """
    An inplace sorting algorithm
    ---------------
    Inputs:
    array: a list of elements to be sorted in ascending order.
    ---------------
    Returns:
    A sorted array in ascending order.
    """
    for j in range(1, len(array)):
        x = array[j]
        i = j-1
        while (i>=0) and (array[i]>=x):
            array[i+1]=array[i]
            i = i-1
            
        array[i+1]=x
        print(array)
    return array

def merge_sort(array: List[int]) -> List[int]:
    """
    A divide and conquer algorithm as funtion divides the list
    into sublists and finally merges.
    ---------------
    Inputs:
    array: a list of elements to be sorted in ascending order.
    ---------------
    Returns:
    A merge function for merging both sublists
    """
    len_array = len(array)
    if len_array<= 1:
        return array

    half_len = math.floor(len_array/2)

    #Dividing lists into two parts.
    left_list = array[:half_len]
    right_list = array[half_len:]

    #Recursive call to divide lists.
    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return merge(left, right)


def merge(left:List, right:List)-> List[int]:
    """
    Compares the left and right sublist and
    merges both into one.
    ---------------
    Inputs:
    left: left sublist
    right: right sublist
    ---------------
    returns merged array in ascending order.
    """
    sorted_list = list()
    while (len(left)>0 and len(right)>0):
        if left[0]<=right[0]:
            sorted_list.append(left[0])
            left = left[1:]
        else:
            sorted_list.append(right[0])
            right = right[1:]
    
    while (len(left)>0):
        sorted_list.append(left[0])
        left = left[1:]

    while (len(right)>0):
        sorted_list.append(right[0])
        right = right[1:]
    return sorted_list