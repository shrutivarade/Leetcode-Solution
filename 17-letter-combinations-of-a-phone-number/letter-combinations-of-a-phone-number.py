class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letters = { "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        if not digits: return []

        output=[""]

        for d in digits:
            temp = []
            
            for l in letters[d]:
                for o in output:
                    temp.append(o+l)
            output = temp
        
        return output