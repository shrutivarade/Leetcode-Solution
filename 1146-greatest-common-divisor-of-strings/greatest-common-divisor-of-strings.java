class Solution {
    public String gcdOfStrings(String str1, String str2) {
        
        if(!(str1+str2).equals(str2+str1)){
            return "";
        }

        int gcd = gcd(str1.length(), str2.length());
        return str1.substring(0,gcd);




    }

    // eg a = 6 and b = 3
    // gcd(b, a%b) = gcd(3,6%3=0)
    private int gcd(int a, int b){
        // if (b == 0){
        //     return a;
        // }
        // else{
        //     gcd(b, a%b);
        // }
        
        return b == 0 ? a : gcd(b, a%b);

    }
}