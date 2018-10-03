package com.leetcode;

import java.util.LinkedList;
import java.util.List;

/**
 * Implement the following operations of a stack using queues.
 *
 * @Author: Aaron Yang
 * @Date: 10/3/2018 9:49 AM
 */
public class ImplementStackUsingQueues {

    public static void main(String[] args) {

//        Your MyStack object will be instantiated and called as such:
        MyStack obj = new MyStack();
        obj.push(1);
        obj.push(2);
        obj.push(3);
        int param_2 = obj.pop();    //3
        int param_3 = obj.top();       //2
        boolean param_4 = obj.empty();  //false

    }

}

class MyStack {

    private List<Integer> aList = new LinkedList<>();
    private List<Integer> bList = new LinkedList<>();
    private Integer top;

    /**
     * Initialize your data structure here.
     */
    public MyStack() {
    }

    /**
     * Push element x onto stack.
     */
    public void push(int x) {
        top = x;
        aList.add(x);
    }

    /**
     * Removes the element on top of the stack and returns that element.
     */
    public int pop() {
        while (aList.size() > 1) {
            bList.add(aList.remove(0));
        }
        top = aList.remove(0);
        LinkedList temp = (LinkedList) aList;
        aList = bList;
        bList = temp;
        return top;
    }

    /**
     * Get the top element.
     */
    public int top() {
        return aList.get(aList.size() - 1);
    }

    /**
     * Returns whether the stack is empty.
     */
    public boolean empty() {
        return aList.isEmpty();
    }
}
