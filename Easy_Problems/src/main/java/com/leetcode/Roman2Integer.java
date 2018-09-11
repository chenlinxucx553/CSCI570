package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Roman2Integer {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {

            int ret = new Solution2().romanToInt(line);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution2 {
    public int romanToInt(String s) {
        int result = 0;
        int max = 0;
        //split the string into chars
        char[] chars = s.toCharArray();
        // map the char to the int value
        int[] numbers = getArray(chars);
        // decide the add or sub
        for (int i = numbers.length - 1; i >= 0; i--) {
            if (numbers[i] >= max) {
                max = numbers[i];
                result += numbers[i];
            } else {
                //sub
                result -= numbers[i];
            }

        }
        return result;
    }

    public int[] getArray(char[] chars) {
        int[] array = new int[chars.length];
        for (int i = 0; i < chars.length; i++) {
            array[i] = getValue(chars[i]);
        }
        return array;
    }

    public int getValue(char character) {
        for (SYMBOL symbol : SYMBOL.values()) {
            if (symbol.getTag() == character) {
                return symbol.getValue();
            }
        }
        return 0;
    }
}

enum SYMBOL {
    I('I', 1),
    V('V', 5),
    X('X', 10),
    L('L', 50),
    C('C', 100),
    D('D', 500),
    M('M', 1000);

    private char tag;
    private int value;

    SYMBOL(char tag, int value) {
        this.tag = tag;
        this.value = value;
    }

    public char getTag() {
        return tag;
    }


    public int getValue() {
        return value;
    }

}
