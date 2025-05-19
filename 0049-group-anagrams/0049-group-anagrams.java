class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // use sorted as key and collect
        HashMap<String,List<String>> hash = new HashMap<>();

        for(String str : strs){
            int[] count = new int[26]; // for 'a' to 'z'
            for (char c : str.toCharArray()) {
                count[c - 'a']++;
            }

            // Convert count array to a string key
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                sb.append(count[i]).append('#'); // add delimiter to prevent overlap
            }
            String key = sb.toString();

            // add to hashmap initialisng a new list if required
            hash.putIfAbsent(sb.toString(),new ArrayList<>());
            hash.get(sb.toString()).add(str);
        }

        // group all anagrams gogether

        return new ArrayList<>(hash.values());

    }
}

/** 
    Time Complexity: O(N * K) where,
     N = number of strings ,
     K = max length of a string

    Space Complexity: O(N * K)
*/