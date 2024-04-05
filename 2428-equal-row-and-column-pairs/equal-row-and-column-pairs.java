class Solution {
    public int equalPairs(int[][] grid) {

        //create a hm to keep track of number of times a given row occurs
        HashMap<List<Integer>, Integer> map = new HashMap<>();
        int n = grid.length; // number odf rows

        // iterate over each row, create a arraylist for each row and put it as a key in hm
        for (int i=0; i<n; i++){
            List<Integer> row = new ArrayList<>();
            for(int j=0; j<grid[0].length;j++){
                row.add(grid[i][j]);
            }
            map.put(row, map.getOrDefault(row,0)+1);
        }

        // iterate over each column, create a arraylist for each column and check if it is present in hm.
        int count = 0;
        for (int i=0; i<n; i++){
            List<Integer> col = new ArrayList<>();
            for(int j=0; j<grid[0].length;j++){
                col.add(grid[j][i]);
            }
            if(map.containsKey(col)){
                count+=map.get(col);
            }
        }
        return count;
    }
}