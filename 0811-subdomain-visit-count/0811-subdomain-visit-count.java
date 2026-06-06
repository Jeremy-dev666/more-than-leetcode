class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> freq = new HashMap<>();
        for (String s : cpdomains) {
            String[] curPair = s.split(" ");
            int times = Integer.parseInt(curPair[0]);
            String fullDomain = curPair[1];
            String[] domains = fullDomain.split("\\.");
            for (int i = 0; i < domains.length; i++) {
                StringBuilder sb = new StringBuilder();
                int ptr = i;
                while (ptr < domains.length) {
                    if (ptr != domains.length - 1) {
                        sb.append(domains[ptr]).append(".");
                    } else {
                        sb.append(domains[ptr]);
                    }
                    ptr++;
                }
                freq.merge(sb.toString(), times, Integer::sum);
            }
        }

        List<String> ans = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : freq.entrySet()) {
            String key = entry.getKey();
            int value = entry.getValue();
            StringBuilder sb = new StringBuilder();
            sb.append(value).append(" ").append(key);
            ans.add(sb.toString());
        }
        return ans;
    }
}