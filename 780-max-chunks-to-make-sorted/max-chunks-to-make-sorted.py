class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # subarray = []

        # i, j = 0, 0

        # while j < len(arr):
        #     if i == arr[j] or arr[i] == j and arr[j]<arr[i]:
        #         subarray.append(arr[i:j+1])
        #         i = j+1
        #         j=i
        #     else:
        #         j+=1

        # return len(subarray)

        return list(accumulate(x-i for i, x in enumerate(arr))).count(0)

        