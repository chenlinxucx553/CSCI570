package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
 *
 * @Author: Aaron Yang
 * @Date: 10/6/2018 11:08 AM
 */
public class AddDigits {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int num = Integer.parseInt(line);

            int ret = new Solution52().addDigits(num);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution52 {
    //Could you do it without any loop/recursion in O(1) runtime?
    public int addDigits(int num) {
        while (num > 9) {
            int sum = 0;
            char[] chars = Integer.toString(num).toCharArray();
            for (char c : chars) {
                sum += c - '0';
            }
            num = sum;
        }
        return num;
    }

//    public int addDigits(int num){
//        if (num == 0){
//            return 0;
//        }
//        if (num % 9 == 0){
//            return 9;
//        }
//        else {
//            return num % 9;
//        }
//    }
}
