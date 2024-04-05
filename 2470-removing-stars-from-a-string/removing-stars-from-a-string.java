class Solution {
    public String removeStars(String s) {
        
        Stack<Character> stack = new Stack<Character>();
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)!='*'){
                stack.push(s.charAt(i));
            }
            else{
                stack.pop();
            }
            
        }

        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }

        sb.reverse();

        return sb.toString();


        // without using stack
        // char arr[]=s.toCharArray();
        // StringBuilder sb=new StringBuilder();
        // for(char c:arr){
        //     if(c=='*'){
        //         sb.setLength(sb.length()-1); // similar to pop operation in stack
        //     }
        //     else{
        //         sb.append(c); // similar to push operation in stack
        //     }
        // }
        // return sb.toString();

    }
}