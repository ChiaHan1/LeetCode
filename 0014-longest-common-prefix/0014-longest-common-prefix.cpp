#include <string>
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string common = "";
        for (int i = 0; i < strs[0].length(); i++) {
            for (int j = 1; j < strs.size(); j++) {
                if (strs[0][i] != strs[j][i]) {
                    return common;
                }
            }
            common += strs[0][i];
        }
        return common;
    }
};