class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        if (tokens.size() <= 0)
            return 0;

        int value = 0;

        stack<int> s;

        for (int i = 0; i < tokens.size(); i++) {
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/" )
                s.push(stoi(tokens[i]));
            else {
                int b = s.top();
                s.pop();
                int a = s.top();
                s.pop();
                if (tokens[i] == "+")
                    s.push(a + b);
                else if (tokens[i] == "-")
                    s.push(a - b);
                else if (tokens[i] == "*")
                    s.push(a * b);
                else
                    s.push(a / b);
            }
        }

        return s.top();
    }
};