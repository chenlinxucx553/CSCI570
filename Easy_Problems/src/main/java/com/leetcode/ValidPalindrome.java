package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
 *
 * @Author: Aaron Yang
 * @Date: 9/22/2018 9:55 AM
 */
public class ValidPalindrome {

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

            boolean ret = new Solution31().isPalindrome(s);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }

}

class Solution31 {
    public boolean isPalindrome(String s) {
        if (s.isEmpty()) return true;
        String str = s.replaceAll("[\\pP‘’“”` +]", "");
        char[] chars = str.toLowerCase().toCharArray();
        int start = 0, end = chars.length - 1;
        while (start < end) {
            if((chars[start++] != chars[end--])) return false;
        }
        return true;
    }
}
