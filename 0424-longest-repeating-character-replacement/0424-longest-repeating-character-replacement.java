class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> window = new HashMap<>();
        int maxFreq = 0;
        int res = 0;

        int start = 0;
        for (int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);
            window.merge(c, 1, Integer::sum);
            maxFreq = Math.max(maxFreq, window.get(c));

            while (end - start + 1 - maxFreq > k) {
                char d = s.charAt(start);
                window.merge(d, -1, Integer::sum);
                start++;
            }

            res = Math.max(res, end - start + 1);
        }

        return res;
    }
}