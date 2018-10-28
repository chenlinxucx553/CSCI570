package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.  The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
 *
 * @Author: Aaron Yang
 * @Date: 10/27/2018 7:00 PM
 */
public class NextGreaterElementI {

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
            int[] nums1 = stringToIntegerArray(line);
            line = in.readLine();
            int[] nums2 = stringToIntegerArray(line);

            int[] ret = new Solution91().nextGreaterElement(nums1, nums2);

            String out = integerArrayToString(ret);

            System.out.print(out);
        }
    }
}

class Solution91 {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        for (int i = 0; i < nums1.length; i++) {
            int temp = nums1[i];
            for (int j = 0; j < nums2.length; j++) {
                if (nums1[i] == nums2[j] && j + 1 < nums2.length) {
                    if (nums1[i] < nums2[j + 1]) {
                        nums1[i] = nums2[j + 1];
                        break;
                    }
                    int max = getMax(nums2, j + 1);
                    if (nums1[i] < max) {
                        nums1[i] = max;
                        break;
                    }
                }
            }
            if (temp == nums1[i]) nums1[i] = -1;
        }
        return nums1;
    }

    private int getMax(int[] nums, int i) {
        int max = nums[i];
        for (; i < nums.length; i++) {
            max = Math.max(nums[i], max);
        }
        return max;
    }
}