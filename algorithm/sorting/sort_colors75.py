# Selection Sort solution O(n^2)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # selection sort: O(n^2)
        # Step 1: go through A[:i] element, find the maximum and swap it with A[i]
        # repeat step 1, until i == 0
        
        for i in range(len(nums), 0, -1):
            max_i = i
            for j in range(i, 0, -1):
                if nums[j-1] > nums[max_i-1]:
                    max_i = j
            nums[i-1], nums[max_i-1] = nums[max_i-1], nums[i-1]
        return nums

# Merge sort solution O(nlogn)
class Solution:
    
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
        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        # merge sort: O(n^2)
        # Step 1: split the array into two pieces recursively to sort them O(nlogn)
        # Step 2: merge the two pieces. O(n)
        self.merge_sort(nums, 0, len(nums))
