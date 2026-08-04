#include <map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> m1{ stringToMap(s) };
        map<char, int> m2{ stringToMap(t) };
        return m1 == m2;
    }

    std::map<char, int> stringToMap(string s) {
        map<char, int> m;
        for (char c: s) {
            if (m.find(c) != m.end()) { m[c] += 1; }
            else { m[c] = 1; }
        } 
        return m;
    }
};
