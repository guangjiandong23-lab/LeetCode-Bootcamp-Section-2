class Solution {

    //8. String to Integer (atoi)
    public int myAtoi(String s) {

        if (s == null || s.length() == 0) {
            return 0;
        }

        int n = s.length();
        int i = 0;

        while (i < n && s.charAt(i) == ' ') {
            i++;
        }


        if (i == n) {
            return 0;
        }


        int sign = 1;
        if (s.charAt(i) == '+' || s.charAt(i) == '-') {
            sign = s.charAt(i) == '-' ? -1 : 1;
            i++;
        }


        int result = 0;
        int maxDiv10 = Integer.MAX_VALUE / 10;
        int maxRemainder = Integer.MAX_VALUE % 10;

        while (i < n) {
            char c = s.charAt(i);

            if (c < '0' || c > '9') {
                break;
            }

            int digit = c - '0';

            if (result > maxDiv10 || (result == maxDiv10 && digit > maxRemainder)) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            result = result * 10 + digit;
            i++;
        }

        return result * sign;
    }

    //438. Find All Anagrams in a String
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();

        if (s == null || p == null || s.length() < p.length()) {
            return result;
        }

        int sLen = s.length();
        int pLen = p.length();
        int[] count = new int[26];

        for (int i = 0; i < pLen; i++) {
            count[p.charAt(i) - 'a']--;
            count[s.charAt(i) - 'a']++;
        }

        // 检查第一个窗口
        boolean isAnagram = true;
        for (int num : count) {
            if (num != 0) {
                isAnagram = false;
                break;
            }
        }
        if (isAnagram) {
            result.add(0);
        }

        for (int i = pLen; i < sLen; i++) {

            count[s.charAt(i - pLen) - 'a']--;

            count[s.charAt(i) - 'a']++;

            isAnagram = true;
            for (int num : count) {
                if (num != 0) {
                    isAnagram = false;
                    break;
                }
            }
            if (isAnagram) {
                result.add(i - pLen + 1);
            }
        }

        return result;
    }

    //151. Reverse Words in a String
    public String reverseWords(String s) {
        // 去除首尾空格
        int left = 0, right = s.length() - 1;
        while (left <= right && s.charAt(left) == ' ') left++;
        while (left <= right && s.charAt(right) == ' ') right--;

        // 用StringBuilder收集单词（逆序收集）
        StringBuilder sb = new StringBuilder();
        int wordEnd = right;

        // 从后往前遍历，遇到空格时截取单词
        for (int i = right; i >= left; i--) {
            if (s.charAt(i) == ' ') {
                // 跳过连续空格
                if (i == wordEnd) {
                    wordEnd--;
                    continue;
                }
                // 截取单词并添加
                sb.append(s.substring(i + 1, wordEnd + 1)).append(' ');
                wordEnd = i - 1;
            }
        }
        // 添加第一个单词（最前面的单词）
        sb.append(s.substring(left, wordEnd + 1));

        return sb.toString();
    }
}