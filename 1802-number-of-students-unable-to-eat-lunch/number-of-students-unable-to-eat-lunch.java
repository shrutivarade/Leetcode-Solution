class Solution {
    public int countStudents(int[] students, int[] sandwiches) {

        // Using stack and queue
        // int len = students.length;
        // Queue<Integer> studentQueue = new LinkedList<>();
        // for (int student : students)
        //     studentQueue.add(student);

        // Stack<Integer> sandwichStack = new Stack<>();
        // for (int i = len - 1; i >= 0; i--)
        //     sandwichStack.push(sandwiches[i]);

        // int servedAgain = 0;
        // while (!studentQueue.isEmpty() && servedAgain < studentQueue.size()) {
        //     if (sandwichStack.peek().equals(studentQueue.peek())) {
        //         sandwichStack.pop();
        //         studentQueue.poll();
        //         servedAgain = 0;
        //     } else {
        //         studentQueue.add(studentQueue.peek());
        //         studentQueue.poll();
        //         servedAgain++;
        //     }
        // }
        // return studentQueue.size();


        // Using array and pointer
        int[] preferenceCount = {0, 0};

        // Count the number of students with each preference
        for (int i = 0; i < students.length; i++) {
            preferenceCount[students[i]]++;
        }

        int notServedCount = 0;
        // Try to serve sandwiches to students
        for (int i = 0; i < sandwiches.length; i++) {
            if (preferenceCount[sandwiches[i]] > 0) {
                // Serve the sandwich to a student with this preference
                preferenceCount[sandwiches[i]]--;
            } else {
                // If no students with this preference remain, stop serving sandwiches
                break;
            }
        }

        // Count the number of students who couldn't get their preferred sandwiches
        for (int count : preferenceCount) {
            notServedCount += count;
        }

        return notServedCount;
    }
}