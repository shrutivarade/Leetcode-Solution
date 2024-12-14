class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0

        removed_indices = set()
        # Create a priority queue with (value, index) tuples
        pq = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(pq)  # Transform into a min-heap

        while pq:
            # Extract the minimum value and its index
            min_value, min_index = heapq.heappop(pq)
            # score += min_value

            # # Check if indices 4, 5, and 6 are present
            # indices_to_check = [min_index - 1, min_index + 1]
            # values_to_remove = []

            # for value, index in pq:
            #     if index in indices_to_check:
            #         values_to_remove.append((value, index))

            # # Remove these elements from the priority queue
            # pq = [(value, index) for value, index in pq if index not in indices_to_check]
            # heapq.heapify(pq)  # Rebuild the heap

            # Skip if this index has already been processed
            if min_index in removed_indices:
                continue

            # Add the value to the score
            score += min_value

            # Mark the current index and neighbors as removed
            removed_indices.add(min_index)
            removed_indices.add(min_index - 1)
            removed_indices.add(min_index + 1)




        # dict = {}
        # for i, val in enumerate(nums):
        #     if val in dict:
        #         dict[val].append(i)
        #     else:
        #         dict[val] = [i]
        # while dict:
        #      # Prepare indices_to_pop
        #     indices_to_pop = [] 
        #     # Find the minimum key
        #     min_key = min(dict)
        #     score += min_key
        #     # Get the 0th element of the list
        #     index = dict[min_key][0]
        #     indices_to_pop.append(index)
        #     indices_to_pop.append(index-1)
        #     indices_to_pop.append(index+1)
        #     # Loop through indices and pop them
        #     for idx in indices_to_pop:
        #         for key, idxs in dict.items():
        #             if idx in idxs:
        #                 idxs.remove(idx)  # Remove the index from the list
        #                 if not idxs:  # If the list is empty, remove the key
        #                     del dict[key]
        #                 break  # Exit the inner loop as index has been popped




        #     if(idx>0 and idx<len(nums)-1):
        #         nums.pop(idx-1)
        #         nums.pop(idx-1)
        #         nums.pop(idx-1)
        #         continue
        #     elif ((idx>0 and not idx<len(nums)-1 or (len(nums)==2 and idx>0))):
        #         nums.pop(idx-1)
        #         nums.pop(idx-1)
        #         continue
        #     elif ((not idx>0 and idx<len(nums)-1) or (len(nums)==2 and idx<len(nums)-1)):
        #         nums.pop(idx+1)
        #         nums.pop(idx)
        #         continue
        #     if(len(nums)==1):
        #         nums.pop(idx)
        #         continue

        return score

