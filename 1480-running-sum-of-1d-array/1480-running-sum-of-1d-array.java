class Solution {
    public int[] runningSum(int[] nums) {
        
        int length = nums.length;
        int total = nums[0];
        
        for (int i = 1; i < length; i++) {
            total += nums[i];
            nums[i] = total;
        }
        
        return nums;
    }
}