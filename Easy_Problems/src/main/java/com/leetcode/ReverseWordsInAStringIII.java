package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


/**
 * Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
 *
 * @Author: Aaron Yang
 * @Date: 11/5/2018 9:44 AM
 */
public class ReverseWordsInAStringIII {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);

            String ret = new Solution102().reverseWords(s);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution102 {
    public String reverseWords(String s) {
        String[] words = s.split("[ ]");
        StringBuffer buffer = new StringBuffer();
        for (String word : words) {
            buffer.append(reverse(word) + " ");
        }
        return buffer.toString().trim();
    }

    private String reverse(String word) {
        char[] chars = new char[word.length()];
        int length = word.length() - 1;
        for (char character : word.toCharArray()) {
            chars[length--] = character;
        }
        return new String(chars);
    }
}