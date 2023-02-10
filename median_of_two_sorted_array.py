class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1)+len(nums2)
        half = total //2
        if len(B)< len(A):
            A, B = B, A
        l, r = 0, len(A)-1

        while True:
            mid = (l+r)//2
            rangeB = half-mid-2

            Aleft =A[mid] if mid>=0 else float("-inf")
            Aright = A[mid+1] if (mid+1)<len(A) else float("inf")

            Bleft = B[rangeB] if rangeB>=0 else float("-inf")
            Bright = B[rangeB+1] if rangeB+1<len(B) else float("inf")

            if Aleft<=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r = mid-1
            else:
                l= mid+1


            
