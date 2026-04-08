class Solution {
    public int[] sortArray(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        int max = nums[0], min = nums[0];
        for (int i : nums) {
            counter.put(i, counter.getOrDefault(i, 0) + 1);
            max = Math.max(max, i);
            min = Math.min(min, i);
        }

        int j = 0;
        for (int i = min; i <= max; i++) {
            while (counter.getOrDefault(i, 0) > 0) {
                nums[j++] = i;
                counter.put(i, counter.get(i)-1);
            }
        }

        return nums;
    }
}