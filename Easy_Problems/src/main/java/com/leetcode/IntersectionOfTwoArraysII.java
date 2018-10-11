package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Given two arrays, write a function to compute their intersection.
 * <p>
 * Example 1:
 * <p>
 * Input: nums1 = [1,2,2,1], nums2 = [2,2]
 * Output: [2,2]
 * Example 2:
 * <p>
 * Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
 * Output: [4,9]
 * Note:
 * <p>
 * Each element in the result should appear as many times as it shows in both arrays.
 * The result can be in any order.
 * Follow up:
 * <p>
 * What if the given array is already sorted? How would you optimize your algorithm?
 * What if nums1's size is small compared to nums2's size? Which algorithm is better?
 * What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
 *
 * @Author: Aaron Yang
 * @Date: 10/11/2018 9:45 AM
 */
public class IntersectionOfTwoArraysII {

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

            int[] ret = new Solution62().intersect(nums1, nums2);

            String out = integerArrayToString(ret);

            System.out.print(out);
        }
    }
}

class Solution62 {

    private List<Integer> list = new ArrayList<>();

    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map;
        if (nums1.length > nums2.length) {
            map = array2Map(nums2);
            map = updateMap(map, nums1);
        } else {
            map = array2Map(nums1);
            map = updateMap(map, nums2);
        }
        return list2array(map);
    }

    private int[] list2array(Map<Integer, Integer> map) {
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) result[i] = (int) list.get(i);
        return result;
    }

    private Map updateMap(Map<Integer, Integer> map, int[] nums) {
        if (null != map) {
            for (int num : nums) {
                if (map.containsKey(num) && map.get(num) > 0) {
                    list.add(num);
                    map.replace(num, map.get(num) - 1);
                }
            }
        }
        return map;
    }

    private Map array2Map(int[] nums) {
        HashMap<Integer, Integer> map;
        map = new HashMap();
        for (int num : nums) {
            if (map.containsKey(num)) map.replace(num, map.get(num) + 1);
            map.putIfAbsent(num, 1);
        }
        return map;
    }
}