package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an array nums, write a function to move all 0's to the end of it
 * while maintaining the relative order of the non-zero elements.
 * <p>
 * You must do this in-place without making a copy of the array.
 * Minimize the total number of operations.
 *
 * @Author: Aaron Yang
 * @Date: 10/8/2018 9:19 AM
 */
public class MoveZeroes {
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
            int[] nums = stringToIntegerArray(line);

            new Solution55().moveZeroes(nums);
            String out = integerArrayToString(nums);

            System.out.print(out);
        }
    }
}

class Solution55 {
    public void moveZeroes(int[] nums) {
        int index = 0;
        if (null != nums) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] != 0) {
                    nums[index++] = nums[i];
                }
            }
        }

        for (; index < nums.length; index++) {
            nums[index] = 0;
        }
    }

    public void moveZeroes2(int[] nums) {
        int numberOdZero = 0;
        int[] temp = new int[nums.length];
        int index = 0;
        if (null != nums) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] == 0) {
                    numberOdZero++;
                } else {
                    temp[index++] = nums[i];
                }
            }
        }

        while (numberOdZero-- > 0) {
            temp[index++] = 0;
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = temp[i];
        }
    }
}
