class Solution {
    public int romanToInt(String s) {
        Map<String,Integer> value = new HashMap<String, Integer>();
        value.put("I", 1);
        value.put("V", 5);
        value.put("X", 10);
        value.put("L", 50);
        value.put("C", 100);
        value.put("D", 500);
        value.put("M", 1000);

        int sum = 0;
        int i = 0;

        while(i<s.length()){
            String curkey = s.substring(i,i+1);
            int curval = value.get(curkey);
            int nextval = 0;
            if( i+1 < s.length()){
                String nextkey = s.substring(i+1, i+2);
                nextval = value.get(nextkey);
            }
            if(curval < nextval){
                sum = sum + (nextval - curval); 
                i = i+2;
            }else{
                sum = sum + curval;
                i=i+1; 
            }
        }
        return sum;
    }
}