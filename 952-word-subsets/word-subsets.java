class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {

        // // Hashmap: counter of word2 characters
        HashMap<String, Map<Character, Integer>> map = new HashMap<>();

        for (String word : words2) {
            Map<Character, Integer> freqMap = new HashMap<>();
            for (char ch : word.toCharArray()) {
                freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
            }
            map.put(word, freqMap);
        }

         Map<Character, Integer> newMap = new HashMap<>();
        for (Map<Character, Integer> letters_map : map.values()){
            for (Map.Entry<Character, Integer> entry : letters_map.entrySet()) {
                char key = entry.getKey();
                int value;
                if (newMap.containsKey(key)){
                    value =  Math.max(newMap.get(key),entry.getValue());
                }
                else{
                    value = entry.getValue();
                }
                newMap.put(key,value);
            }

        }

        List<String> res = new ArrayList<String>();
        for (String word : words1){
            boolean flag = true;
            for ( char ch_key : newMap.keySet()){   
                if(newMap.get(ch_key) > word.chars().filter(c -> c == ch_key).count()){
                    flag = false;
                    break;
                }
            }
            if (flag) {
                res.add(word);
            }
        }
        return res; 

        
        // for (String word1 : words1){
        //     Map<Character, Integer> wordMap = new HashMap<>();
        //     for (char ch : word1.toCharArray()) {
        //         wordMap.put(ch, wordMap.getOrDefault(ch, 0) + 1);
        //     }

        //     boolean isSubset = true;
        //     for(Map.Entry<String, Map<Character, Integer>> entry : map.entrySet()){
        //         char ch = entry.getKey();
        //         int requiredCount = entry.getValue();
        //         if (wordMap.getOrDefault(ch, 0) < requiredCount) {
        //             isSubset = false;
        //             break;
        //         }

        //     }

        //     if (isSubset) {
        //         res.add(word1);
        //     }
        // }

        
        // return res;


        


        // List<String> res = new ArrayList<String>();
        // for (String word1 : words1){
        //     boolean flag = true;
        //     for ( String word2 : words2){
        //         if ( !word2.chars().allMatch( ch -> word1.chars().filter(c -> c == ch).count() >= word2.chars().filter(c -> c==ch).count())){
        //             flag = false;
        //             break;

        //         }
        //     }
        //     if (flag) {
        //         res.add(word1);
        //     }
        // }
        // return res; 


        
        // // Hashmap: counter of word2 characters
        // HashMap<Character, Integer> map = new HashMap<>();
        // List<String> res = new ArrayList<String>();

        // for (String word : words2){
        //     for ( char ch : word.toCharArray()){
        //         map.put( ch, Math.max(map.getOrDefault(ch,0)+1, map.get(ch),));
        //     }
        // }

        // for (String word : words1){
        //     boolean flag = true;
        //     for ( char ch_key : map.keySet()){   
        //         if(map.get(ch_key) > word.chars().filter(c -> c == ch_key).count()){
        //             flag = false;
        //             break;
        //         }
        //     }
        //     if (flag) {
        //         res.add(word);
        //     }
        // }
        // return res; 
    }
}