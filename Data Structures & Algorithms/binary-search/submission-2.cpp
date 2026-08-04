class Solution {
public:
    int search(vector<int>& nums, int target) {
        return searchWithBounds(nums, 0, nums.size(), target);
    }

    int searchWithBounds(vector<int>& nums, int l, int r, int target) {
        if (r < l || l > r) { return -1; }
        
        int midI = (l+r)/2;
        int midVal = nums[midI];
        cout << l << ' ' << r << ' ' << midI << endl;
        if (midVal == target) { return midI; }
        if (midVal > target) { return searchWithBounds(nums, l, midI-1, target); } 
        if (midVal < target) { return searchWithBounds(nums, midI+1, r, target); } 
    }
};
