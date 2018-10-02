package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Given an array of integers and an integer k,
 * find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
 * and the absolute difference between i and j is at most k.
 *
 * @Author: Aaron Yang
 * @Date: 10/2/2018 11:08 AM
 */
public class ContainsDuplicateII {

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

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] nums = stringToIntegerArray(line);
            line = in.readLine();
            int k = Integer.parseInt(line);

            boolean ret = new Solution46().containsNearbyDuplicate(nums, k);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution46 {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, ArrayList> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                map.get(nums[i]).add(i);
            }else {
                ArrayList tempList = new ArrayList();
                tempList.add(i);
                map.putIfAbsent(nums[i],tempList);
            }
        }

        for(ArrayList list : map.values()){
            if(list.size() >= 2){
                if(getMinDiff(list) <= k) return true;
            }
        }
        return false;
    }

    private int getMinDiff(ArrayList<Integer> list) {
        int min = Integer.MAX_VALUE;
        for (int i = list.size() - 1; i > 0; i--) {
            min = Math.min(min, list.get(i) - list.get(i - 1));
        }
        return min;
    }
}
