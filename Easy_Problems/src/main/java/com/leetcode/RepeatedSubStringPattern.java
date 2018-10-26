package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
 * You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
 *
 * @Author: Aaron Yang
 * @Date: 10/20/2018 12:06 PM
 */
public class RepeatedSubStringPattern {

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

            boolean ret = new Solution82().repeatedSubstringPattern(s);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution82 {
    public boolean repeatedSubstringPattern(String s) {
        int length = s.length();
        if (length < 2) return false;
        for (int i = length / 2; i >= 1; i--) {
            if (length % i == 0) {
                int times = length / i;
                String substring = s.substring(0, i);
                StringBuffer buffer = new StringBuffer();
                for (int l = 0; l < times; l++) {
                    buffer.append(substring);
                }
                if (buffer.toString().equals(s)) return true;
            }
        }
        return false;
    }
}