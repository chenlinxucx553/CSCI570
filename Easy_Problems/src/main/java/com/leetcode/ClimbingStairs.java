package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * You are climbing a stair case. It takes n steps to reach to the top.
 *
 * @Author: Aaron Yang
 * @Date: 9/15/2018 1:44 PM
 */
public class ClimbingStairs {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            int ret = new Solution15().climbStairs(n);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution15 {
    public int climbStairs(int n) {

        int step_1_max_number = n;
        int step_2_max_number = n / 2;
        int a = 0;  //step_1_number
        int b;  //step_2_number
        int result = 0;
        for (; a <= step_1_max_number; a++) {
            b = (n - a) / 2;
            if (b <= step_2_max_number && a + 2 * b == n) {
                result += count(a, b);
            }
        }
        return result;
    }

    private int count(int a, int b) {
//        int temp_result = 1;
//        if (a > 0 && b == 0 || a == 0 && b > 0) {
//            return temp_result;
//        }
//        int temp = 1;
//        for (int i = 1; i <= b; i++) {
//            temp_result *= (a + i);
//        }
//
//        return b >= 2 ? temp_result / 2 : temp_result;
        return a <= b ? factorial(a) / (factorial(b) * factorial((a - b))) : 0;
    }

    private static int factorial(int n) {
        int sum = 1;
        while (n > 0) {
            sum = sum * n--;
        }
        return sum;
    }
}
