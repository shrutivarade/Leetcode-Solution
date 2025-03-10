class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = nums1 + nums2
        nums3.sort()

        if(len(nums3)%2 == 0):

            one = nums3[len(nums3)//2-1]

            two = nums3[(len(nums3)//2)]

            med = (one + two) / 2
        else:

            med = nums3[len(nums3)//2]

        return med