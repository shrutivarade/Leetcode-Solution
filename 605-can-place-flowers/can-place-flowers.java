class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int max = 0;

        for( int i=0 ; i<flowerbed.length; i++)
        {

            if(flowerbed[i] == 0){
                boolean left, right;
                if( i == 0 || flowerbed[i-1]==0){
                    left = true;
                }
                else{
                    left = false;
                }

                if( i == flowerbed.length-1 || flowerbed[i+1]==0){
                    right = true;
                }
                else{
                    right = false;
                }
                
                if(left&&right){
                    flowerbed[i] = 1;
                    max = max + 1;
                }
            }
            
        }

        return max>=n;
    }
}

