package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
 *
 * @Author: Aaron Yang
 * @Date: 10/12/2018 10:07 AM
 */
public class SumOfTwoIntegers {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int a = Integer.parseInt(line);
            line = in.readLine();
            int b = Integer.parseInt(line);

            int ret = new Solution64().getSum(a, b);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution64 {
    public int getSum(int a, int b) {
        //数字在计算机中都是补码形式存储 正数：原码=反码=补码  负数就麻烦了 补码=反码+1
//        System.out.println("a: " + Integer.toBinaryString(a));
//        System.out.println("b: " + Integer.toBinaryString(b));
        if (0 == b) return a;
        int sum = a ^ b; //相同为0， 不同为1
//        System.out.println("a ^ b: " + Integer.toBinaryString(sum));
        int carry = (a & b) << 1;   //算数左移
//        System.out.println("a & b: " + Integer.toBinaryString(a & b));
//        System.out.println("----------------");
        return getSum(sum, carry);

    }
}
