package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a positive integer, output its complement number.
 * The complement strategy is to flip the bits of its binary representation.
 *
 * @Author: Aaron Yang
 * @Date: 10/25/2018 11:06 AM
 */
public class NumberComplement {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int num = Integer.parseInt(line);

            int ret = new Solution86().findComplement(num);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution86 {
    public int findComplement(int num) {
        String origin = Integer.toBinaryString(num);
        int length = origin.length();
        int result = ~num;
        String complement = Integer.toBinaryString(result).substring(32 - length, 32);
        return Integer.parseUnsignedInt(complement, 2);
    }
}