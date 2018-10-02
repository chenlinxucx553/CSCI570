package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * Reverse a singly linked list.
 *
 * @Author: Aaron Yang
 * @Date: 10/2/2018 9:46 AM
 */
public class ReverseLinkedList {


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

    public static String listNodeToString(ListNode node) {
        if (node == null) {
            return "[]";
        }

        String result = "";
        while (node != null) {
            result += Integer.toString(node.val) + ", ";
            node = node.next;
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            ListNode head = stringToListNode(line);

            ListNode ret = new Solution44().reverse_it(head);

            String out = listNodeToString(ret);

            System.out.print(out);
        }
    }
}

class Solution44 {
    public ListNode reverseList(ListNode head) {
        ListNode result = new ListNode(-1);
        List<Integer> data = new ArrayList<>();
        while (null != head) {
            data.add(head.val);
            head = head.next;
        }
        for (int i = data.size() - 1; i >= 0; i--) {
            ListNode node = new ListNode(data.get(i));
            addLast(result, node);
        }
        return result.next;
    }

    private void addLast(ListNode result, ListNode node) {
        while (null != result) {
            if (null == result.next) {
                result.next = node;
                break;
            }
            result = result.next;
        }
    }

    public ListNode reverse_rec(ListNode head) {
        if (head.next == null) {
            //Found the end.
            return head;
        }
        //Recurse all the way to the end of the list.
        ListNode temp = reverse_rec(head.next);
        //The last node is always head.next since it will  be at the end of the  returned list.
        head.next.next = head;
        //Set a null to the end of the current node.
        head.next = null;
        return temp;
    }

    public ListNode reverse_it(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode cur = head;
        ListNode prev = null;
        ListNode next = cur;

        while (cur != null) {
            if (cur.next == null) {
                cur.next = prev;
                break;
            }
            //Save the reference of the next pointer.
            next = cur.next;
            //change the next pointer of the cur to its prev.
            cur.next = prev;
            prev = cur;
            cur = next;

        }

        return cur;
    }
}
