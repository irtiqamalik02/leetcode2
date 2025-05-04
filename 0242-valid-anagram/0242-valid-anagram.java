import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        HashMap<Character, Integer> charCountMap = new HashMap<>();

        // Increment counts for characters in s and decrement for characters in t
        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);
            charCountMap.put(c1, charCountMap.getOrDefault(c1, 0) + 1);
            charCountMap.put(c2, charCountMap.getOrDefault(c2, 0) - 1);
        }

        // Check if all counts are zero
        for (int val : charCountMap.values()) { // #####
            if (val != 0)
                return false;
        }

        return true;
    }
}

/**
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 **/