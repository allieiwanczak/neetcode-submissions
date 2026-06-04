class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        vector<int> res;

        for (int &x: nums) {
            freq[x]++;
        }

        for (auto& entry: freq) {
            heap.push({entry.second, entry.first});
            if (heap.size() > k) {
                heap.pop();
            }
        }

        for (int i = 0 ; i <k; i++) {
            res.push_back(heap.top().second);
            heap.pop();
        }
        
        return res;


    }
};
