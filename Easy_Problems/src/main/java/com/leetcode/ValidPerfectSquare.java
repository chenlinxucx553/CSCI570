package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a positive integer num, write a function which returns True if num is a perfect square else False.
 *
 * @Author: Aaron Yang
 * @Date: 10/11/2018 10:44 AM
 */
public class ValidPerfectSquare {

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int num = Integer.parseInt(line);

            boolean ret = new Solution63().isPerfectSquare(num);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution63 {
    public boolean isPerfectSquare(int num) {
        //https://jingyan.baidu.com/article/f79b7cb31082079144023ebb.html
        //牛顿迭代法
        if (1 == num) return true;
        int root = num / 2;
        while (Long.valueOf(Math.abs((long) root * root)) > num) {
            root = (root + num / root) / 2;
        }
        return root * root == num;
    }
}
