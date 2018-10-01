package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Count the number of prime numbers less than a non-negative number, n.
 *
 * @Author: Aaron Yang
 * @Date: 10/1/2018 9:50 AM
 */
public class CountPrimes {


    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            int ret = new Solution42().countPrimes2(n);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution42 {
    //Time Limit Exceeded
    public int countPrimes(int n) {
        int count = 0;
        int original = n;
        while (n > 1) {
            if (isPrime(n) && n != original) ++count;
            --n;
        }
        return count;
    }

    private boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    // Sieve of Eratosthenes
    public int countPrimes2(int n) {
        Boolean[] result = new Boolean[n];
        int count = 0;
        if (n > 1) {
            result[0] = result[1] = false;
            //init
            for (int i = 2; i < n; i++) {
                result[i] = true;
            }
            for (int i = 2; i < n; i++) {
                if (result[i]) {
                    for (int j = 2; j * i < n; j++) {
                        result[i * j] = false;
                    }
                }
            }
            for (int i = 2; i < n; i++) {
                if (result[i]) ++count;
            }
        }
        return count;
    }

}
