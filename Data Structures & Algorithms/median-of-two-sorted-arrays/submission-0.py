class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        m, n = len(nums1), len(nums2)
        # len b >= a
        if m > n:
            a, b = b, a
            m, n = n, m
        
        total = m+n
        half = (total+1)//2
        l, r = 0, m # a
        while l < total:
            i = (l+r)//2 # a index
            j = half-i # b index

            aleft = a[i-1] if i > 0 else float('-inf')
            aright = a[i] if i < m else float('inf')
            bleft = b[j-1] if j > 0 else float('-inf')
            bright = b[j] if j < n else float('inf')

            if aleft <= bright and bleft <= aright:
                # odd length
                if total & 1:
                    return max(aleft, bleft)
                # even length
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1