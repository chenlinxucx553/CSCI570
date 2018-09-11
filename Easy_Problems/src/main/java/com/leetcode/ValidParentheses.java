package com.leetcode;

import com.eclipsesource.json.Json;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class ValidParentheses {
    public static String stringToString(String input) {
        if (input == null) {
            return "null";
        }
        return Json.value(input).toString();
    }

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);

            boolean ret = new Solution4().isValid(s);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution4 {
    public boolean isValid(String s) {
        if (s.length() == 0) {
            return true;
        }

        Stack<Character> characters = new Stack<>();
        for (Character tag : s.trim().toCharArray()) {
            if (tag == '(' || tag == '[' || tag == '{') {
                // if start brackets push into the stack
                characters.push(tag);
            } else {
                if (characters.isEmpty()) {
                    return false;
                }
                //if end brackets compare it with the latest pop
                Character ch = characters.pop();
                if (!(tag == ')' && ch == '(' || tag == '}' && ch == '{' || tag == ']' && ch == '['))
                    return false;
            }

        }
        return characters.isEmpty();
    }
}
