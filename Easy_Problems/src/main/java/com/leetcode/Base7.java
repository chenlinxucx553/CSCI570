package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an integer, return its base 7 string representation.
 *
 * @Author: Aaron Yang
 * @Date: 10/29/2018 11:11 AM
 */
public class Base7 {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int num = Integer.parseInt(line);

            String ret = new Solution93().convertToBase7(num);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution93 {
    public String convertToBase7(int num) {
        StringBuffer buffer = new StringBuffer();
        if (num >= 0) {
            while (num >= 7){
                buffer.append(num % 7);
                num /= 7;
            }
            return buffer.append(num).reverse().toString();
        }else {
            return "-" + convertToBase7(-num);
        }
    }
}
