class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         # Convert strings s and t into lists
#         a = []
#         for i in s:
#             a.append(i)
#         b = []
#         for i in t:
#             b.append(i)

#         # Sort the lists in ascending order
#         a.sort()
#         b.sort()

#         # Compare the sorted lists
#         if a == b:
#             return True
#         else:
#             return False

# # Time complexity analysis:
# # - Converting strings `s` and `t` into lists using a loop takes O(n) time, where n is the length of the longer string between `s` and `t`.
# # - Sorting the lists `a` and `b` using the `sort()` method takes O(n log n) time, as it uses an efficient sorting algorithm like Timsort or Quicksort.
# # - Comparing the sorted lists `a` and `b` using the `==` operator takes O(n) time, as it needs to compare each element of the lists.
# # - Therefore, the overall time complexity of this code is dominated by the sorting step, which is O(n log n), where n is the length of the longer string between `s` and `t`.

        mapS = Counter(s)
        mapT = Counter(t)

        return mapS == mapT

        # if len(s)==len(t) and len(set(s)) == len(set(t)) and set(s)==set(t):
        #     return True
        # else:
        #     return False