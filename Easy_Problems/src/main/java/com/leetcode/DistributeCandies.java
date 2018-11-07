package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.
 *
 * @Author: Aaron Yang
 * @Date: 11/7/2018 9:53 AM
 */
public class DistributeCandies {


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
            int[] candies = stringToIntegerArray(line);

            int ret = new Solution107().distributeCandies(candies);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution107 {
    public int distributeCandies(int[] candies) {
        int unique = getUniqueItemSize(candies);
        if (unique >= candies.length / 2) return candies.length / 2;
        else return unique;
    }

    private int getUniqueItemSize(int[] candies) {
        Set set = new HashSet();
        for (int num : candies) {
            set.add(num);
        }
        return set.size();
    }
}