package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an integer, write an algorithm to convert it to hexadecimal.
 * For negative integer, two’s complement (补码)method is used.
 * <p>
 * https://en.wikipedia.org/wiki/Two%27s_complement
 *
 * @Author: Aaron Yang
 * @Date: 10/15/2018 9:26 AM
 */
public class ConvertANumber2Hexadecimal {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int num = Integer.parseInt(line);

            String ret = new Solution72().toHex(num);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution72 {

    char[] HexChars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};

    public String toHex(int num) {
        if (0 == num) return "0";
        StringBuffer buffer = new StringBuffer();
        for (int i = 0; i < 8 && num != 0; i++) {
            buffer.append(HexChars[num & 0xF]);
            num >>>= 4;
        }
        return buffer.reverse().toString();
    }

}