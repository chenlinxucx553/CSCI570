package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
 * some elements appear twice and others appear once.
 * Find all the elements of [1, n] inclusive that do not appear in this array.
 * Could you do it without extra space and in O(n) runtime?
 * You may assume the returned list does not count as extra space.
 *
 * @Author: Aaron Yang
 * @Date: 10/19/2018 10:34 AM
 */
public class FindAllNumbersDisappearedInAArray {

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

    public static String integerArrayListToString(List<Integer> nums, int length) {
        if (length == 0) {
            return "[]";
        }

        String result = "";
        for (int index = 0; index < length; index++) {
            Integer number = nums.get(index);
            result += Integer.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static String integerArrayListToString(List<Integer> nums) {
        return integerArrayListToString(nums, nums.size());
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] nums = stringToIntegerArray(line);

            List<Integer> ret = new Solution80().findDisappearedNumbers(nums);

            String out = integerArrayListToString(ret);

            System.out.print(out);
        }
    }
}

class Solution80 {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Arrays.sort(nums);
        int size = nums.length;
        List<Integer> result = new ArrayList<>();
        if (size > 0) {
            ///front
            if (1 != nums[0]) {
                int n = nums[0] - 1;
                int temp = nums[0];
                while (n > 0) result.add(n--);
            }
            //mid
            for (int i = size - 1; i >= 1; i--) {
                int n = nums[i] - nums[i - 1];
                while (n > 1) result.add(nums[i] - --n);
            }
            //tail
            if (size != nums[size - 1]) {
                int n = size - nums[size - 1];
                if (n > 0) {
                    while (n-- > 0) result.add(Math.abs(size--));
                } else if (n < 0) {
                    n = Math.abs(n);
                    int last = nums[size - 1];
                    while (n-- > 0) result.add(--last);
                }
            }
        }
        return result;
    }
}