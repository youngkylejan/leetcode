class MinStack {
private:
    stack<int> number;
    stack<int> mins;
public:
    void push(int x) {
        number.push(x);
        if (mins.empty() || mins.top() >= x) {
            mins.push(x);
        }
    }
    void pop() {
        if (number.empty()) {
            return;
        }
        if (number.top() == mins.top()) {
            mins.pop();
        }
        number.pop();
    }
    int top() {
        return number.top();
    }
    int getMin() {
        return mins.top();
    }
};