class Solution {
public:
    bool isPalindrome(string s) {
       string result = "";
        for(auto c : s){
            if(iswalnum(c) && c != ' '){
                result += tolower(c);
            }
        }
        string reverseString = "";
        for(int i = result.length()-1; i>=0; i--){
            reverseString += result.at(i);
        }
        return result == reverseString; 
    }
};
