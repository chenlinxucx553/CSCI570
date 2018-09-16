package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
 *
 * @Author: Aaron Yang
 * @Date: 9/16/2018 9:32 AM
 */
public class MergeSortedArray {

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
            int m = Integer.parseInt(line);
            line = in.readLine();
            int[] nums2 = stringToIntegerArray(line);
            line = in.readLine();
            int n = Integer.parseInt(line);

            new Solution17().merge(nums1, m, nums2, n);
            String out = integerArrayToString(nums1);

            System.out.print(out);
        }
    }
}

class Solution17 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int i = m - 1, j = n - 1;
        int index = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (nums1[i] >= nums2[j]) {
                nums1[index--] = nums1[i--];
            } else {
                nums1[index--] = nums2[j--];
            }
        }
        while (i >= 0) {
            nums1[index--] = nums1[i--];
        }
        while (j >= 0) {
            nums1[index--] = nums2[j--];
        }
    }
}