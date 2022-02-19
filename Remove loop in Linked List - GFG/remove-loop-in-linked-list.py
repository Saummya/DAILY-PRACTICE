'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        if head:
            temp=head
            temp.data=-1*temp.data
            while temp.next:
                if temp.next.data<0:
                    temp.next=None
                    break
                else:
                    temp.next.data=-1*temp.next.data
                temp=temp.next
            
        
        
        # remove the loop without losing any nodes
        '''
        slow=head
        fast=head
        loop_found = False
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                loop_found = True
                break
        
        
        if loop_found:
            loop_length = 1
            while slow.next != fast:
                slow = slow.next
                loop_length+=1
            
            curr = head
            forward = head
            len = 0
            prev = None
            while len < loop_length:
                prev = forward
                forward = forward.next
                len+=1
                
            while curr != forward:
                curr = curr.next
                prev = forward
                forward = forward.next'''
            
            
            
        


#{ 
#  Driver Code Starts
# driver code:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,num):
        if self.head is None:
            self.head=Node(num)
            self.tail=self.head
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next
    
    def isLoop(self):
        if self.head is None:
            return False
        
        fast=self.head.next
        slow=self.head
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next
        
        return True
    
    def loopHere(self,position):
        if position==0:
            return
        
        walk=self.head
        for _ in range(1,position):
            walk=walk.next
        self.tail.next=walk
    
    def length(self):
        walk=self.head
        ret=0
        while walk:
            ret+=1
            walk=walk.next
        return ret

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=tuple(int(x) for x in input().split())
        pos=int(input())
        
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)
        
        Solution().removeLoop(ll.head)
        
        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)

# } Driver Code Ends