package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * You are given a string representing an attendance record for a student.
 * The record only contains the following three characters:
 * <p>
 * 'A' : Absent. 'L' : Late. 'P' : Present.
 * <p>
 * A student could be rewarded if his attendance record
 * doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
 * <p>
 * You need to return whether the student could be rewarded according to his attendance record.
 *
 * @Author: Aaron Yang
 * @Date: 11/3/2018 10:41 AM
 */
public class StudentAttendanceRecordI {

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
            String s = stringToString(line);

            boolean ret = new Solution101().checkRecord(s);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }

}

class Solution101 {

    public boolean checkRecord(String s) {
        int countA = 0;
        for (char character : s.toCharArray()) {
            if (character == 'A') countA++;
            if (countA >= 2) return false;
        }
        if (s.matches(".*LLL.*")) return false;
        return true;
    }
}