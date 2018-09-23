package com.leetcode;

/**
 * Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 *
 * @Author: Aaron Yang
 * @Date: 9/23/2018 9:32 AM
 */
public class MinStack {

    private Node node;

    public MinStack() {
    }

    public void push(int x) {
        if(null == node ){
            node = new Node(x,x,null);
        }else {
            node = new Node(x, Math.min(x, node.min), node);
        }
    }

    public void pop() {
        node = node.next;
    }

    public int top() {
        return node.val;
    }

    public int getMin() {
        return node.min;
    }

    public static void main(String[] args) {
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin();   //--> Returns -3.
        minStack.pop();
        minStack.top();     // --> Returns 0.
        minStack.getMin();   //--> Returns -2.
    }
}

class Node {

    protected int val;
    protected int min;
    protected Node next;

    public Node(int val, int min, Node next) {
        this.val = val;
        this.min = min;
        this.next = next;
    }
}
/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */