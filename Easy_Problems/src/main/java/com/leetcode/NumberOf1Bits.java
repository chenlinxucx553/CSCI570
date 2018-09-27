package com.leetcode;

/**
 * Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
 *
 * @Author: Aaron Yang
 * @Date: 9/27/2018 10:27 AM
 */
public class NumberOf1Bits {

    public int hammingWeight(int n) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            count += n & 1;
            n >>>= 1;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(new NumberOf1Bits().hammingWeight(11));
    }

}
