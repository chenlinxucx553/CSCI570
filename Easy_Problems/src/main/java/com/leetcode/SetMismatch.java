package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * The set S originally contains numbers from 1 to n. But unfortunately,
 * due to the data error, one of the numbers in the set got duplicated to another number in the set,
 * which results in repetition of one number and loss of another number.
 * <p>
 * Given an array nums representing the data status of this set after the error.
 * Your task is to firstly find the number occurs twice and then find the number that is missing.
 * Return them in the form of an array.
 *
 * @Author: Aaron Yang
 * @Date: 11/20/2018 11:26 AM
 */
public class SetMismatch {
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
            int[] nums = stringToIntegerArray(line);

            int[] ret = new Solution117().findErrorNums(nums);

            String out = integerArrayToString(ret);

            System.out.print(out);
        }
    }
}

class Solution117 {
    public int[] findErrorNums(int[] nums) {
        Arrays.sort(nums);
        int[] res = new int[2];
        int missing = 1;
        //duplicated number
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] == nums[i]) {
                res[0] = nums[i];
                break;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if(missing == nums[i]){
                missing++;
            }
        }
        res[1] = missing;
        return res;
    }
}

