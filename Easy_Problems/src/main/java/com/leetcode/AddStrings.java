package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
 * <p>
 * The length of both num1 and num2 is < 5100.
 * Both num1 and num2 contains only digits 0-9.
 * Both num1 and num2 does not contain any leading zero.
 * You must not use any built-in BigInteger library or convert the inputs to integer directly.
 *
 * @Author: Aaron Yang
 * @Date: 10/16/2018 10:18 AM
 */
public class AddStrings {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String num1 = stringToString(line);
            line = in.readLine();
            String num2 = stringToString(line);

            String ret = new Solution76().addStrings(num1, num2);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution76 {
    public String addStrings(String num1, String num2) {
        StringBuffer buffer = new StringBuffer();
        Stack<Character> stack1 = new Stack();
        pushAll(stack1, num1.toCharArray());
        Stack<Character> stack2 = new Stack();
        pushAll(stack2, num2.toCharArray());
        int carry = 0;
        while (!stack1.empty() && !stack2.empty()) {
            int result = stack1.pop() - '0' + stack2.pop() - '0' + carry;
            if (result >= 10) {
                result -= 10;
                carry = 1;
            } else {
                carry = 0;
            }
            buffer.append((char) (result + '0'));
        }
        if (!stack1.empty()) {
            addRemain(stack1, carry, buffer);
        } else {
            addRemain(stack2, carry, buffer);
        }
        return buffer.reverse().toString();
    }

    private void addRemain(Stack<Character> stack, int carry, StringBuffer buffer) {
        while (!stack.empty()) {
            int result = stack.pop() - '0' + carry;
            if (result >= 10) {
                result -= 10;
                carry = 1;
            } else {
                carry = 0;
            }
            buffer.append((char) (result + '0'));
        }
        if (stack.isEmpty() && carry == 1) {
            buffer.append('1');
        }
    }

    private void pushAll(Stack<Character> stack, char[] chars) {
        for (char character : chars) {
            stack.push(character);
        }
    }
}
