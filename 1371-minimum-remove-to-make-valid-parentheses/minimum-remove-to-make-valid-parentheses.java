class Solution {
    public String minRemoveToMakeValid(String s) {

        Stack<Character> stack = new Stack<>();
        int countOpen = 0;
        int countClose = 0;
        for( char ch : s.toCharArray() ) {
            if( ch == '('){
                countOpen++;
                stack.push(ch);
            }
            else if( ch == ')'){
                if(countOpen > countClose){
                    countClose++;
                    stack.push(ch);
                }
            }
            else{
                stack.push(ch);
            }
        }

        StringBuilder sb = new StringBuilder();

        while(!stack.isEmpty()){
            if(stack.peek() == '(' && countOpen != countClose){
                stack.pop();
                countOpen--;
                continue;
            }
            else{
                sb.append(stack.pop());
            }
        }

        sb.reverse();

        return sb.toString();
    }
}