package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
 *
 * @Author: Aaron Yang
 * @Date: 11/1/2018 10:57 AM
 */
public class KPairsInArray {

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

//            for (int i = 1; i <= Integer.parseUnsignedInt(line); i++) {
//                for (int j = 1; j <= i; j++) {
//                    for (int k = 1; k <= j; k++) {
//                        System.out.println("@@ k = " + k + " @@");
//                    }
//                    System.out.print("j = " + j + "");
//                    System.out.println();
//                }
//                System.out.println("-------i = " + i + "-------");
//            }


//            int i = 1, j = 0;
//            int count = 1;
//            while (i + j <= Integer.parseUnsignedInt(line)) {
//                System.out.println("----" + count++ + "----");
//                if (i < j) {
//                    j++;
//                } else {
//                    i++;
//                }
//            }
            int[] nums = stringToIntegerArray(line);
            line = in.readLine();
            int k = Integer.parseInt(line);

            int ret = new Solution97().findPairs(nums, k);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution97 {

    private Set<Integer> set = new HashSet<>();

    public int findPairs(int[] nums, int k) {
        if (k == 0) {
            return findSame(nums);
        } else if (k > 0) {
            return findDiff(nums, k);
        } else {
            return 0;
        }
    }

    private int findDiff(int[] nums, int k) {
        Set<Integer> temp = new HashSet<>();
        for (int num : nums) {
            set.add(num);
            temp.add(num + k);
        }
        set.retainAll(temp);
        return set.size();
    }

    private int findSame(int[] nums) {
        HashSet temp = new HashSet();
        for (int num : nums) {
            if (!set.add(num)) temp.add(num);
        }
        return temp.size();
    }
}