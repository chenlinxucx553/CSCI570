package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a column title as appear in an Excel sheet, return its corresponding column number.
 *
 * @Author: Aaron Yang
 * @Date: 9/25/2018 10:13 AM
 */
public class ExcelSheetColumnNumber {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);

            int ret = new Solution36().titleToNumber(s);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution36 {
    public int titleToNumber(String s) {
        char[] chars = s.toCharArray();
        int result = 0;
        for (int i = 0; i < chars.length; i++) {
            int ascii = chars[i] - 64;
            for (int j = 0; j < chars.length - 1 - i; j++) {
                ascii *= 26;
            }
            result += ascii;
        }
        return result;
    }
}