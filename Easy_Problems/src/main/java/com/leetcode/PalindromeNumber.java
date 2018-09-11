package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PalindromeNumber {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int x = Integer.parseInt(line);

            boolean result = new Solution1().isPalindrome(x);

            System.out.print(result);
        }

    }
}

class Solution1 {

    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int original = x;
        int res = 0;
        while (x != 0) {
            //1.取余 获得最后一位
            //2.余数乘10 又依次向前进一位
            //因为 乘 和 除的次数相同所以放到了一起
            int temp = res * 10 + x % 10;
            x = x / 10; //不断取前几位
            res = temp;
        }

        return res == original ? true : false;
    }
}