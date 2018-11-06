package com.leetcode;


import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.  You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.  The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.  If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
 *
 * @Author: Aaron Yang
 * @Date: 11/6/2018 10:24 AM
 */
public class ReshapeTheMatrix {

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

    public static String int2dArrayToString(int[][] array) {
        if (array == null) {
            return "null";
        }
        if (array.length == 0) {
            return "[]";
        }

        StringBuilder sb = new StringBuilder("[");
        for (int[] item : array) {
//            sb.append(Integer.toString(item));
            sb.append(",");
        }

        sb.setCharAt(sb.length() - 1, ']');
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[][] nums = stringToInt2dArray(line);
            line = in.readLine();
            int r = Integer.parseInt(line);
            line = in.readLine();
            int c = Integer.parseInt(line);

            int[][] ret = new Solution105().matrixReshape(nums, r, c);

//            String out = int2dArrayToString(ret);

//            System.out.print(out);
        }
    }
}

class Solution105 {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        if(r * c > nums.length * nums[0].length) return nums;
        int[][] result = new int[r][c];
        int[] temp = new int[r * c];
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums[0].length; j++) {
                temp[index++] = nums[i][j];
            }
        }
        index = 0;
        for (int i = 0, j = 0; i < r && index < temp.length;) {
            while (j < c){
                result[i][j++] = temp[index++];
            }
            i++;
            j = 0;
        }
        return result;
    }
}