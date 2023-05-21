class Solution:
        
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if d.get(sorted_str, None):
                d[sorted_str].append(s) 
            else:
                d[sorted_str] = [s]

        l = []

        for v in d.values():
            l.append(v)
        
        return l
