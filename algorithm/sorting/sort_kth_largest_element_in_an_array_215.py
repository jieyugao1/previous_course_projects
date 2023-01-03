import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # QuickSelection Solution
        # Quick Sort extension:
        # Step 1: find the order of the pivot number
        # step 2: Compare the index with k, decide which branch to continue.
        # Step 3: repeat step 1 and step 2, until you find the kth largest number. 
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # step 1: move pivot to the last of the array
            nums[right], nums[pivot_index] = pivot, nums[right]
            ind = left # start of the pivot ranking
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[ind] = nums[ind], nums[i] 
                    # if less, swap, make it left hand side of the pivot
                    ind += 1
            nums[ind], nums[right] = nums[right], nums[ind]
            # swap the pivot to its correct position of the slice
            return ind 
        def select(left, right, k_smallest):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right) # both edges are included. 
            # pivot value
            pivot_index = partition(left, right, pivot_index)
            # find the ranking of the pivot value
            if k_smallest == pivot_index:
                return nums[pivot_index]
            elif k_smallest < pivot_index:
                return select(left, pivot_index -1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)

        return select(0, len(nums)-1, len(nums) - k)
