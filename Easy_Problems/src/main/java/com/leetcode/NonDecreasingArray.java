package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.  We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
 *
 * @Author: Aaron Yang
 * @Date: 11/23/2018 10:13 AM
 */
public class NonDecreasingArray {

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

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] nums = stringToIntegerArray(line);

            boolean ret = new Solution120().checkPossibility(nums);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution120 {
    public boolean checkPossibility(int[] nums) {
        int count = 0;
        int max = nums[0];
        int index = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] > nums[i]) count++;
            if (count == 2) return false;
            if (nums[i] > max) {
                max = nums[i];
                index = i;
            }
        }
        return nums.length - index < 2;
    }

    public int countBinarySubstrings(String s) {
        int count = 0;
        int consecutiveCount = 1;
        int lastConsecutiveCount = 0;

        char[] chars = s.toCharArray();
        for (int i = 1; i < s.length(); i++) {
            if (chars[i] != chars[i - 1]) {
                lastConsecutiveCount = consecutiveCount;
                consecutiveCount = 1;
                count++;
            } else {
                consecutiveCount++;
                if (consecutiveCount <= lastConsecutiveCount) count++;
            }
        }

        return count;
    }
}