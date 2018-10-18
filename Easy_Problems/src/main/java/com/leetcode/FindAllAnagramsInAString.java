package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
 *
 * @Author: Aaron Yang
 * @Date: 10/18/2018 11:42 AM
 */
public class FindAllAnagramsInAString {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static String integerArrayListToString(List<Integer> nums, int length) {
        if (length == 0) {
            return "[]";
        }

        String result = "";
        for (int index = 0; index < length; index++) {
            Integer number = nums.get(index);
            result += Integer.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static String integerArrayListToString(List<Integer> nums) {
        return integerArrayListToString(nums, nums.size());
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);
            line = in.readLine();
            String p = stringToString(line);

            List<Integer> ret = new Solution78().findAnagrams(s, p);

            String out = integerArrayListToString(ret);

            System.out.print(out);
        }
    }
}

class Solution78 {
//Time Limited
//    private Map<Character, Integer> map = new HashMap<>();
//
//    public List<Integer> findAnagrams(String s, String p) {
//        initP(p);
//        List<Integer> result = new ArrayList<>();
//        if (null != s || !"".equals(s)) {
//            for (int i = 0; i <= s.length() - p.length(); i++) {
//                HashMap<Character, Integer> mapCopy = new HashMap<>(map);
//                String substring = s.substring(i, i + p.length());
//                if (substring.equals(p)) {
//                    result.add(i);
//                } else {
//                    for (char character : substring.toCharArray()) {
//                        if (!mapCopy.containsKey(character)) break;
//                        mapCopy.replace(character, mapCopy.get(character) - 1);
//                    }
//                    if (allZero(mapCopy)) result.add(i);
//                }
//            }
//        }
//        return result;
//    }
//
//    private boolean allZero(Map<Character, Integer> map) {
//        for (Integer num : map.values()) {
//            if (num != 0) return false;
//        }
//        return true;
//    }
//
//    void initP(String p) {
//        map.clear();
//        for (char character : p.toCharArray()) {
//            if (map.containsKey(character)) map.replace(character, map.get(character) + 1);
//            map.putIfAbsent(character, 1);
//        }
//    }

    public List<Integer> findAnagrams(String s, String p) {
        if (null == s || s.length() < p.length()) return new ArrayList<>();
        int[] map = new int[26];
        for (int i = 0; i < p.length(); i++) {
            map[p.charAt(i) - 'a']++;
            map[s.charAt(i) - 'a']--;
        }
        List<Integer> array = new ArrayList<>();
        if (isAllZero(map)) array.add(0);
        for (int i = p.length(); i < s.length(); i++) {
            map[s.charAt(i) - 'a']--;
            map[s.charAt(i - p.length()) - 'a']++;
            if (isAllZero(map)) array.add(i - p.length() + 1);
        }

        return array;
    }

    private boolean isAllZero(int[] array) {
        for (int num : array) {
            if (num != 0) return false;
        }
        return true;
    }
}
