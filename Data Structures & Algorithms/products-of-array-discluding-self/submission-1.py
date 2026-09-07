class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        prod=1
        zero_count = nums.count(0)
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            prod*=nums[i]
        for i in range(len(nums)):
            if zero_count > 0:
                if zero_count == 1 and nums[i]==0:
                    output.append(prod)
                else:
                    output.append(0)
            else:
                output.append(int(prod/nums[i]))

        return output