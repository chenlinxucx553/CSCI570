package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
 *
 * @Author: Aaron Yang
 * @Date: 9/20/2018 10:19 AM
 */
public class TriangleOfPascal {

    public static String integerArrayListToString(List<Integer> nums, int length) {
        if (length == 0) {
            return "[]";
        }
        String result = "";
        for (int index = 0; index < length; index++) {
            Integer number = nums.get(index);
            result += Integer.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static String integerArrayListToString(List<Integer> nums) {
        return integerArrayListToString(nums, nums.size());
    }

    public static String int2dListToString(List<List<Integer>> nums) {
        StringBuilder sb = new StringBuilder("[");
        for (List<Integer> list : nums) {
            sb.append(integerArrayListToString(list));
            sb.append(",");
        }
        sb.setCharAt(sb.length() - 1, ']');
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int numRows = Integer.parseInt(line);

            List<List<Integer>> ret = new Solution27().generate(numRows);

            String out = int2dListToString(ret);

            System.out.print(out);
        }
    }
}

class Solution27 {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            LinkedList<Integer> rowList = new LinkedList<>();
            rowList.addFirst(1);
            for (int j = 1; j < i; j++) {
                List<Integer> prevList = result.get(i - 1);
                rowList.add(prevList.get(j - 1) + prevList.get(j));
            }
            if (i > 0) rowList.addLast(1);
            result.add(rowList);
        }
        return result;
    }
}
