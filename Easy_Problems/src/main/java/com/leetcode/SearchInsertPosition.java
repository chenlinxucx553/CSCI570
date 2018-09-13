package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a sorted array and a target value, return the index if the target is found.
 * If not, return the index where it would be if it were inserted in order.
 *
 * @Author: Aaron Yang
 * @Date: 9/12/2018 11:28 AM
 */
public class SearchInsertPosition {

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
            line = in.readLine();
            int target = Integer.parseInt(line);

            int ret = new Solution9().searchInsert(nums, target);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution9 {
    public int searchInsert(int[] nums, int target) {

        for (int i = 0; i < nums.length; i++) {
            //if existed
            if (nums[i] == target) {
                return i;
            }
        }

        //if not exist
        if (target < nums[0]) {
            return 0;
        }

        if (target > nums[nums.length - 1]) {
            return nums.length;
        }

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] < target && target < nums[i + 1]) {
                return i + 1;
            }
        }

        return 0;
    }
}
