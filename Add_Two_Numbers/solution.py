    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        p = ListNode(0)
        q = ListNode(0)
        q.next = p
        carry = 0
        
        while l1 is not None and l2 is not None:
            num = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) / 10
            p.val = num
            
            if l1.next is not None or l2.next is not None:
                p.next = ListNode(0)
                p = p.next
                
            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            num = (l1.val + carry) % 10
            carry = (l1.val + carry) / 10
            p.val = num
            
            if l1.next is not None:
                p.next = ListNode(0)
                p = p.next
                
            l1 = l1.next
        
        while l2 is not None:
            num = (l2.val + carry) % 10
            carry = (l2.val + carry) / 10
            p.val = num
            
            if l2.next is not None:
                p.next = ListNode(0)
                p = p.next
                
            l2 = l2.next
        
        if carry > 0:
            p.next = ListNode(carry)
            p = p.next
        
        return q.next