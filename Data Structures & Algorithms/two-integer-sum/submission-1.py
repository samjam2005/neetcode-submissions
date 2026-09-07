class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement={}
        nums2={}
        for i in range(len(nums)):
            complement[i]=nums[i]
            nums2[nums[i]]=i
        for i in range(len(complement)):
            if target-complement[i] in nums and i!=nums2[target-complement[i]]:
                return [i,nums2[target-complement[i]]]        