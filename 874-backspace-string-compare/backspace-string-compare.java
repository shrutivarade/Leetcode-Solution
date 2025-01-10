class Solution {
    public boolean backspaceCompare(String s, String t) {

        Stack<Character> stack_s = new Stack<>();
        
        for (char ch : s.toCharArray()){
            if ( !stack_s.isEmpty() && ch == '#'){
                stack_s.pop();
                continue;
            }else if (ch == '#'){
                continue;
            }
            stack_s.push(ch);
        }

        Stack<Character> stack_t = new Stack<>();
        
        for (char ch : t.toCharArray()){
            if ( !stack_t.isEmpty() && ch == '#'){
                stack_t.pop();
                continue;
            }
            else if (ch == '#'){
                continue;
            }
            stack_t.push(ch);
        }

        // for ( int i=t.length()-1; i>=0; i--){
        //     if (t.charAt(i) == '#') {
        //         i-=1;
        //         continue;
        //     }
        //     if (!stack.isEmpty() && t.charAt(i) != stack.pop()){
        //         return false;
        //     }

        // }

        return stack_s.equals(stack_t);

        
    }
}