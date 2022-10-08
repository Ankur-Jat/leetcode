
/**
Leetcode: https://leetcode.com/problems/3sum-closest/
Date: 8-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
*/

import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int arrLength = nums.length;
        int sum = nums[0] + nums[1] + nums[arrLength - 1];
        int closestDiff = Math.abs(target - sum);
        for (int i = 0; i < arrLength - 2; i++) {
            int start = i + 1;
            int end = arrLength - 1;
            while (start < end) {
                int localSum = nums[i] + nums[start] + nums[end];
                int localDiff = Math.abs(target - localSum);
                if (localDiff < closestDiff) {
                    closestDiff = localDiff;
                    sum = localSum;
                } else if (localDiff == 0) {
                    return localSum;
                }
                if (localSum < target) {
                    start += 1;
                } else {
                    end -= 1;
                }
            }
        }
        return sum;
    }

}

class ThreeSumClosest {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        int[] nums = { 1, 4, 5, 8, 2, 3 };
        int closestDiff = solution.threeSumClosest(nums, 14);
        if (closestDiff != 14) {
            throw new Exception("Invalid threesum closest");
        }
    }
}