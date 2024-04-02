class Solution {
    public int largestAltitude(int[] gain) {

        int alt=0, sum=0, max=0 ;

        for(int g: gain){
            sum = sum + g;
            max = Math.max(max, sum);
        }

        return max;

    }
}