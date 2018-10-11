package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

/**
 * Given two arrays, write a function to compute their intersection.
 *
 * @Author: Aaron Yang
 * @Date: 10/11/2018 9:15 AM
 */
public class IntersectionOfTwoArrays {

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

            int[] ret = new Solution61().intersection(nums1, nums2);

            String out = integerArrayToString(ret);

            System.out.print(out);
        }
    }
}

class Solution61 {

    //https://blog.csdn.net/mengyinjun217/article/details/77645612
    //Set List 直接转String[]数组

    public int[] intersection(int[] nums1, int[] nums2) {
        Set set1 = array2set(nums1);
        Set set2 = array2set(nums2);
        Set resultSet = new HashSet<Integer>();
        resultSet.addAll(set1);
        resultSet.retainAll(set2);
        return set2array(resultSet);
    }

    private Set array2set(int[] nums) {
        Set set = new HashSet<Integer>();
        for (int num : nums) {
            set.add(num);
        }
        return set;
    }

    public int[] set2array(Set<Integer> set) {
        int[] array = new int[set.size()];
        Iterator iterator = set.iterator();
        int index = 0;
        for (Integer num : set) {
            array[index++] = num;
        }
        return array;
    }
}
