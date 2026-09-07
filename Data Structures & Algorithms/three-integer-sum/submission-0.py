class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums=sorted(nums)
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l<r:
                cursum=nums[l]+nums[r]
                if cursum<-nums[i]:
                    l+=1
                elif cursum>-nums[i]:
                    r-=1
                else:
                    output.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicates on right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return output
        