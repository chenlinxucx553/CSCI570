package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * We are playing the Guess Game. The game is as follows:
 * I pick a number from 1 to n. You have to guess which number I picked.
 * Every time you guess wrong, I'll tell you whether the number is higher or lower.
 * You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
 * <p>
 * -1 : My number is lower
 * 1 : My number is higher
 * 0 : Congrats! You got it!
 *
 * @Author: Aaron Yang
 * @Date: 10/12/2018 11:00 AM
 */
public class GuessNumberHigherOrLower {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);
            line = in.readLine();
            int pick = Integer.parseInt(line);

            int ret = new Solution65().guessNumber(n, pick);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution65 extends GuessGame {

    public int guessNumber(int n, int pick) {
        super.pick = pick;
        return guessNumber(n);
    }

    public int guessNumber(int n) {
        int start = 1;
        int end = n;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            int guessResult = guess(mid);
            if (guessResult == -1) end = mid - 1;
            if (guessResult == 1) start = mid + 1;
            if (guessResult == 0) return mid;
        }
        return -1;
    }
}
