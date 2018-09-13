package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
 *
 * @Author: Aaron Yang
 * @Date: 9/13/2018 9:26 AM
 */
public class MaximumSubarray {

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

            int ret = new Solution10().maxSubArray(nums);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution10 {
    public int maxSubArray(int[] nums) {

        int max = nums[0];
        for (int starIndex = 0; starIndex < nums.length; starIndex++) {
            int temp = 0;
            for (int i = starIndex; i < nums.length; i++) {
                temp += nums[i];
                if (max < temp) {
                    max = temp;
                }
            }
        }
        return max;
    }

    //Time Limit Exceeded
//    public int maxSubArray(int[] nums) {
//
//        int max = nums[0];
//        for (int subArrayLength = 1; subArrayLength <= nums.length; subArrayLength++) {
//            for (int i = 0; i < nums.length; i++) {
//                int temp = 0;
//                for (int j = 0; j < subArrayLength; j++) {
//                    if (i + j < nums.length) {
//                        temp += nums[i + j];
//                    }
//                }
//                if (max < temp) {
//                    max = temp;
//                }
//            }
//        }
//        return max;
//    }


}


