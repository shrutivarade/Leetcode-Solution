class Solution {
    public boolean isRobotBounded(String instructions) {

        int x = 0, y = 0;
        String direction = "North";

        for(char ch : instructions.toCharArray()){
            if ( ch=='L'){
                //change direction
                if(direction=="North"){
                    direction = "West";
                }else if(direction=="West"){
                    direction = "South";
                }else if(direction=="South"){
                    direction = "East";
                }else{
                    direction = "North";
                }


            }
            else if( ch == 'R'){
                //change direction
                if(direction=="North"){
                    direction = "East";
                }else if(direction=="East"){
                    direction = "South";
                }else if(direction=="South"){
                    direction = "West";
                }else{
                    direction = "North";
                }
            }else{
                if ( direction == "North" ){
                    y++;

                }else if( direction == "East" ){
                    x++;

                }else if( direction == "South"){
                    y--;

                }else{
                    x--;

                }
            }
        }

        if( x==0 && y==0 ) return true;

        if( direction == "North" ) return false;

        return true;

        // int dir[][] = {{0,1}, {-1, 0}, {0, -1}, {1,0}};
        // int i = 0;
        // int x = 0;
        // int y = 0;
       
        // for(int s = 0; s < instructions.length(); s++){
        //     if(instructions.charAt(s) == 'L'){
        //         i = (i + 1) % 4;
        //     }
        //     else if(instructions.charAt(s) == 'R'){
        //         i = (i + 3) % 4;
        //     }
        //     else{
        //         x = x + dir[i][0];
        //         y = y + dir[i][1];
        //     }
        // }
        // return x == 0 && y == 0 || i != 0;

        
    }
}