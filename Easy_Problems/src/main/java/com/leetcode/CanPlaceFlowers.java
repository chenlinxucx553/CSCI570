package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Suppose you have a long flowerbed in which some of the plots are planted and some are not.
 * However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
 * <p>
 * Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty),
 * and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
 *
 * @Author: Aaron Yang
 * @Date: 11/16/2018 10:03 AM
 */
public class CanPlaceFlowers {

    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
            return new int[0];
        }

        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for (int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] flowerbed = stringToIntegerArray(line);
            line = in.readLine();
            int n = Integer.parseInt(line);

            boolean ret = new Solution111().canPlaceFlowers(flowerbed, n);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }

}

class Solution111 {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int index = 0;
        while (index < flowerbed.length) {
            if ((flowerbed[index] == 0)
                    && (index == 0 || flowerbed[index - 1] == 0)
                    && (index == flowerbed.length - 1 || flowerbed[index + 1] == 0)) {
                flowerbed[index] = 1;
                n--;
            }
            index++;
        }
        return n <= 0;
    }
}
