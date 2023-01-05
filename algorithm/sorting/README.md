# Sorting Algorithms

## Selection Sort

**Time complexity**: O(N^2)
    
    T(N) = T(N-1) + O(N)

**Space complexity**: O(1)

**Steps**:
    
    1. Find a largest number in A[:i + 1] and swap it to A[i]
    2. i = i - 1
    3. Recursively sort prefix A[:i], until i == 1

    
## Insertion Sort

**Time complexity**: O(N^2)

    T(N) = T(N-1) + O(N)

**Space complexity**: O(1)

**Steps**:

    1. Sort A[:i]
    2. i = i + 1
    3. Sort A[:i+1] assuming that A[:i] is sorted. (Repeated swaps)

## Bubble Sort

**Time complexity**: O(N^2)

    T(N) = T(N-1) + O(N)

**Space complexity**: O(1)

**Steps**:

    1. Consider two adjacent elements at a time, if out of order, swap. 
    2. Repeat step 1 until no more swaps are made in a single pass. 

## Quick Sort

**Time complexity**: O(NlogN)

    T(N) = T(k) + T(N-k-1) + O(N)

Worst case: O(N^2)

Best case: O(NlogN)

    1. Faster in practice. 
    2. Not a stable sort.


**Space complexity**: O(1)

**Steps**:
    
    1. In each pass, randomly (or other selection criterion) select the pivot value. 
    2. in each round, find the index of the pivot value, put all values that are less than the pivot value to the left, that are larger than the pivot value to the right. 
    3. Recursively sort the array by repeating step 1 and step 2 on both side around the pivot value. 
    
## Heap Sort

Heap sort is a direct optimizaiton of the selection sort. 

**Time complexity**: O(NlogN)

    1. Building a max-heap: O(N)
    2. Removing any element in the max-heap: O(logK), where K is the number of elements in the heap. 

Note that, based on stirling approximation:

    O(logn + log(n-1) + ... + log(1)) = O(log(n!)) = O(nlogn) 

    T(N) = O(N) + O(NlogN) = O(NlogN)

**Space complexity**: O(1)

**Steps**:
    
    1. Convert the array into max-heap. 
    2. The maximum value is stored at the root of the heap. Swap the root with the last item of the heap. Reduce the heap size by 1. Heapify the root of the tree. 
    3. Repeat step 2 until the size of the heap equals to 1. 


## Merge Sort 

Time complexity: O(nlogn)
Space complexity: O(1)


