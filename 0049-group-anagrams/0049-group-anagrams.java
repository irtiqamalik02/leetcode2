class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // use sorted as key and collect

        List<List<String>> res = new ArrayList<>();
        HashMap<String,List<String>> hash = new HashMap<>();

        for(String str : strs){

            char[] ch = str.toCharArray();
            Arrays.sort(ch);

            // create key from this

            String sortedStr = new String(ch);

            // add to hashmap initialisng a new list if required
            hash.putIfAbsent(sortedStr,new ArrayList<>());
            hash.get(sortedStr).add(str);
        }

        // group all anagrams gogether

        res.addAll(hash.values());
        return res;
    }
}