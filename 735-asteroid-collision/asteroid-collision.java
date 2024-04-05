class Solution {
    public int[] asteroidCollision(int[] asteroids) {

        Stack<Integer> stack = new Stack<>();

        for(int a : asteroids){
            // add positive values to stack
            if(stack.isEmpty() || a>0){
                stack.add(a);
            }
            else{

                while(true){
                    int top = stack.peek();

                    if(top<0){ // top is having negative number and a is also having negative, same direction
                        stack.add(a);
                        break;
                    }
                    else if(top == -a){ // top is positive but a is negative with same value opposite and direction, both explode
                        stack.pop();
                        break;
                    }
                    else if(top > -a){
                        break; // do nothing, mean do not add a to stack
                    }
                    else{
                        stack.pop();
                        if(stack.isEmpty()){
                            stack.add(a);
                            break;
                        }
                    }
                }
            }
        }


        int []ans=new int[stack.size()];
        for(int i=stack.size()-1;i>=0;i--){
            ans[i]=stack.pop();
        }
        return ans;

        
        
    }
}



// class Solution {
//     public int[] asteroidCollision(int[] asteroids) {
//         Stack<Integer> st = new Stack<Integer>();

//         for (int asteroid : asteroids) {
//             boolean flag = true;
//             while (!st.isEmpty() && (st.peek() > 0 && asteroid < 0)) {
//                 // If the top asteroid in the stack is smaller, then it will explode.
//                 // Hence pop it from the stack, also continue with the next asteroid in the stack.
//                 if (Math.abs(st.peek()) < Math.abs(asteroid)) {
//                     st.pop();
//                     continue;
//                 }
//                 // If both asteroids have the same size, then both asteroids will explode.
//                 // Pop the asteroid from the stack; also, we won't push the current asteroid to the stack.
//                 else if (Math.abs(st.peek()) == Math.abs(asteroid)) {
//                     st.pop();
//                 }

//                 // If we reach here, the current asteroid will be destroyed
//                 // Hence, we should not add it to the stack
//                 flag = false;
//                 break;
//             }

//             if (flag) {
//                 st.push(asteroid);
//             }
//         }

//         // Add the asteroids from the stack to the vector in the reverse order.
//         int[] remainingAsteroids = new int[st.size()];
//         for (int i = remainingAsteroids.length - 1; i >= 0; i--) {
//             remainingAsteroids[i] = st.pop();
//         }

//         return remainingAsteroids;
//     }
// }