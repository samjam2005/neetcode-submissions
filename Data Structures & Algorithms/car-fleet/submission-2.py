class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionindex=sorted(range(len(position)), key=lambda i: position[i],reverse=True)
        l = []

        for i in positionindex:

            a = (target - position[i]) / speed[i]

            if l and a <= l[-1]:
                continue

            l.append(a)

        return len(l)