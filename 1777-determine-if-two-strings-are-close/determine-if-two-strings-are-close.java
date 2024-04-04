class Solution {
    public boolean closeStrings(String word1, String word2) {
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];
        for (char ch : word1.toCharArray()) {
            freq1[ch - 'a']++;
        }
        for (char ch : word2.toCharArray()) {
            freq2[ch - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if ((freq1[i] == 0 && freq2[i] != 0) || (freq1[i] != 0 && freq2[i] == 0)) {
                return false;
            }
        }
        Arrays.sort(freq1);
        Arrays.sort(freq2);
        for (int i = 0; i < 26; i++) {
            if (freq1[i] != freq2[i]) {
                return false;
            }
        }
        return true;
    }
}


// class Solution {
//     public boolean closeStrings(String word1, String word2) {

//         if(word1.length()!=word2.length()){
//             return false;
//         }

//         // Count occurrences of each character in both words
//         Map<Character, Integer> map1 = new HashMap<>();
//         Map<Character, Integer> map2 = new HashMap<>();

//         for(int i=0; i<word1.length(); i++){
//             map1.put(word1.charAt(i), map1.getOrDefault(word1.charAt(i),0)+1);
//             map2.put(word2.charAt(i), map2.getOrDefault(word2.charAt(i),0)+1);
//         }

//         // Check if both words have the same set of keySets
//         if (!map1.keySet().equals(map2.keySet())) {
//             return false;
//         }

//         // Check if both words have the same set of valueSets
//         // Convert values (counts) to sets
//         // Set<Integer> v1 = new HashSet<>(map1.values());
//         // Set<Integer> v2 = new HashSet<>(map2.values());

//         // Compare sets of frequencies
//         // return v1.equals(v2);

//         // Set do not work for examples such as:
//         // word1:"aaabbbbccddeeeeefffff"
//         // word2:"aaaaabbcccdddeeeeffff"
//         // map1:{"a":3,"b":4,"c":2,"d":2,"e":5,"f":5}
//         // map2:{"a":5,"b":2,"c":3,"d":3,"e":4,"f":4}
//         // v1:[2, 3, 4, 5]
//         // v2:[2, 3, 4, 5]


//         // LETS USE LIST AND SORT IT, AND THEN EQUATE

//         List<Integer> v1 = new ArrayList<>(map1.values());
//         List<Integer> v2 = new ArrayList<>(map2.values());

//         Collections.sort(v1);
//         Collections.sort(v2);

//         return v1.equals(v2);
//     }
// }