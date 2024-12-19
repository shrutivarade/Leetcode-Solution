class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        subarray = []
        i, j = 0, 0
        while j < len(arr):
            # if (i == arr[j] or arr[i] == j ) or len(arr[i:j+1]) == max(arr[i:j+1])+1: this logic was working partially
            if max(arr[i:j+1]) == j:
                subarray.append(arr[i:j+1])
                i = j+1
                j=i
            else:
                j+=1
                if(j==len(arr)):
                    subarray.append(arr[i:j+1])
        return len(subarray)

        