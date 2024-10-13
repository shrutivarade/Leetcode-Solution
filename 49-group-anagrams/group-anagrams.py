
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create an empty dictionary to store anagrams
        dict = {}

        # Iterate over each string in the input list
        for s in strs:
            # Sort the current string and convert it back to a string
            sorted_string = ''.join(sorted(s))

            # Check if the sorted string is not in the dictionary
            # If it's not, add it as a key and assign an empty list as its value
            if sorted_string not in dict:
                dict[sorted_string] = []

            # Append the current string to the list of anagrams in the dictionary
            dict[sorted_string].append(s)

        # Return a list of lists containing the grouped anagrams
        return list(dict.values())

# Time complexity analysis:
# - The code uses a dictionary to group anagrams. The dictionary allows constant-time average case lookup.
# - The code iterates over each string in the `strs` list, which takes O(n) time, where n is the length of the input list.
# - Inside the loop, the code performs string sorting, which takes O(k log k) time, where k is the average length of the strings in `strs`.
# - Appending the current string to the list of anagrams in the dictionary takes constant time.
# - Finally, converting the dictionary values to a list takes O(m) time, where m is the number of groups of anagrams.
# - Therefore, the overall time complexity of this code is O(n * k log k), where n is the length of the input list `strs`, and k is the average length of the strings in `strs`.