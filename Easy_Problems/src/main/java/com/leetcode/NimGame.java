package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * You are playing the following Nim Game with your friend:
 * There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
 * The one who removes the last stone will be the winner.
 * You will take the first turn to remove the stones.
 * Both of you are very clever and have optimal strategies for the game.
 * Write a function to determine whether you can win the game given the number of stones in the heap.
 *
 * @Author: Aaron Yang
 * @Date: 10/9/2018 9:17 AM
 */
public class NimGame {
    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            boolean ret = new Solution57().canWinNim(n);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution57 {
    public boolean canWinNim(int n) {
        if (n < 1) {
            return false;
        } else if (n <= 3) {
            return true;
        } else {
            return !canWinNim(n - 1) || !canWinNim(n - 2) || !canWinNim(n - 3);
        }
    }

    //I hope I can solve this problem with DFS
}
