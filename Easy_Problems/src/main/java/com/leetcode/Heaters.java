package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * Winter is coming! Your first job during the contest is to design a standard heater
 * with fixed warm radius to warm all the houses.
 *
 * @Author: Aaron Yang
 * @Date: 10/21/2018 10:49 AM
 */
public class Heaters {

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

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] houses = stringToIntegerArray(line);
            line = in.readLine();
            int[] heaters = stringToIntegerArray(line);

            int ret = new Solution85().findRadius(houses, heaters);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution85 {
    public int findRadius(int[] houses, int[] heaters) {
        int radix = 0;
        Arrays.sort(houses);
        Arrays.sort(heaters);
        int i = 0;
        for (int house : houses) {
            while (i < heaters.length - 1 && Math.abs(heaters[i + 1] - house) <= Math.abs(heaters[i] - house)) {
                ++i;
            }
            radix = Math.max(radix, Math.abs(heaters[i] - house));
        }
        return radix;
    }
}