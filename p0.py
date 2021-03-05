#!/usr/bin/python3
from random import randrange


def RandomizedPartition(A, p, r):
    """
    Implement Randomized partitioning from Cormen book
    20% Points will be deducted if you do not use RANDOMIZATION
    """
    i = randrange(p,r)
    A[r], A[i] = A[i], A[r]
    return part(A, p, r)
    
def part(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return (i+1)

def QuickSort(A, p, r):
    """
    Implement Quicksort method using RandomizedPartition from Cormen book (Look at Section 7.3)
    40% points will be reduced if you do not use RandomizedPartition
    The array is sorted in place.
    """
    if p<r:
        q = RandomizedPartition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
        
    
def isAnagram(string1, string2):
    """
    Return true if string2 is an anagram of string1 otherwise return false
    Example of anagrams: (red, der) (abcdefg, bacdgfe)
    """
    if len(string1) == len(string2):
        QuickSort(string1, 0, (len(string1)-1))
        QuickSort(string2, 0, (len(string2)-1))
        if string1 == string2:
            return True
    return False
    
    
def sortByOnesBits(array):
    """
    You are given an integer array. 
    The goal is to sort the integers in ascending order by the number of 1's in their binary representation and 
    when two or more integers have the same number of 1's, those numbers must be sorted in ascending order.
    Return the sorted array
    """
    binQuick(array, 0, (len(array)-1))
    return
    
def binPart(A, p, r):
    x = bin(A[r]).count('1')
    y = A[r]
    i = p-1
    for j in range(p, r):
        if bin(A[j]).count('1') < x:
            i = i+1
            A[i], A[j] = A[j], A[i]
        elif bin(A[j]).count('1') == x:
            if A[j] <= y:
                i = i+1
                A[i], A[j] = A[j], A[i]   
    A[i+1], A[r] = A[r], A[i+1]
    return (i+1)

def binQuick(A, p, r):
    if p<r:
        q = binPart(A, p, r)
        binQuick(A, p, q-1)
        binQuick(A, q+1, r)