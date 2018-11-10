package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an m * n matrix M initialized with all 0's and several update operations.
 * <p>
 * Operations are represented by a 2D array,
 * and each operation is represented by an array with two positive integers a and b,
 * which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
 * <p>
 * You need to count and return the number of maximum integers in the matrix after performing all the operations.
 *
 * @Author: Aaron Yang
 * @Date: 11/10/2018 9:43 AM
 */
public class RangeAdditionII {


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

    public static int[][] stringToInt2dArray(String input) {
        JsonArray jsonArray = JsonArray.readFrom(input);
        if (jsonArray.size() == 0) {
            return new int[0][0];
        }

        int[][] arr = new int[jsonArray.size()][];
        for (int i = 0; i < arr.length; i++) {
            JsonArray cols = jsonArray.get(i).asArray();
            arr[i] = stringToIntegerArray(cols.toString());
        }
        return arr;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int m = Integer.parseInt(line);
            line = in.readLine();
            int n = Integer.parseInt(line);
            line = in.readLine();
            int[][] ops = stringToInt2dArray(line);

            int ret = new Solution110().maxCount(m, n, ops);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution110 {
    public int maxCount(int m, int n, int[][] ops) {
        if (ops.length == 0) {
            return m * n;
        }
        int row = Integer.MAX_VALUE, col = Integer.MAX_VALUE;
        for (int i = 0; i < ops.length; i++) {
            if (ops[i][0] < row) {
                row = ops[i][0];
            }
            if (ops[i][1] < col) {
                col = ops[i][1];
            }
        }
        return row * col;
    }
}