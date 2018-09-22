package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Say you have an array for which the ith element is the price of a given stock on day i.
 * Design an algorithm to find the maximum profit. You may complete as many transactions as you like
 * (i.e., buy one and sell one share of the stock multiple times).
 *
 * @Author: Aaron Yang
 * @Date: 9/21/2018 11:08 AM
 */
public class BestTime2BuyAndSellStockII {
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
            int[] prices = stringToIntegerArray(line);

            int ret = new Solution30().maxProfit2(prices);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution30 {
    //Brute Force 蛮力法 Time Limit Exceeded
    public int maxProfit(int[] prices) {
        return calculate(prices, 0);
    }

    private int calculate(int[] prices, int index) {
        int result = 0;
        for (int i = index; i < prices.length; i++) {
            int buy_price = prices[i];
            int tempProfit = 0;
            for (int j = i + 1; j < prices.length; j++) {
                int sell_price = prices[j];
                if (sell_price > buy_price) {
                    tempProfit = Math.max(tempProfit, calculate(prices, j + 1) + sell_price - buy_price);
                }
            }
            result = Math.max(result, tempProfit);
        }
        return result;
    }

    //Peak Valley Approach
    //https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
    public int maxProfit2(int[] prices) {
        int result = 0;
        int peak = 0, valley = 0;
        int i = 0;
        while (i < prices.length - 1) {
            while (i < prices.length - 1 && prices[i] >= prices[i + 1]) i++;
            valley = prices[i];
            while (i < prices.length - 1 && prices[i] <= prices[i + 1]) i++;
            peak = prices[i];

            result += peak - valley > 0 ? peak - valley : 0;
        }
        return result;
    }
}
