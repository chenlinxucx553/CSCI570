package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
 *
 * @Author: Aaron Yang
 * @Date: 11/5/2018 11:08 AM
 */
public class ArrayPartitionI {

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

            int ret = new Solution103().arrayPairSum(nums);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution103 {
    public int arrayPairSum(int[] nums) {
        int n = nums.length / 2;
        int sum = 0;
        Arrays.sort(nums);
        for (int i = 0, j = 0; j < n; i += 2) {
            sum += Math.min(nums[i], nums[i + 1]);
            j++;
        }
        return sum;
    }

}
