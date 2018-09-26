package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;

/**
 * Given an array of size n, find the majority element.
 * The majority element is the element that appears more than ⌊ n/2 ⌋ times.
 *
 * @Author: Aaron Yang
 * @Date: 9/25/2018 9:45 AM
 */
public class MajorityElement {

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

            int ret = new Solution35().majorityElement(nums);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution35 {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> result = new HashMap<>();
        for (int number : nums) {
            if (result.containsKey(number)) {
                result.replace(number, result.get(number) + 1);
            } else {
                result.putIfAbsent(number, 1);
            }
        }
        Integer maxCount = 0;
        Integer maxIndex = 0;
        Iterator<Map.Entry<Integer, Integer>> it = result.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<Integer, Integer> entry = it.next();
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                maxIndex = entry.getKey();
            }
        }
        return maxIndex;
    }

//    public int majorityElement(int[] nums) {
//        Arrays.sort(nums);
//        return nums[nums.length/2];
//    }
}