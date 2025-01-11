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

        
    }
}