class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # heap sort
        # step 1: write a heapify function to create max-heap - max_heapify
        # step 2: swap the root node with the last element, continue with the remaining elements
        # step 3: repeat step 1 and 2 until the len(arr) equals to 1
        
        def max_heapify(n, i):
            # Find the index of the left child and right 
            largest = i
            left = i * 2 + 1
            right = i * 2 + 2
            
            # Check if the parent node is larger than the children
            # if not, swap the parent node with the children. 
            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            if largest != i:
                # swap 
                nums[largest], nums[i] = nums[i], nums[largest]
                # check the swapped branches. 
                max_heapify(n, largest)
                
        # initialize the max-heap         
        for i in range(len(nums)//2 -1, -1, -1): # starting with the nodes that have childrens
            max_heapify(len(nums), i)
        print(nums)
        for i in range(len(nums)-1, -1, -1):  
            nums[0], nums[i] = nums[i], nums[0] # swap the last element with the current element
            max_heapify(i, 0) # max_heapify the remaining elements
        return nums
