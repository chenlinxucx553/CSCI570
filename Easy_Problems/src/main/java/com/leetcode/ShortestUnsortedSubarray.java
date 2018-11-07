package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.  You need to find the shortest such subarray and output its length.
 *
 * @Author: Aaron Yang
 * @Date: 11/7/2018 10:17 AM
 */
public class ShortestUnsortedSubarray {

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

            int ret = new Solution108().findUnsortedSubarray(nums);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution108 {
    public int findUnsortedSubarray(int[] nums) {
        int start = 0, end = 0;
        boolean flag = false;
        int[] sorted = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sorted);
        for (int i = 0; i < sorted.length; i++) {
            if (nums[i] != sorted[i]) {
                if (!flag) {
                    start = i;
                    flag = true;
                } else {
                    end = i + 1;
                }
            }
        }
        return end - start;
    }
}