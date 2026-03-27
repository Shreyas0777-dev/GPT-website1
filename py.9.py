class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Doublylinkedlist:
    def __init__(self):
        self.first=None
    def insertfirst(self,data):
        newnode=Node(data)
        if self.first==None:
            self.first=newnode
        else:
             newnode.next=self.first
             self.first=newnode
    def removefirst(self):
        if (self.first==None):
            print("list is empty")
        else:
            cur=self.first
            self.first=self.first.next
            print("the deleted element is:",cur.data)
    def display(self):
        if(self.first== None):
            print("list is empty")
            return
        cur=self.first
        while(cur):
            print("cur.data",end=" ")
            cur=cur.next
    def search(self,item):
        if(self.first==None):
            print("list is empty")
            return
        cur=self.first
        found=False
        while cur!=None:
            if cur.data==item:
               print("the data item is present in the list")
            else:
                cur=cur.next
                print("the data item is not present")
sll=Doublylinkedlist()
while(True):
    choice=int(input("\nenter your choice 1-insert 2-delete 3-search 4-display 5-exit:"))
    if(choice==1):
        item=input("enter the element to insert:")
        sll.insertfirst(item)
        sll.display()
    elif(choice==2):
        sll.removefirst()
        sll.display()
    elif(choice==3):
        item=input("enter the element to search:")
        sll.search(item)
    elif(choice==4):
        sll.display()
    else:
        break
                        
    
            
        
