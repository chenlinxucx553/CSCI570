package com.leetcode;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

/**
 * Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 * <p>
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 *
 * @Author: Aaron Yang
 * @Date: 9/22/2018 10:23 AM
 */
public class SingleNumber {

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

            int ret = new Solution32().singleNumber2(nums);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution32 {
    //Set
    public int singleNumber(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int i : nums) {
            if (!s.add(i)) s.remove(i);
        }
        return (int) s.toArray()[0];
    }

    //^= 异或运算
    public int singleNumber2(int[] nums) {
        int result = 0;
        for (int i : nums){
            result ^= i;
        }
        return result;
    }
}