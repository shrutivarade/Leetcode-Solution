class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # count the frequency of all the characters in word1 and word2 and create a hashmap/dict (key:value)
        c1 = Counter(word1)
        c2 = Counter(word2)

        #  count the frequency of all the values in c1 and c2
        # n1 = Counter([v for v in c1.values()])
        # n2 = Counter([v for v in c2.values()])

        n1 = Counter(list(c1.values()))
        n2 = Counter(list(c2.values()))

        one  = True if c1==c2 else False
        two  = True if n1==n2 else False
        three  = True if set(word1) == set(word2) else False

        return one or (two and three)