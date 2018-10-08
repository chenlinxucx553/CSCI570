package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 * Given a pattern and a string str, find if str follows the same pattern.
 * <p>
 * Here follow means a full match, such that there is a bijection between a letter in pattern
 * and a non-empty word in str.
 * <p>
 * Example 1:
 * <p>
 * Input: pattern = "abba", str = "dog cat cat dog"
 * Output: true
 * Example 2:
 * <p>
 * Input:pattern = "abba", str = "dog cat cat fish"
 * Output: false
 * Example 3:
 * <p>
 * Input: pattern = "aaaa", str = "dog cat cat dog"
 * Output: false
 * Example 4:
 * <p>
 * Input: pattern = "abba", str = "dog dog dog dog"
 * Output: false
 * Notes:
 * You may assume pattern contains only lowercase letters,
 * and str contains lowercase letters separated by a single space.
 *
 * @Author: Aaron Yang
 * @Date: 10/8/2018 11:26 AM
 */
public class WordPattern {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String pattern = stringToString(line);
            line = in.readLine();
            String str = stringToString(line);

            boolean ret = new Solution56().wordPattern(pattern, str);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution56 {
    public boolean wordPattern(String pattern, String str) {
        Map<Character, String> map = new HashMap<>();
        char[] chars = pattern.toCharArray();
        String[] words = str.split("[ ]");
        if (chars.length != words.length) return false;
        for (int i = 0; i < chars.length; i++) {
            if (map.containsKey(chars[i])) {
                if (!map.get(chars[i]).equals(words[i])) return false;
            } else {
                if (map.containsValue(words[i])) return false;
                map.put(chars[i], words[i]);
            }
        }
        return true;
    }
}
