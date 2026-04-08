class Solution {
    // merge sort TC: nlog(n) SC: O(n)
    public void merge(int[] nums, int l, int m, int r) {
        int i = l, j = m+1, k = 0;
        int[] temp = new int[r-l+1];
        while (i <= m && j <= r) {
            if (nums[i] < nums[j]) {
                temp[k++] = nums[i++];
            } else {
                temp[k++] = nums[j++];
            }
        }
        while (i <= m) {
            temp[k++] = nums[i++];
        }
        while (j <= r) {
            temp[k++] = nums[j++];
        }

        for (i=0; i<temp.length; i++) {
            nums[i+l] = temp[i];
        }
    }

    public void mergeSort(int[] nums, int l, int r) {
        if (l == r) return;
        int m = (l+r) / 2;
        mergeSort(nums, l, m);
        mergeSort(nums, m+1, r);
        merge(nums, l, m, r);
    }

    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length-1);
        return nums;
    }
}