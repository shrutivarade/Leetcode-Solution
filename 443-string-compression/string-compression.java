class Solution {
    public int compress(char[] chars) {
        int n = chars.length;
        StringBuilder s = new StringBuilder();
        if(n==1){
            return 1;
        }

        char letter = chars[0];
        int count = 1;
        int i;
        for(i=1; i<n; i++){
            
            if( letter==chars[i]){
                count += 1;
            }
            else{
                s.append(chars[i-1]);
                if(count>1){
                    s.append(count);
                }
                letter = chars[i];
                count = 1;
            }

        }

        s.append(chars[i-1]);
        if(count>1){
            s.append(count);
        }

        char[] result = s.toString().toCharArray();
        for(int j=0; j<result.length; j++){
            chars[j] = result[j];
        }

        return s.length();
        
    }
}