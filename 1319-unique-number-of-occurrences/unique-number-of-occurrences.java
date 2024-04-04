class Solution {
    public boolean uniqueOccurrences(int[] arr) {

        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int a : arr){
            if(map.containsKey(a)){
                map.put(a, map.get(a)+1);
            }
            else{
                map.put(a,1);
            }
        }

        Set<Integer> valueSet = new HashSet<>(map.values());

        return map.size() == valueSet.size();
        
    }
}