package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
 *
 * @Author: Aaron Yang
 * @Date: 11/2/2018 10:14 AM
 */
public class ReverseStringII {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);
            line = in.readLine();
            int k = Integer.parseInt(line);

            String ret = new Solution99().reverseStr(s, k);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution99 {

    public String reverseStr(String s, int k) {
        char[] chars = s.toCharArray();
        int index = 0;
        int length = s.length();
        for (; index < length; index += 2 * k) {
            if (index + k - 1 >= length || index + (2 * k) - 1 >= length)
                break;
            reverse(chars, index, index + k - 1);
        }

        if (index + k - 1 < length) {
            reverse(chars, index, index + k - 1);
        }

        if (index < length && index + k - 1 >= length) {
            reverse(chars, index, length - 1);
        }
        return new String(chars);
    }

    private void reverse(char[] chars, int start, int end) {
        while (start < end) {
            char temp = chars[start];
            chars[start] = chars[end];
            chars[end] = temp;
            start++;
            end--;
        }
    }
}