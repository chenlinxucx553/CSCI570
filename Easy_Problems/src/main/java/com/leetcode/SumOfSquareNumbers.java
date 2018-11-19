package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
 *
 * @Author: Aaron Yang
 * @Date: 11/19/2018 10:55 AM
 */
public class SumOfSquareNumbers {

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int c = Integer.parseInt(line);

            boolean ret = new Solution114().judgeSquareSum(c);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution114 {
    public boolean judgeSquareSum(int c) {
        for (long i = 0; i * i <= c; i++) {
            int j = c - (int) (i * i);
            if (binarySearch(0, j, j)) return true;
        }
        return false;
    }

    private boolean binarySearch(long start, long end, int num) {
        if (start > end) return false;
        long mid = start + (end - start) / 2;

        if (mid * mid == num) return true;
        else if (mid * mid < num) return binarySearch(mid + 1, end, num);
        else return binarySearch(start, mid - 1, num);
    }
}
