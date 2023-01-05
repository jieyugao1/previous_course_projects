# Sorting Algorithms

## Selection Sort

**Time complexity**: O($$N^2$$)
    
    T(N) = T(N-1) + O(N)

**Space complexity**: O(1)

**Steps**:
    
    1. Find a largest number in A[:i + 1] and swap it to A[i]
    2. i = i - 1
    3. Recursively sort prefix A[:i], until i == 1

    
## Insertion Sort

**Time complexity**: O($N^2$)

    T(N) = T(N-1) + O(N)

**Space complexity**: O(1)

**Steps**:

    1. Sort A[:i]
    2. i = i + 1
    3. Sort A[:i+1] assuming that A[:i] is sorted. (Repeated swaps)

## Bubble Sort



## Merge Sort 

Time complexity: O(nlogn)
Space complexity: O(1)


