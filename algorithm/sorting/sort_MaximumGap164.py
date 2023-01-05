class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # sort in linear time: 
        # use radix sort
        def countingSort(place):
            eles = [(nums[i] // place) % 10 for i in range(len(nums))]
            
            k = max(eles)
            counts = [0] * (k + 1)
            # counts
            for i in range(len(eles)):
                counts[eles[i]] += 1
            start = 0
            # cumsum
            
            for i, count in enumerate(counts):
                counts[i] = start
                start += count
            
            arr = [0] * len(nums)
            for i in range(len(nums)):
                arr[counts[eles[i]]] = nums[i]
                counts[eles[i]] += 1
            for i in range(len(nums)):
                nums[i] = arr[i]
            
            
        if len(nums) < 2:
            return 0
        k = max(nums)
        digit = 1
        while digit <= k:
            countingSort(digit)
            digit = digit * 10
        #print(nums)
        max_diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] > max_diff:
                max_diff = nums[i] - nums[i-1]
        return max_diff
        
