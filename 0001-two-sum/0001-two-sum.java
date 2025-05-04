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
        
        // If no solution is found
        return new int[]{-1, -1};
    }
}
/**
    Time Complexity: O(N) - for loop
    Space Complexity: O(N) - hashmap
 */
