class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None #start from empty list

    def insert(self,value):
        new_node=Node(value)
        if self.head==None: # if there is no value as a head , make the new inserted on the head 
            self.head=new_node
        else:
            current=self.head
            while current.next!=None: # while a list doesn't contain an only value 
                current=current.next # make a current value the one next to the head .. until current.next=none ,which mean the last elem
            current.next=new_node   

    def includes(self,value):
        current=self.head  # means start from the first element
        while current!=None:
            if current.value==value:
                return True

            else:
                current=current.next # means continue searching 
        return False 

    def __str__(self):
         if self.head!=None:
             list=''
             current=self.head
             while current:
                 list+=f'{{{current.value}}} ->'   
                 current=current.next
             list+='NULL'
             return list
         else:
            return 'It is an empty list !!!'     


if __name__ == '__main__':

    array = LinkedList()
    array.insert(0)
    array.insert(1)
    print(array)
    print(array.includes(0),array.includes(8)) 
    print(array.head.value)


