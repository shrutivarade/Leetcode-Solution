class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        
        while k>0:

            maxVal = max(gifts)
            idx = gifts.index(maxVal)
            # gifts.remove(maxVal)
            gifts[idx] = floor(sqrt(maxVal))

            k-=1
        
        return sum(gifts)