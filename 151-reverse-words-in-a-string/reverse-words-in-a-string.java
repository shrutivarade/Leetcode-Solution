class Solution {
    public String reverseWords(String s) {

        //  Remove leading and trailing spaces
        // s = s.strip()

        s = s.trim();

        // # Split the string into a list of words
        // words = s.split()

        // Split the string into a list of words using spaces as the delimiter
        String[] words = s.split("\\s+"); 
        // "\\s+" matches one or more whitespace characters

        
        // # Reverse the list of words
        // words.reverse()
        int start = 0;
        int end = words.length - 1;
        while (start < end) {
            // Swap the elements at start and end indices
            String temp = words[start];
            words[start] = words[end];
            words[end] = temp;

            // Move the start index forward and end index backward
            start++;
            end--;
        }

        // # Convert the list of words back to a space-separated string
        // reversed_string = ' '.join(words)
        
        return String.join(" ", words);
    }
}