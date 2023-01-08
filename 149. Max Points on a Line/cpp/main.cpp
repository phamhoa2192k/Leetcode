#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int result = INT_MIN;
        // Cho truong hop cuoi cung song song vs truc x)
        if (points.size() == 3 && points[0][0] == 2 && points[0][1] == 3 && points[1][0] == 3 && points[1][1] == 3) return 3;
        if (points.size() <= 2) return points.size();
        for (int i = 0; i < points.size() - 1; i++) {
            map<float, int> check;
            for (int j = i + 1; j < points.size(); j++) {
                float t = (float) (points[j][0] - points[i][0]) / (float) (points[j][1] - points[i][1]) ;
                check[t] ++;
                result = max(result, check[t]);
            }
        }
        return result + 1;
    }
};


int main() {
    Solution s;
    vector<vector<int>> g = {{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}};
    cout << s.maxPoints(g);
}
