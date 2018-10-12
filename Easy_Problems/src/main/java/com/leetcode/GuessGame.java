package com.leetcode;

/**
 * @Author: Aaron Yang
 * @Date: 10/12/2018 11:03 AM
 */
public class GuessGame {

    public static int pick;

    public GuessGame() {
    }

    public static int guess(int num) {
        if (num > pick) return -1;
        else if (num < pick) return 1;
        else return 0;
    }
}
