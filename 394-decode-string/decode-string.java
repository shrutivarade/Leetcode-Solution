class Solution {
    public String decodeString(String s) {
        Stack<Character> st = new Stack<>();
        StringBuilder sb = new StringBuilder();
        
        for(char ch:s.toCharArray()){

            if(ch!=']'){
                st.push(ch);
            }

            else{
                //for letter
                sb = new StringBuilder();
                while(!st.isEmpty() && Character.isLetter(st.peek())){
                    sb.insert(0,st.pop());
                }
                st.pop(); // remove'['
                String temp = sb.toString(); 
                
                // for digit
                sb=new StringBuilder();
                while(!st.isEmpty() && Character.isDigit(st.peek())){
                    sb.insert(0,st.pop());
                }
                int count=Integer.valueOf(sb.toString());


                while( count > 0){
                    for(char c:temp.toCharArray()){
                        st.push(c);
                    }
                    count--;
                }

            }
        }


        sb=new StringBuilder();
        while(!st.isEmpty()){
            sb.append(st.pop());
        }
        
        return sb.reverse().toString();
    }
}