package com.leetcode;

import java.math.BigInteger;

/**
 * Reverse bits of a given 32 bits unsigned integer.
 *
 * @Author: Aaron Yang
 * @Date: 9/27/2018 9:33 AM
 */
public class ReverseBits {


    public int reverseBits(int n) {
        String binaryString = Integer.toBinaryString(n);
        while (binaryString.length() < 32) binaryString = '0' + binaryString;
//        System.out.println(binaryString);
        String reverseString = new StringBuffer(binaryString).reverse().toString();
//        System.out.println(reverseString);
        return Integer.parseUnsignedInt(reverseString, 2);
    }

    public static void main(String[] args) {
        ReverseBits reverseBits = new ReverseBits();
        System.out.println(reverseBits.reverseBits(1));
    }
}
