class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l={}
        for i in strs:
            if "".join(sorted(i)) not in l.keys():
                l["".join(sorted(i))]=[i]
            else:
                l["".join(sorted(i))].append(i)

        return list(l.values())
        