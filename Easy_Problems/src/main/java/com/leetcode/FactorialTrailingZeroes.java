package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an integer n, return the number of trailing zeroes in n!.
 *
 * @Author: Aaron Yang
 * @Date: 9/25/2018 10:51 AM
 */
public class FactorialTrailingZeroes {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            int ret = new Solution37().trailingZeroes2(n);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution37 {
    public int trailingZeroes(int n) {
        long result = factorial(n);
        int count = 0;
        while (result > 10) {
            if (result % 10 == 0) count++;
            result /= 10;
        }
        return count;
    }

    public int trailingZeroes2(int n) {
        if(n < 5) return 0;
        else return n/5 + trailingZeroes2(n/5);
    }

    long factorial(long number) {
        if (number != 0) {
            return number * factorial(number - 1);
        } else return 1;
    }
}
