package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 * Given two strings s and t, determine if they are isomorphic.
 * <p>
 * Two strings are isomorphic if the characters in s can be replaced to get t.
 * <p>
 * All occurrences of a character must be replaced with another character while preserving the order of characters.
 * No two characters may map to the same character but a character may map to itself.
 * <p>
 * You may assume both s and t have the same length.
 * Example 1:
 * <p>
 * Input: s = "egg", t = "add"
 * Output: true
 * Example 2:
 * <p>
 * Input: s = "foo", t = "bar"
 * Output: false
 * Example 3:
 * <p>
 * Input: s = "paper", t = "title"
 * Output: true
 *
 * @Author: Aaron Yang
 * @Date: 10/1/2018 1:39 PM
 */
public class IsomorphicStrings {

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
            String s = stringToString(line);
            line = in.readLine();
            String t = stringToString(line);

            boolean ret = new Solution43().isIsomorphic(s, t);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution43 {
    public boolean isIsomorphic(String s, String t) {
        if (null != s && null != t) {
            Map<Character, Integer> map = new HashMap<>();
            int[] s_pattern = toArray(s.toCharArray(), map);
            map.clear();
            int[] t_pattern = toArray(t.toCharArray(), map);
            for (int i = 0; i < s_pattern.length; i++) {
                if (s_pattern[i] != t_pattern[i]) return false;
            }
            return true;
        }
        return false;
    }

    int[] toArray(char[] chars, Map map) {
        int[] array = new int[chars.length];
        int index = 0;
        for (int i = 0; i < chars.length; i++) {
            if (map.containsKey(chars[i])) {
                Integer count = (Integer) map.get(chars[i]);
                array[i] = count;
            } else {
                map.putIfAbsent(chars[i], index + 1);
                array[i] = ++index;
            }
        }
        return array;
    }
}
