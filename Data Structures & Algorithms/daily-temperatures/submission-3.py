class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            j=i+1
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                l[prev]=i-prev
            stack.append(i)
        return l
        