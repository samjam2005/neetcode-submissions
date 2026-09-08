class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        l = []

        for pos, spd in cars:

            a = (target - pos) / spd

            if l and a <= l[-1]:
                continue

            l.append(a)

        return len(l)