class Solution {
    public int prefixCount(String[] words, String pref) {
        
        int n = pref.length(), count=0;
        for( String str : words){
            if (str.length()>=n && str.substring(0,n).equals(pref)){
                count++;
            }
        }
        return count;
    }
}