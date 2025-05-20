class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Step 1: Count frequencies using HashMap
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Step 2: Group numbers by frequency using TreeMap (descending order)
        TreeMap<Integer, List<Integer>> bucket = new TreeMap<>(Collections.reverseOrder());
        for (int num : freqMap.keySet()) {
            int freq = freqMap.get(num);
            bucket.putIfAbsent(freq, new ArrayList<>());
            bucket.get(freq).add(num);
        }

        // Step 3: Collect top K frequent elements
        List<Integer> result = new ArrayList<>();
        for (int freq : bucket.keySet()) {
            for (int num : bucket.get(freq)) {
                result.add(num);
                k--;
                if (k == 0) break; // break inner
            }
            if (k == 0) break; // break outer as well!
        }

        // Step 4: Convert to int[]
        int[] ans = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            ans[i] = result.get(i);
        }

        return ans;
    }
}
