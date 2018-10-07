package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
 * find the one that is missing from the array.
 *
 * @Author: Aaron Yang
 * @Date: 10/7/2018 10:00 PM
 */
public class MissingNumber {

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

            int ret = new Solution54().missingNumber(nums);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution54 {
    public int missingNumber(int[] nums) {
        int sum = 0, temp = 0, i = 0;
        for (; i < nums.length; i++) {
            sum += nums[i];
            temp += i;
        }
        temp += i;
        return Math.abs(sum - temp);
    }
}
