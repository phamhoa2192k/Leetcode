#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        int size = nums.size();
        sort(nums.begin(), nums.end());
//        vector<vector<int>> matrix (size, vector<int> (size));
        vector<int> result;
        vector<int> matrix (size);
        matrix[0] = nums[0];
        for (int i = 1; i < size; i++) {
            matrix[i] = matrix[i - 1] + nums[i];
        }
        for (auto i : queries) {
            for (int j = 0; j < matrix.size(); j++) {
                if (j == 0 && i < matrix[j]) {
                    result.push_back(0);
                    break;
                } else if (i < matrix[j]) {
                    result.push_back(j);
                    break;
                } else if (j == matrix.size() - 1 && i >= matrix[j]) {
                    result.push_back(size);
                }
            }
        }
        return result;
    }
};


int main() {
    Solution s;
    vector<int> nums {1}, queries {1};
    for (auto i : s.answerQueries(nums, queries)) {
        cout << i << " ";
    }
}
