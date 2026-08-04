class Solution {
public:
    bool isPalindrome(string s) {
        auto l{s.begin()}; auto r{s.end()-1};
        while (l != r) {
            if (l == s.end() || r == s.begin()-1) { return true; }
            while (!isalnum(*l) && l != r) {++l; continue;}
            while (!isalnum(*r) && l != r) {--r; continue;}
            if (tolower(*l) != tolower(*r)) { 
                return false; 
            }
            ++l;
            --r;
        } 
        return true;
    }
};
