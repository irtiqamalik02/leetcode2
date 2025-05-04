import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // Check if the complement exists in the map
            if (hash.containsKey(complement)) {
                return new int[]{hash.get(complement), i}; // Return indices
            }
            
            // Store the current number and its index
            hash.put(nums[i], i);
        }
        
        // In case there is no solution, return an empty array
        return new int[] {};
    }
}
/**
    Time Complexity: O(N) - for loop
    Space Complexity: O(N) - hashmap
 */
