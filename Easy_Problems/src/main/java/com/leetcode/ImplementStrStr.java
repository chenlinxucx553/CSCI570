package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 *
 * @Author: Aaron Yang
 * @Date: 9/12/2018 9:57 AM
 */
public class ImplementStrStr {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String haystack = stringToString(line);
            line = in.readLine();
            String needle = stringToString(line);

            int ret = new Solution8().strStr(haystack, needle);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution8 {
    public int strStr(String haystack, String needle) {
        if (null == needle || needle.isEmpty()) {
            return 0;
        }
        char[] haystack_chars = haystack.toCharArray();
        char[] needle_chars = needle.toCharArray();

        int j = 0;
        for (int i = 0; i < haystack_chars.length; ) {
            if (haystack_chars[i++] == needle_chars[j]) {
                j++;
//                System.out.printf("_1");
            } else {
                //look back
                i = i - j;
                j = 0;
//                System.out.printf("_0");
            }
            if (j == needle_chars.length) {
                return i - j;
            }
        }
        return -1;
    }
}
