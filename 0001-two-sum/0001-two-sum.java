class Solution {
    public int[] twoSum(int[] nums, int target) {
        // store the target - v=num alng with index

        HashMap<Integer,Integer> hash = new HashMap<>(nums.length);

        for(int i = 0 ; i < nums.length; i++){
            int n = nums[i];
            if(hash.containsKey(n)){
                return new int[]{i,hash.get(n)};
            }
            hash.put(target-n,i);
        }
        
        return new int[]{};
    }
}