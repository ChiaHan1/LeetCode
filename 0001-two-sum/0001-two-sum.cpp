class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // map[number] = index
        unordered_map<int, int> map;

        // number of elements in nums
        int n = nums.size();

        // build the hash table of the numbers
        for (int i = 0; i < n; i++) {
            map[nums[i]] = i;
        }

        // find the pair
        for (int i = 0; i < n; i++) {
            if (map.find(target - nums[i]) != map.end() && map[target - nums[i]] != i) {
                return {i, map[target - nums[i]]};
            }
        }
        return {};
    }
};