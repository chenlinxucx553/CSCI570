package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.  The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.  Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
 *
 * @Author: Aaron Yang
 * @Date: 11/21/2018 11:58 AM
 */
public class RobotReturnToOrigin {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String moves = stringToString(line);

            boolean ret = new Solution119().judgeCircle(moves);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution119 {

    public boolean judgeCircle(String moves) {
        Point point = new Point();
        for (char c : moves.toCharArray()) {
            if (c == 'R') point.setX(point.getX() - 1);
            if (c == 'L') point.setX(point.getX() + 1);
            if (c == 'U') point.setY(point.getY() + 1);
            if (c == 'D') point.setY(point.getY() - 1);
        }
        return point.isZero();
    }
}

class Point {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Point() {
        this.x = 0;
        this.y = 0;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public boolean isZero() {
        return this.x == 0 && this.y == 0;
    }
}
