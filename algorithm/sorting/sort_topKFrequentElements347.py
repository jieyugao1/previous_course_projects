class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}
        for e in nums:
            if not e in arr:
                arr[e] = 1
            else:
                arr[e] += 1
        # sorting the frequency array arr2 using radix sort
        arr1 = list(arr.keys())
        arr2 = list(arr.values())
        #print(arr1)
        def countingSort(place):
            ele = [(e // place) % 10 for e in arr2]
            vk = max(ele)
            counts = [0] * (vk + 1)
            for i in range(len(ele)):
                counts[ele[i]] += 1
            # cumsum
            print(counts)
            start = 0
            for i, count in enumerate(counts):
                counts[i] = start
                start += count
                
            freq = [0] * len(arr1)
            eles = [0] * len(arr1)
            
            for i in range(len(ele)):
                freq[counts[ele[i]]] = arr2[i]
                eles[counts[ele[i]]] = arr1[i]
                counts[ele[i]] += 1
            
            for i in range(len(ele)):
                arr1[i] = eles[i]
                arr2[i] = freq[i]
        mval = max(arr2)
        place = 1
        while place <= mval:
            countingSort(place)
            place = place * 10
        
        return arr1[len(arr1) - k:]
                
                
            
                
                
        
        
