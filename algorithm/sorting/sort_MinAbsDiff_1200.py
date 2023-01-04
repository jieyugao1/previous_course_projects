class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # step 1: sort the array o(nlogn) using merge sort
        # step 2: for the sorted array, find the minimum distance by differencing the consecutive element: o(n)
        # step 3: report the resulted pairs
        def merge(L, R, i, j, a, b):
            # merge L[:i] and R[:j] to arr[a:b]
            if a < b:
                if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
                    arr[b - 1] = L[i - 1]
                    i = i - 1
                else:
                    arr[b - 1] = R[j - 1]
                    j = j - 1
                merge(L, R, i, j, a, b-1)
        def merge_sort(a, b):
            # arr: array to be sorted
            # a: start index
            # b: end index
            # The goal is to sort arr[a:b]
            if 1< b - a:
                c = (a+b+1) //2 # seperate the array from the middle
                merge_sort(a, c)
                merge_sort(c, b)
                L = arr[a:c]
                R = arr[c:b]
                merge(L, R, len(L), len(R), a, b)
        merge_sort(0, len(arr))
        min_distance = arr[len(arr)-1] - arr[0] # initiate the min distance
        res = []
        for i in range(1, len(arr)):
            min_distance = min(min_distance, arr[i] - arr[i-1])
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_distance:
                res.append([arr[i-1], arr[i]])
        return res
        
                
            
            
            
