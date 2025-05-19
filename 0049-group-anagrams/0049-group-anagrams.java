class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // use sorted as key and collect
        HashMap<String,List<String>> hash = new HashMap<>();

        for(String str : strs){
            int[] count = new int[26];
            for(char s: str.toCharArray()){
                count[s-'a']++;
            }

            // create key from this
            StringBuilder sb = new StringBuilder("");
            for(int i = 0 ; i < 26; i++){
                sb.append(count[i]);
                sb.append("#");
            }

            

            // add to hashmap initialisng a new list if required
            hash.putIfAbsent(sb.toString(),new ArrayList<>());
            hash.get(sb.toString()).add(str);
        }

        // group all anagrams gogether

        return new ArrayList<>(hash.values());

    }
}

/** 
    Time Complexity: O(N * K log K) where,
     N = number of strings ,
     K = max length of a string (due to sorting)

    Space Complexity: O(N*K)
*/