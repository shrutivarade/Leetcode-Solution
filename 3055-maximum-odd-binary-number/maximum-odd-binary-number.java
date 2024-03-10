class Solution {
    public String maximumOddBinaryNumber(String s) {

        // Hint 1
        // The binary representation of an odd number contains '1' in the least significant place.

        // Soluton 1:
        // return Arrays.stream(s.split("")).sorted(Comparator.reverseOrder()).skip(1).collect(Collectors.joining()) + "1";


        // Solution 2:
        int count_1 = 0, count_0 = 0, i = 0;
        for ( char ch : s.toCharArray()){
            if(ch=='1'){
                count_1++;
            }
            else{
                count_0++;
            }
        }

        char[] result = new char[s.length()];
        while(i < count_1 - 1) {
            result[i++] = '1';
        }        
        while(i < count_1 - 1 + count_0) {
            result[i++] = '0';
        }
        result[i] = '1';
        
        return new String(result);

    }
}