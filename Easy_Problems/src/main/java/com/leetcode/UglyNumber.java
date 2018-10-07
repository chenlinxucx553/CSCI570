package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Write a program to check whether a given number is an ugly number.
 *
 * @Author: Aaron Yang
 * @Date: 10/7/2018 9:51 PM
 */
public class UglyNumber {
    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int num = Integer.parseInt(line);

            boolean ret = new Solution53().isUgly(num);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution53 {
    public boolean isUgly(int num) {
        if (0 == num) return false;
        while (num % 2 == 0) num /= 2;
        while (num % 3 == 0) num /= 3;
        while (num % 5 == 0) num /= 5;
        return num == 1;
    }
}