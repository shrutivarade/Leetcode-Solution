class Solution {
    public int equalPairs(int[][] grid) {

        //create a hm to keep track of number of times a given row occurs
        HashMap<List<Integer>, Integer> mp = new HashMap<>();
        int n=grid.length; 

        // iterate over each row, create a arraylist for each row and put it as a key in hm
        for(int i=0;i<n;i++){
            List<Integer> li=new ArrayList<>();
            for(int j=0;j<n;j++){
                li.add(grid[i][j]);
            }
             mp.put(li, mp.getOrDefault(li, 0) + 1);
        }

        // iterate over each column, create a arraylist for each column and check if it is present in hm.
        int count=0;
          for(int i=0;i<n;i++){
            List<Integer> li=new ArrayList<>();
            for(int j=0;j<n;j++){
                li.add(grid[j][i]);
            }
           if (mp.containsKey(li)){
           count+=mp.get(li);
           }
        }
        return count;
    }
}