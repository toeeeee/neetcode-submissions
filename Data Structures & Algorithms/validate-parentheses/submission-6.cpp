class Solution {
public:
    void matchPair(stack<char>& st, char start, bool& valid) {
        if (st.empty()) { valid = false; return; }

        if (st.top() != start) { valid = false; }
        else { st.pop(); }
    }

    bool isValid(string s) {
        stack<char> st;
        bool valid{true};

        for (char ch: s) {
            switch(ch) {
                case '(':
                    st.push(ch); break;
                case '[':
                    st.push(ch); break;
                case '{':
                    st.push(ch); break;
                case ')':
                    matchPair(st, '(', valid);
                    break;
                case ']':
                    cout << "here";
                    matchPair(st, '[', valid);
                    break;
                case '}':
                    matchPair(st, '{', valid);
                    break;
            }
        }

        return ((st.empty()) ? valid : false);
    }
};
