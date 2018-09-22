package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * Given a linked list, determine if it has a cycle in it.
 *
 * @Author: Aaron Yang
 * @Date: 9/22/2018 10:54 AM
 */
public class LinkedListCycle {

    public boolean hasCycle(ListNode2 head) {
        if(null == head) return false;
        Set<String> set = new HashSet<>();
        while (null != head && null != head.next){
            if(!set.add(head.toString())) return true;
            head = head.next;
        }
        return false;
    }

    //快慢指针
    //https://baike.baidu.com/item/%E5%BF%AB%E6%85%A2%E6%8C%87%E9%92%88/4630261?fr=aladdin
    public boolean hasCycle2(ListNode2 head) {
        ListNode2 slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast)
                return true;
        }

        return false;
    }
}

class ListNode2 {
    int val;
    ListNode2 next;

    ListNode2(int x) {
        val = x;
        next = null;
    }
}