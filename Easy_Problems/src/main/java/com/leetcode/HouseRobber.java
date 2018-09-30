package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is
 * that adjacent houses have security system connected and it will automatically contact the police
 * if two adjacent houses were broken into on the same night.
 * <p>
 * <p>
 * Given a list of non-negative integers representing the amount of money of each house,
 * determine the maximum amount of money you can rob tonight without alerting the police.
 *
 * @Author: Aaron Yang
 * @Date: 9/29/2018 11:07 AM
 */
public class HouseRobber {
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

            int ret = new Solution39().rob(nums);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution39 {
    public int rob(int[] nums) {
        if (nums.length > 0) {
            int[] result = new int[nums.length];
            result[0] = nums[0];
            if (nums.length > 1) {
                result[1] = Math.max(nums[0], nums[1]);
                for (int i = 2; i < nums.length; i++) {
                    result[i] = Math.max(result[i - 1], result[i - 2] + nums[i]);
                }
            }
            return result[nums.length - 1];
        } else {
            return 0;
        }
    }
}
