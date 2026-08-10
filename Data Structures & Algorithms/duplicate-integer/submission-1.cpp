class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> map; 
        for (auto& num: nums) {
            if (map.contains(num)) {
                return true;
            } else {
                map.insert({num, 0});
            }
        }

        return false;
    }
};