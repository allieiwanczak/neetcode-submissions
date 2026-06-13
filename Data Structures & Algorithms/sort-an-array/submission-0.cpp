class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
       // merge sort
       mergeSort(nums, 0, nums.size()-1);
    return nums;
    }
private:
    void mergeSort(vector<int>&arr, int l , int r) {
        if (l>=r) return;
        int mid = l + (r-l) /2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid+1, r);
        merge(arr, l, mid, r);
    }
    void merge(vector<int>&arr, int l, int m, int r) {
        vector<int> L(arr.begin()+l, arr.begin()+m+1);
        vector<int> R(arr.begin()+m+1, arr.begin()+r+1);

        int i = 0, j=0, k=l;
        while (i<L.size()&& j<R.size()) {
            if (L[i]<= R[j]) arr[k++] = L[i++];
            else arr[k++] = R[j++];
        }
        while (i<L.size()) arr[k++]=L[i++];
        while (j<R.size()) arr[k++]=R[j++];
        
    }
};