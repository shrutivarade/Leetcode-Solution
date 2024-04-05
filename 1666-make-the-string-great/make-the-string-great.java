class Solution {
    public String makeGood(String s) {

        if(s.length()==1 || s.length()==0){
            return s;
        }

        Stack<Character> stack = new Stack<>();
        
        for(char ch : s.toCharArray()){
            if(stack.isEmpty()){
                stack.push(ch);
            }
            else if(Character.isUpperCase(ch)){
                if(stack.peek() == Character.toLowerCase(ch)){
                    stack.pop();
                }
                else{
                    stack.push(ch);
                }
            }
            else if(Character.isLowerCase(ch)){
                if(stack.peek() == Character.toUpperCase(ch)){
                    stack.pop();
                }
                else{
                    stack.push(ch);
                }
            }
            
        }

        StringBuilder sb = new StringBuilder();
        for(int i=stack.size()-1; i>=0; i--){
            sb.append(stack.pop());
        }
        sb.reverse();

        return sb.toString();
    }
}