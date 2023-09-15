class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        val = 0
        for g in gain:
            val = val + g
            alt = max(alt, val)

        return alt