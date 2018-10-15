package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
 *
 * @Author: Aaron Yang
 * @Date: 10/15/2018 10:50 AM
 */
public class ThirdMaximumNumber {

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

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] nums = stringToIntegerArray(line);

            int ret = new Solution75().thirdMax(nums);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution75 {
    public int thirdMax(int[] nums) {
        Arrays.sort(nums);
        if (nums.length < 3) return nums[nums.length - 1];
        int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE, third = Integer.MIN_VALUE;
        for (int i = nums.length - 1; i >= 0; i--) {
            first = Math.max(nums[i], first);
            if (nums[i] < first) second = Math.max(nums[i], second);
            if (nums[i] < second) return nums[i];
        }
        return third == Integer.MIN_VALUE ? first : third;
    }
}