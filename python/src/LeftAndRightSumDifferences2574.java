class Solution {
    public int[] leftRightDifference(int[] nums) {
        int numsSum = Arrays.stream(nums).sum();
        int leftSum = 0;
        int numsLen = nums.length;
        int[] result = new int[numsLen];
        for(int i = 0; i < numsLen; i++) {
            numsSum -= nums[i];
            result[i] = Math.abs(numsSum - leftSum);
            leftSum += nums[i];
        }
        return result;
    }
}


class LeftAndRightSumDifferences2574 {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        int[] nums = { 1, 2, 3, 4, 5 };
        int[] result = solution.leftRightDifference(nums);
        if (result[0] != 14 || result[1] != 10 || result[2] != 6 || result[3] != 2 || result[4] != 0) {
            throw new Exception("Invalid left and right sum differences");
        }
        nums = new int[] { 1 };
        result = solution.leftRightDifference(nums);
        if (result[0] != 0) {
            throw new Exception("Invalid left and right sum differences");
        }
        nums = new int[] { 1, 2 };
        result = solution.leftRightDifference(nums);
        if (result[0] != 1 || result[1] != 1) {
            throw new Exception("Invalid left and right sum differences");
        }
        nums = new int[] { 1, 2, 3 };
        result = solution.leftRightDifference(nums);
        if (result[0] != 4 || result[1] != 2 || result[2] != 0) {
            throw new Exception("Invalid left and right sum differences");
        }
        nums = new int[] { 1, 2, 3, 4 };
        result = solution.leftRightDifference(nums);
    }
}