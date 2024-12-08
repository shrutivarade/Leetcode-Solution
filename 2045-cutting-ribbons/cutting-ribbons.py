# class Solution:
#     def maxLength(self, ribbons: List[int], k: int) -> int:

#         if k > sum(ribbons):
#             return 0

#         # def can_divide(max_balls):
#         #     ops = 0
#         #     for n in ribbons:
#         #         ops += ceil(n / max_balls) - 1
#         #         if ops > k:
#         #             return False
#         #     return True
#         # O(n * logm)
#         l, r = 1, max(ribbons)
#         # res = r
#         while l < r:
#             m = (l + r + 1) // 2
#             res = 0
#             for r in ribbons:
#                 res += r // m
#                 if res >= k:
#                     break

#             if res >= k:
#                 l = m
#             else:
#                 r = m - 1
#         # return res
#         return l

class Solution:
	def maxLength(self, ribbons: List[int], k: int) -> int:
	    # If we cut every ribbon to size of 1 and 
		# we still cannot make k ribbons then it's impossible to satisfy k.
		if sum(ribbons) < k:
			return 0
       
	    # We know we can make any k ribbons with size of 1 from here, 
		# the largest possible ribbon we can make is the largest ribbon in `ribbons`
		right = max(ribbons)
		left = 1

		while right > left:
		    # we take the ceiling rather than the floor here so we don't get stuck in infinite loop
			# +1 is for ceiling.
			mid = (right + left + 1) // 2
			total = 0
			# Count the ribbons and see how many we can make with length == mid.
			for ribbon in ribbons:
				total += ribbon // mid
				# Optimization to short circuit if we know we can make enough ribbons
				if total >= k:
					break
			# This is the important bits, if we know mid is a candidate now, then we know answer
			# is in the space of [mid, right], if not we know the answer must be in the space of
			# [low, mid - 1] since mid would not be a candidate anymore in the latter case. 
			if total >= k:
				left = mid
			else:
				right = mid - 1
		return left