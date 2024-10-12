class Solution {
    public int getSum(int a, int b) {

        while (b!=0){
            int tmp = (a&b)<<1; // logical AND and shift all bits to left by 1
            a = a^b; // logical XOR
            b = tmp;
        }
        return a;
    }
}