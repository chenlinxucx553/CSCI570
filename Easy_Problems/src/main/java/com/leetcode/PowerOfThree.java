package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an integer, write a function to determine if it is a power of three.
 *
 * @Author: Aaron Yang
 * @Date: 10/10/2018 9:25 AM
 */
public class PowerOfThree {

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            boolean ret = new Solution58().isPowerOfThree(n);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution58 {
    public boolean isPowerOfThree(int n) {
        return Integer.toString(n, 3).matches("^10*$");
//        return (((Math.log10(n) / (Math.log10(4)))) % 1) == 0;
    }
}