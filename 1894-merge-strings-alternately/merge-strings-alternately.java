class Solution {
    public String mergeAlternately(String word1, String word2) {

        // StringBuilder result = new StringBuilder();
        
        // int i = 0;
        // while (i < word1.length() || i < word2.length()){
        //     if(i < word1.length()){
        //         result.append(word1.charAt(i));
        //     }
        //     if(i < word2.length()){
        //         result.append(word2.charAt(i));
        //     }
        //     i++;
        // }

        // for (int i =0; i < word1.length() || i < word2.length(); i++){
        //     if(i < word1.length()){
        //         result.append(word1.charAt(i));
        //     }
        //     if(i < word2.length()){
        //         result.append(word2.charAt(i));
        //     }
        // }
        // return result.toString();


        String result = "";
        int maxLength = Math.max(word1.length(), word2.length());
        for (int i = 0; i < maxLength; i++) {
            if (i < word1.length()) {
                result += word1.charAt(i);
            }
            if (i < word2.length()) {
                result += word2.charAt(i);
            }
        }
        return result;

    }
}

