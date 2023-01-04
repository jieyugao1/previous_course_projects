class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # Radix sort
        # step 1: writing the counting sort
        # step 2: call the radix sort using the counting sort with the appropriate digits. 
        def countingSort(place): # return the ranking index
            
            counts = [0] * 10
            eles = [(int(nums2[i][len(nums2[i]) - place -1])) % 10 for i in range(len(nums2))]
            for i in range(len(nums2)):
                ele = eles[i]
                counts[ele] += 1
            # cumsum counts
            start = 0
            for i, count in enumerate(counts):
                counts[i] = start
                start += count
            # back up the index
            inds = [0] * len(nums2)
            for i in range(len(inds)): 
                inds[counts[eles[i]]] = nums2[i]
                counts[eles[i]] += 1
            for i in range(len(nums2)):
                nums2[i] = inds[i]
                
        res = []
        # initialize the eles0
        res2 = {}
        for e in queries:
            ki, trimi = e[0], e[1]
            if trimi not in res2:
                start = 1
                #print(res2)
                if len(res2) > 0:
                    for e, _ in enumerate(res2):
                        if (e < trimi) and (e > start):
                            start = e
                        nums2 = res2[start]
                else:
                    nums2 = [ele for ele in nums]
                for j in range(start - 1, trimi):
                    countingSort(j)
                    res2[j+1] = [ele for ele in nums2]
                #print(nums2)
            else:
                nums2 = res2[trimi]
            # to avoid the repeated issues: create a included array
            included = [0] * len(nums)
            #print(nums2)
            start = 0 
            for i in range(ki):
                j = 0
                while j < len(nums):
                    if (not included[j]) and (nums2[i] == nums[j]):
                        included[j] = 1
                        start = j
                        break
                    j = j + 1
            #print(inds)
            res.append(start)
        return res
                
                
            
            
            
            
        
