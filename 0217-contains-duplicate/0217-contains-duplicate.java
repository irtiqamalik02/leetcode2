class Solution {
    public boolean containsDuplicate(int[] nums) {
        if(nums.length == 1) return false;
        Set<Integer> uniques = new HashSet<>(nums.length);
        for(int i: nums){
            if(uniques.contains(i)) return true;
            uniques.add(i);
        }
        return false;
    }
}

// Time Complexity: O(n) - search (loop) and insert n times
// Space Complexity: O(n) - hash table of size n