package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
 *
 * @Author: Aaron Yang
 * @Date: 9/15/2018 11:34 AM
 */
public class SqrtX {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int x = Integer.parseInt(line);

            int ret = new Solution14().mySqrt(x);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution14 {
    public int mySqrt(int x) {
        if (x == 0) return 0;
        double root = x / 2;
        double accuracy = 1;
        double temp = 0;
        double diff = root;
        while (diff >= accuracy) {
            temp = (root + x / root) / 2;
            diff = Math.abs(root - temp);
            root = temp;
        }
        return root <= 1 ? 1 : (int)root;
    }
}
