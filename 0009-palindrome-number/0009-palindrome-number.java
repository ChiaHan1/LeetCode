class Solution {
    public boolean isPalindrome(int x) {
        
        if (x == 0) {
            return true;
        }
        
        if (x < 0 || x % 10 == 0) {
            return false;
        }
        
        int reverse = 0;
        
        while (reverse < x) {
            reverse = reverse * 10 + x % 10;
            x /= 10;
        }
        
        if (reverse == x || (reverse / 10) == x) {
            return true;
        } else {
            return false;
        }
        
    }
}