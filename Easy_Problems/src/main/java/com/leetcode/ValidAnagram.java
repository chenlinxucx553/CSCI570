package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 * Given two strings s and t , write a function to determine if t is an anagram of s.
 *
 * @Author: Aaron Yang
 * @Date: 10/5/2018 5:43 PM
 */
public class ValidAnagram {

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

            boolean ret = new Solution50().isAnagram(s, t);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution50 {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<Character, Integer> s_map = str2Map(s);
        Map<Character, Integer> t_map = str2Map(t);
        return s_map.equals(t_map);
    }

    Map<Character, Integer> str2Map(String str) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : str.toCharArray()) {
            if (map.containsKey(c)) {
                Integer oldCount = map.get(c);
                map.replace(c, ++oldCount);
            } else {
                map.put(c, 1);
            }
        }
        return map;
    }

//    public boolean isAnagram(String s, String t) {
//        if (s.length() != t.length()) {
//            return false;
//        }
//        int[] counter = new int[26];
//        for (int i = 0; i < s.length(); i++) {
//            counter[s.charAt(i) - 'a']++;
//            counter[t.charAt(i) - 'a']--;
//        }
//        for (int count : counter) {
//            if (count != 0) {
//                return false;
//            }
//        }
//        return true;
//    }
}