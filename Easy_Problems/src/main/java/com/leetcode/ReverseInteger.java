package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ReverseInteger {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int x = Integer.parseInt(line);

            int ret = new Solution().reverse(x);

            String out = String.valueOf(ret);

            System.out.print(out);
        }

    }
}

class Solution {
//
//    public int reverse(int x) {
//        int res = 0;
//        while (x != 0) {
//            int temp = res * 10 + x % 10;
//            x = x / 10; //不断取前几位
//            if (temp / 10 != res) {
//                res = 0;
//                break;
//            }
//            res = temp;
//        }
//        return res;
//    }

    public int reverse(int x) {
        long result = 0l;
        if (x < 0) {
            //negative number -141231  ==> 132141- ==> -132141
            result = -Long.parseLong(new StringBuffer(Long.valueOf(x).toString()).reverse().toString().split("[-]")[0]);
        } else {
            result = Long.parseLong(new StringBuffer(Long.valueOf(x).toString()).reverse().toString());
        }
        if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE)
            return 0;
        else
            return (int)result;
    }

//    public int reverse(int x) {
//
//        String str = Integer.toString(x);
//        String reverse = new StringBuffer(str).reverse().toString();
//
//        if (reverse.endsWith("-")) {
//            reverse = reverse.substring(0, reverse.length() -1);
//            long y = Long.parseLong(reverse);
//            if (y > Integer.MAX_VALUE || y < Integer.MIN_VALUE)
//                return 0;
//            else
//                return -(int)y;
//        }
//
//        long y = Long.parseLong(reverse);
//        if (y > Integer.MAX_VALUE || y < Integer.MIN_VALUE)
//            return 0;
//        else
//            return (int)y;
//    }
}
