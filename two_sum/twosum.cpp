class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int v=nums.size();
        for(int i=0;i<v;i++){
            for(int j=i+1;j<v;j++){
                int sum=nums[i]+nums[j];
                if(sum==target)
                    return {i,j};
            }
        }
        return {};
    }
};
