class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i is '(' or i is '[' or i is '{':
                stack.append(i)
            elif  i is ')':
                if len(stack)==0:
                    return False
                elif stack[-1] is not '(' :
                    return False
                else:
                    stack.pop()
            elif  i is ']':
                if len(stack)==0:
                    return False
                elif stack[-1] is not '[' :
                    return False
                else:
                    stack.pop()
            elif  i is '}':
                if len(stack)==0:
                    return False
                elif stack[-1] is not '{' :
                    return False
                else:
                    stack.pop()
            

        if len(stack) != 0:
            return False
        
        return True
            
            
        