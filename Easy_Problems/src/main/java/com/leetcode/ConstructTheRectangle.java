package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * For a web developer, it is very important to know how to design a web page's size.
 * So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page,
 * whose length L and width W satisfy the following requirements:
 * <p>
 * 1. The area of the rectangular web page you designed must equal to the given target area.
 * 2. The width W should not be larger than the length L, which means L >= W.
 * 3. The difference between length L and width W should be as small as possible.
 *
 * @Author: Aaron Yang
 * @Date: 10/27/2018 9:46 AM
 */
public class ConstructTheRectangle {

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
            int area = Integer.parseInt(line);

            int[] ret = new Solution90().constructRectangle(area);

            String out = integerArrayToString(ret);

            System.out.print(out);
        }
    }
}

class Solution90 {
    public int[] constructRectangle(int area) {
        int root = (int) Math.sqrt(area);
        if (root * root == area) return new int[]{root, root};
        while (root >= 1) {
            double edge = (double) area / root;
            if (isInteger(edge)) return new int[]{(int) edge, root};
            root--;
        }
        return new int[]{area, 1};
    }

    private boolean isInteger(double edge) {
        if (edge - (int) edge == 0) return true;
        return false;
    }
}