package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Write a function that takes a string as input and reverse only the vowels of a string.
 *
 * @Author: Aaron Yang
 * @Date: 10/10/2018 10:37 AM
 */
public class ReverseVowelsOfAString {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);

            String ret = new Solution60().reverseVowels2(s);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution60 {

    private Set set = new HashSet(
            Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        List<Integer> list = new ArrayList<>();
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < chars.length; i++) {
            if (set.contains(chars[i])) {
                list.add(i);
                stack.push(chars[i]);
            }
        }
        if (!stack.empty()) {
            StringBuffer buffer = new StringBuffer(s);
            for (Integer index : list) {
                buffer.replace(index, index + 1, stack.pop().toString());
            }
            return buffer.toString();
        } else {
            return s;
        }
    }

    public String reverseVowels2(String s) {
        int start = 0;
        char[] chars = s.toCharArray();
        int end = chars.length - 1;
        while (start < end) {
            while (start < end && !set.contains(chars[start])) {
                start++;
            }
            while (start < end && !set.contains(chars[end])) {
                end--;
            }
            char temp = chars[start];
            chars[start] = chars[end];
            chars[end] = temp;
            start++;
            end--;
        }
        return new String(chars);
    }
}