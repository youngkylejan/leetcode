class Solution {
public:
    struct node{
        int key;
        string szRoman;
        node(int k, string s):key(k), szRoman(s){}
    };
    string intToRoman(int num){
        vector<node> dct;
        dct.push_back(node(1000, "M"));
        dct.push_back(node(900,  "CM"));
        dct.push_back(node(500,  "D"));
        dct.push_back(node(400,  "CD"));
        dct.push_back(node(100,  "C"));
        dct.push_back(node(90,   "XC"));
        dct.push_back(node(50,   "L"));
        dct.push_back(node(40,   "XL"));
        dct.push_back(node(10,   "X"));
        dct.push_back(node(9,   "IX"));
        dct.push_back(node(5,   "V"));
        dct.push_back(node(4,   "IV"));
        dct.push_back(node(1,   "I"));
        string res;
        int i = 0;
        while(num > 0)
        {
            if(num/dct[i].key == 0)
            {
                i += 1;
                continue;
            }
            for(int j = 0; j < num/dct[i].key; ++j)
                res.append(dct[i].szRoman);
            num%=dct[i].key;
        }
        return res;
    }
};