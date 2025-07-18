class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:]=nums2
        return nums1.sort()

        # i, j = 0, 0

        # while j<n:
        #     if nums2[j]<nums1[i]:
        #         nums1[i+1:] = nums1[i:len(nums1)-1]
        #         nums1[i] = nums2[j]
        #         i+=1
        #         j+=1
        #     else:
        #         i+=1
        # # print(nums1[:m+n])
        # nums1 = nums1[:m+n]

        


        

        