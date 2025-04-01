class Solution {
    public long mostPoints(int[][] questions) {
        int questionsSize = questions.length;
        long[] scoreMetrics = new long[questionsSize];
        scoreMetrics[questionsSize - 1] = questions[questionsSize - 1][0];
        for (int index = questionsSize - 2; index > -1; index--) {
            int nextIndex = index + questions[index][1] + 1;
            if (nextIndex >= questionsSize) {
                scoreMetrics[index] = Math.max(questions[index][0], scoreMetrics[index+1]);
            } else {
                scoreMetrics[index] = Math.max(questions[index][0] + scoreMetrics[nextIndex], scoreMetrics[index+1]);
            }
        }
        return scoreMetrics[0];
    }
}

class SolvingQuestionsWithBrainPower {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        int[][] questions = { { 1, 1 }, { 2, 2 }, { 3, 3 } };
        long mostPoints = solution.mostPoints(questions);
        if (mostPoints != 4) {
            throw new Exception("Invalid most points");
        }
    }
}