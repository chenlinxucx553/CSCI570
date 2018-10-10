package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Write a function that takes a string as input and returns the string reversed.
 *
 * @Author: Aaron Yang
 * @Date: 10/10/2018 10:28 AM
 */
public class ReverseString {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);

            String ret = new Solution59().reverseString(s);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution59 {
    public String reverseString(String s) {
        return new StringBuffer(s).reverse().toString();
    }
}