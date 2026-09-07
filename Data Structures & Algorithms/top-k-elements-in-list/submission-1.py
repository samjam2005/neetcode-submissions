class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        d=dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        output=[]
        for i in d:
            if k==0:
                break
            else:
                output.append(i)
                k-=1
        return output

        