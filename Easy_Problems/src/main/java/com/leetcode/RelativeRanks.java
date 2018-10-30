package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * Given scores of N athletes,
 * find their relative ranks and the people with the top three highest scores,
 * who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
 *
 * @Author: Aaron Yang
 * @Date: 10/30/2018 11:05 AM
 */
public class RelativeRanks {


    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] nums = stringToIntegerArray(line);
            String[] relativeRanks = new Solution94().findRelativeRanks(nums);
            for (String str : relativeRanks) {
                System.out.printf(str + " ");
            }
        }

    }

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


}

class Solution94 {
    private String[] prizes = {"Gold Medal", "Silver Medal", "Bronze Medal"};

    public String[] findRelativeRanks(int[] nums) {
        int[] ranks = Arrays.copyOf(nums, nums.length);
        Arrays.sort(ranks);
        String[] level = new String[nums.length];
        int length = nums.length - 1;
        for (int i = 0; i < nums.length; i++) {
            level[i] = getIndex(ranks, nums[i]);
        }
        return level;
    }

    private String getIndex(int[] ranks, int num) {
        int start = 0;
        int end = ranks.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (ranks[mid] < num) start = mid + 1;
            if (ranks[mid] > num) end = mid;
            if (ranks[mid] == num) {
                if (mid >= ranks.length - 3) return prizes[ranks.length - mid - 1];
                else return ranks.length - mid + "";
            }
        }
        return "";
    }
}
