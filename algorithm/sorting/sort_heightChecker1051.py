# bubble sort
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # step 1: sort the array heights to expected
        # step 2: compare the two arrays heights and expected. 
        
        # bubble sort:
        expected = [e for e in heights]
        swap = True
        while swap:
            changed = 0
            for i in range(len(expected)-1):
                if expected[i] > expected[i + 1]:
                    expected[i], expected[i+1] = expected[i+1], expected[i]
                    changed = 1
            if changed == 0:
                swap = False
        counts = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                counts += 1
        return counts
# merge sort
class Solution:
    
    # merge sort
    def merge_sort(self, heights, a, b):
        if 1 < b - a:
            c = (a + b + 1) // 2
            self.merge_sort(heights, a, c)
            self.merge_sort(heights, c, b)
            L = heights[a:c]
            R = heights[c:b]
            self.merge(heights, L, R, len(L), len(R), a, b)
            
    def merge(self, heights, L, R, i, j, a, b):
        if a < b:
            if (j <= 0) or (i>0 and L[i-1] > R[j-1]):
                heights[b-1] = L[i-1]
                i = i - 1
            else:
                heights[b-1] = R[j-1]
                j = j -1
            self.merge(heights, L, R, i, j, a, b-1)

    def heightChecker(self, heights: List[int]) -> int:
        # step 1: sort the array heights to expected
        # step 2: compare the two arrays heights and expected. 
        
        # merge sort:
        expected = [e for e in heights]
        self.merge_sort(expected, 0, len(expected))
        counts = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                counts += 1
        return counts

