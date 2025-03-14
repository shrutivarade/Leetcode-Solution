class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # bruteforce: O(n^3) 3 for loops was getting results with duplicates
        [-1,-1,-1,0,2,2]
        nums.sort()
        result = []
        #  sorted: [-4, -1, -1, 0, 1, 2]
        for i in range(0, len(nums)-1):
            if i>0 and nums[i]==nums[i-1]: # for i^th pointer, outer loop
                continue
                
            l, r = i + 1, len(nums)-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if(sum > 0):
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r: # for l^th pointer, inner loop
                        l+=1

        return result
 



        # extended 2 sum, works only for easy test cases
        # result = []
        # for i in range(len(nums)):
        #     target = 0-nums[i]
        #     arr = []
        #     for j in range(i+1, len(nums)):
        #         if(target-nums[j] in arr):
        #             if(sorted([nums[i], nums[j], target-nums[j]]) not in result):
        #                 result.append(sorted([nums[i], nums[j], target-nums[j]]))
        #         else:
        #             arr.append(nums[j])
        # return result












