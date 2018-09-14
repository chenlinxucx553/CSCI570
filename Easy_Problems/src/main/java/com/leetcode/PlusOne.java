package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
 *
 * @Author: Aaron Yang
 * @Date: 9/14/2018 9:19 AM
 */
public class PlusOne {

    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
            return new int[0];
        }

        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for (int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }

    public static String integerArrayToString(int[] nums, int length) {
        if (length == 0) {
            return "[]";
        }

        String result = "";
        for (int index = 0; index < length; index++) {
            int number = nums[index];
            result += Integer.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static String integerArrayToString(int[] nums) {
        return integerArrayToString(nums, nums.length);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] digits = stringToIntegerArray(line);

            int[] ret = new Solution12().plusOne(digits);

            String out = integerArrayToString(ret);

            System.out.print(out);
        }
    }
}

class Solution12 {
    public int[] plusOne(int[] digits) {
        int[] result = null;
        if (digits[digits.length - 1] >= 0 && digits[digits.length - 1] <= 8) {
//            0 <= last <= 8 ==> [0, 8]
            digits[digits.length - 1] += 1;
            return digits;
        } else {
//            last = 9
            for (int i = digits.length - 1; i >= 0; i--) {
                if (digits[i] == 9 && i != 0) {
                    digits[i] = 0;
                } else if (digits[i] == 9 && i == 0) {
                    digits[i] = 0;
                    result = new int[digits.length + 1];
                    result[0] = 1;
                    System.arraycopy(digits, 0, result, 1, digits.length - 1);
                } else {
                    digits[i] += 1;
                    return digits;
                }
            }
        }

        return result;
    }
    //数组偿付太长，将超过long的限制--》报错
//    public int[] plusOne(int[] digits) {
//
//        long number = 0;
//        long multiple = 1;
//        for (int i = digits.length - 1; i >= 0; i--) {
//            number += digits[i] * multiple;
//            multiple *= 10;
//        }
//        number += 1;
//        int[] result;
//        if (number == multiple) {
//            result = new int[digits.length + 1];
//        } else {
//            result = new int[digits.length];
//        }
//        Stack<Long> stack = new Stack<Long>();
//        while (number != 0) {
//            long temp = number % 10;
//            number = number / 10;
//            stack.push(temp);
//        }
//        int index = 0;
//        while (!stack.isEmpty()) {
//            result[index++] = Math.toIntExact(stack.pop());
//        }
//        return result;
//    }
}
