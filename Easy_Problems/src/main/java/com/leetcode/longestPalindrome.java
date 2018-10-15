package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

/**
 * Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
 * <p>
 * This is case sensitive, for example "Aa" is not considered a palindrome here.
 *
 * @Author: Aaron Yang
 * @Date: 10/15/2018 10:31 AM
 */
public class longestPalindrome {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);

            int ret = new Solution73().longestPalindrome(s);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution73 {
    public int longestPalindrome(String s) {
        if (s.length() == 1) return 1;
//        if("AB".equals(s)) return 1;// why  this string cannot be the palindrome  MDZZ
        Set<Character> set = new HashSet<>();
        int sum = 0;
        char[] chars = s.toCharArray();
        if (null != s) {
            for (char character : chars) {
                if (set.contains(character)) {
                    set.remove(character);
                    sum += 2;
                } else {
                    set.add(character);
                }
            }
        }
        if (set.size() > 0 && sum > 0) sum += 1;

        return sum;
    }
}
