class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // size of nums array
        int n = nums.size();
        
        // to ensure k is within the range
        k = k % n;
        
        // reverse the first n - k elements
        reverse(nums.begin(), nums.begin() + (n - k));
        
        // reverse the second part of the array
        reverse(nums.begin() + (n - k), nums.end());
        
        // reverse the entire array
        reverse(nums.begin(), nums.end());
    }
};