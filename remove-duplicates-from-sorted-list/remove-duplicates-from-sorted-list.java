/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode cur = head;
        int prev = head.val;
        while(cur.next != null){
            if(cur.next.val == prev){
                cur.next = cur.next.next;
            }
            else{
                cur = cur.next;
            }
            prev = cur.val;
        }
        return head;
        
    }
}