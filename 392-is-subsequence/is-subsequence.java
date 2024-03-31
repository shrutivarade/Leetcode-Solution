class Solution {
    public boolean isSubsequence(String s, String t) {

        // 1 loop and 2 pointers, 1 for each String
        
        int i,j;
        for(i=0, j=0; i<s.length() && j<t.length(); j++){
            if(s.charAt(i) == t.charAt(j)){
                i++;
            }
        }

        if(i == s.length()){
            return true;
        }
        else{
            return false;
        }

    }
}