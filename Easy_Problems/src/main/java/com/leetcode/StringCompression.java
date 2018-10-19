package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * Given an array of characters, compress it in-place.
 * The length after compression must always be smaller than or equal to the original array.
 * Every element of the array should be a character (not int) of length 1.
 * After you are done modifying the input array in-place, return the new length of the array.
 *
 * @Author: Aaron Yang
 * @Date: 10/19/2018 9:57 AM
 */
public class StringCompression {

    public int compress(char[] chars) {
        int sum = 0;
        int index = 0;
        while (index < chars.length) {
            int count = 0;
            char currentChar = chars[index];
            while ((index < chars.length && currentChar == chars[index])) {
                index++;
                count++;
            }

            chars[sum++] = currentChar;
            if (count > 1) {
                for (char c : Integer.toString(count).toCharArray()) {
                    chars[sum++] = c;
                }
            }
        }

        return sum;
    }
}
