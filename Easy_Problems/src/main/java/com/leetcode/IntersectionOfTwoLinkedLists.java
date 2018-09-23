package com.leetcode;

/**
 * Write a program to find the node at which the intersection of two singly linked lists begins.
 *
 * @Author: Aaron Yang
 * @Date: 9/23/2018 10:56 AM
 */
public class IntersectionOfTwoLinkedLists {

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA, b = headB;
        int lenA = length(a);
        int lenB = length(b);
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA.next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB.next;
            }
        }

        while(headA != headB){
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }

    private int length(ListNode a) {
        int length = 0;
        while (a != null) {
            a = a.next;
            length++;
        }
        return length;
    }

    //Confused Solution
//    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
//        //boundary check
//        if(headA == null || headB == null) return null;
//
//        ListNode a = headA;
//        ListNode b = headB;
//
//        //if a & b have different len, then we will stop the loop after second iteration
//        while( a != b){
//            //for the end of first iteration, we just reset the pointer to the head of another linkedlist
//            if (a == null) a = headB;
//            else a = a.next;
//            b = b == null? headA : b.next;
//        }
//
//        return a;
//    }
}
