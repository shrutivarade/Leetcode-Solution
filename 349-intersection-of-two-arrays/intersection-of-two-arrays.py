class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        # result = []
        # for i in nums1:
        #     if i in nums2:
        #         result.append(i)

        # return result


        return list(set(nums1) & set(nums2))