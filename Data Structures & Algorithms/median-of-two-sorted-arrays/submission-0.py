class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import statistics
        l=sorted(nums1+nums2)
        n=len(l)
        return statistics.median(l)
        