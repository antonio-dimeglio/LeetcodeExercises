class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []

        for elem in nums:
            d[elem] = d.get(elem, 0) + 1
        
        for i in range(k):
            vmax = 0
            kmax = 0 

            for k, v in d.items():
                mx = max(vmax, v)
                if v == mx:
                    kmax = k
                    vmax = mx
            
            l.append(kmax)
            d.pop(kmax)
        return l
