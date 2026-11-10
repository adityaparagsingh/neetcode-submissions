from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def k_works(k):
            #k belongs to [l,r] range
            hours = 0 
            for pile in piles:
                hours += ceil(pile/k) #ceil is roundup function
            
            return hours <= h #return True or False
        
        l = 1
        r = max(piles)
        for k in range(l,r+1):
            if k_works(k):
                return k