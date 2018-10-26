package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * You are given a license key represented as a string S which consists only alphanumeric character and dashes.
 * The string is separated into N+1 groups by N dashes.
 * <p>
 * Given a number K, we would want to reformat the strings such that each group contains exactly K characters,
 * except for the first group which could be shorter than K, but still must contain at least one character.
 * Furthermore, there must be a dash inserted between two groups and all lowercase letters
 * should be converted to uppercase.
 * <p>
 * Given a non-empty string S and a number K, format the string according to the rules described above.
 *
 * @Author: Aaron Yang
 * @Date: 10/26/2018 10:46 AM
 */
public class LicenseKeyFormatting {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String S = stringToString(line);
            line = in.readLine();
            int K = Integer.parseInt(line);

            String ret = new Solution88().licenseKeyFormatting(S, K);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution88 {
    public String licenseKeyFormatting(String S, int K) {
        Stack<Character> stack = new Stack<>();
        array2Stack(S.toCharArray(), stack);
        StringBuffer buffer = new StringBuffer();
        while (!stack.isEmpty()) {
            for (int i = 0; i < K; i++) {
                if (!stack.isEmpty()){
                    buffer.append(Character.toUpperCase(stack.pop()));
                }
            }
            if (!stack.isEmpty()) buffer.append("-");
        }
        return buffer.reverse().toString();
    }

    private void array2Stack(char[] chars, Stack<Character> stack) {
        for (char character : chars) {
            if ('-' != character) stack.push(character);
        }
    }
}