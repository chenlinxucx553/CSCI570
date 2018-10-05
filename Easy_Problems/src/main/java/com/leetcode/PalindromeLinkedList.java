package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * Given a singly linked list, determine if it is a palindrome.
 *
 * @Author: Aaron Yang
 * @Date: 10/5/2018 10:07 AM
 */
public class PalindromeLinkedList {
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

    public static ListNode stringToListNode(String input) {
        // Generate array from the input
        int[] nodeValues = stringToIntegerArray(input);

        // Now convert that list into linked list
        ListNode dummyRoot = new ListNode(0);
        ListNode ptr = dummyRoot;
        for (int item : nodeValues) {
            ptr.next = new ListNode(item);
            ptr = ptr.next;
        }
        return dummyRoot.next;
    }

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            ListNode head = stringToListNode(line);

            boolean ret = new Solution49().isPalindrome(head);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution49 {
    public boolean isPalindrome(ListNode head) {
        Stack<ListNode> stack = new Stack();
        int len = 0;
        ListNode node = head;
        while (node != null) {
            node = node.next;
            len++;
        }
        int mid = (len + 1) / 2;
        while (mid-- > 0) {
            //the amount of listnode is even
            stack.push(head);
            head = head.next;
        }

        if (len % 2 != 0) {
            stack.pop();
        }
        while (head != null) {
            if (stack.pop().val != head.val) return false;
            head = head.next;
        }

        return head == null;
    }
}
