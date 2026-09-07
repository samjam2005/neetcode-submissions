class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        l=sorted(nums)
        maxx=1
        seq=[l[0]]
        for i in range(len(l)-1):
            if l[i+1]==l[i]:
                continue
            if l[i+1]-l[i]==1:
                seq.append(l[i+1])
            else:
                seq=[l[i+1]]
            if len(seq)>maxx:
                maxx=len(seq)
            
        return maxx


        