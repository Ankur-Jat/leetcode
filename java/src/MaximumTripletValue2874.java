class Solution {

    public long maximumTripletValue(int[] nums) {
        int n = nums.length;
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];
        for(int i=1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i-1], nums[i-1]);
            rightMax[n - i - 1] = Math.max(rightMax[n - i],nums[n - i]);
        }
        long maxTripletValue = 0;
        for (int i=1; i < n - 1; i++) {
            maxTripletValue = Math.max(
                maxTripletValue,
                (long) ((leftMax[i] - nums[i]) * rightMax[i])
            );
        }

        return maxTripletValue;
    }
}

class MaximumTripletValue2874 {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        int[] nums = { 1000000,1,1000000 };
        long maximumTripletValue = solution.maximumTripletValue(nums, 14);
        if (maximumTripletValue != 999999000000) {
            throw new Exception("Invalid maximumTripletValue");
        }
    }
}