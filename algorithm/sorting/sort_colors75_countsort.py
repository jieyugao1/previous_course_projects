import numpy as np
class Solution:
    # using counting sort 
    # time: O(n+k); space O(n+k)
    # since only have 0, 1, 2 possible values. k = 2
    # step 1: creating a counting array o(k+1)
    # step 2: get the counts o(n)
    # step 3: cumsum o(k+1)
    # step 4: back up the sorted array o(n)
    
    def sortColors(self, nums: List[int]) -> None:
        k = max(nums) # o(n)
        
        counts = [0] * (k+1)
        for i in range(len(nums)):
            counts[nums[i]] += 1
        # cumsum
        start = 0
        for i, count in enumerate(counts):
            counts[i] = start
            start = start + count
        #print(counts)
        arr = [0] * len(nums)
        #print(arr)
        for i in range(len(nums)):
            #print(nums[i])
            arr[counts[nums[i]]] = nums[i]
            counts[nums[i]] += 1
        #print(arr)
        for i in range(len(arr)):
            nums[i] = arr[i]

                
            
    
    """
    def merge(self, L, R, nums, i, j, a, b):
        # merge sort L[:i] and R[:j] into nums[a:b]
        # L, R: sorted list
            if a < b:
                if (j <= 0) or (i > 0 and L[i-1] > R[j-1]):
                    nums[b - 1] = L[i - 1] # change the largest value at position b-1
                    i = i -1 # update the pointer i
                else:
                    nums[b-1] = R[j-1] # the largest is R[j-1]
                    j = j -1 # update pointer j
                self.merge(L, R, nums, i, j, a, b-1)
    def merge_sort(self, nums, a, b):
        # A: array to be sorted
        # a: start index
        # b: end index
            if 1 < b - a:
                c = (a + b + 1) //2
                self.merge_sort(nums, a, c)
                self.merge_sort(nums, c, b)
                L, R = nums[a:c], nums[c:b]
                self.merge(L, R, nums, len(L), len(R), a, b)
    
    def sortColors(self, nums: List[int]) -> None:
        
        
        
        #Do not return anything, modify nums in-place instead.
        
        # merge sort: O(n^2)
        # Step 1: split the array into two pieces recursively to sort them O(nlogn)
        # Step 2: merge the two pieces. O(n)
        self.merge_sort(nums, 0, len(nums))
    
    """



            
            
        
