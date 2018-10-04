package com.leetcode;

import java.util.Stack;

/**
 * Implement the following operations of a queue using stacks.
 * <p>
 * You must use only standard operations of a stack -- which means
 * only push to top, peek/pop from top, size, and is empty operations are valid.
 * <p>
 * Depending on your language, stack may not be supported natively.
 * You may simulate a stack by using a list or deque (double-ended queue),
 * as long as you use only standard operations of a stack.
 * <p>
 * You may assume that all operations are valid
 * (for example, no pop or peek operations will be called on an empty queue).
 *
 * @Author: Aaron Yang
 * @Date: 10/4/2018 10:23 AM
 */
public class ImplementQueueUsingStacks {

    public static void main(String[] args) {

//        Your MyQueue object will be instantiated and called as such:
        MyQueue obj = new MyQueue();
        obj.push(1);
        int param_2 = obj.pop();    //1
        obj.push(2);
        int param_3 = obj.peek();   //2
        boolean param_4 = obj.empty();  //false

    }
}

class MyQueue {

    Stack aStack = new Stack<Integer>();
    Stack bStack = new Stack<Integer>();
    Integer front = 0;

    /**
     * Initialize your data structure here.
     */
    public MyQueue() {

    }

    /**
     * Push element x to the back of queue.
     */
    public void push(int x) {
        aStack.push(x);
        if (bStack.isEmpty()) {
            front = x;
            bStack.push(x);
        }
    }

    /**
     * Removes the element from in front of queue and returns that element.
     */
    public int pop() {
        Integer temp = 0;
        if (!bStack.empty()) {
            temp = (Integer) bStack.pop();
        } else {
            temp = front;
        }
        int size = aStack.size() - 1;
        for (int i = 0; i < size; i++) {
            bStack.push(aStack.pop());
            front = (Integer) bStack.peek();
        }
        aStack.clear();
        for (int i = 0; i < size; i++) {
            aStack.push(bStack.pop());
        }
        if (aStack.size() != 0) bStack.push(front);
        return temp;
    }

    /**
     * Get the front element.
     */
    public int peek() {
        return front;
    }

    /**
     * Returns whether the queue is empty.
     */
    public boolean empty() {
        return aStack.empty();
    }
}

