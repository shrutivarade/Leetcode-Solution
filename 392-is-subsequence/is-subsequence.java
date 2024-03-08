class Solution {
    public boolean isSubsequence(String s, String t) {

            String count = "";
            int j=0;

            for(int i=0; i<s.length(); i++){
                while( j<t.length()){
                    if(s.charAt(i) == t.charAt(j)){
                        count = count + s.charAt(i);
                        j = j+1;
                        break;
                    }
                    j = j+1;
                }
            }

            if(s.equals(count)){
                return true;
            }
            else{
                return false;
            }



    }
}