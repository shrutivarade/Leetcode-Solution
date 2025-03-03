class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        n = len(nums)
        i,j,l,r = 0, n-1, 0, n-1
        res = [0] * n
        while i<n and j>-1:

            # Both are pivot
            if nums[i]==pivot and nums[j]==pivot:
                i+=1
                j-=1
                continue

            #  either of them is pivot
            if nums[i]==pivot: 
                i+=1
                if nums[j]>pivot:
                    res[r] = nums[j]
                    r-=1
                j-=1
                continue
                
            if nums[j]==pivot: 
                j-=1
                if nums[i]<pivot:
                    res[l] = nums[i]
                    l+=1
                i+=1
                continue

            #  None of them is pivot
            if nums[i]<pivot:
                res[l] = nums[i]
                l+=1
            if nums[j]>pivot:
                res[r] = nums[j]
                r-=1
                
            i+=1
            j-=1
        j+=1
        while j<n:
            if nums[j]==pivot: 
                res[l] = pivot 
                l+=1
            j+=1

        
        return res
