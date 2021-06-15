
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

   

    def append(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=node

    def insertBefor(self,value,newVal):
        if self.includes(value) == True:
            node= Node(newVal)
            if self.head.value == value:
                return self.insert(newVal)
            current=self.head
            while  current.next.value!= value:
                current = current.next
            node.next = current.next
            current.next=node


    def insertAfter(self,value,newVal):
        if (self.includes(value) == False):
            return('Value does not exist.')
        else:
            node = Node(newVal)
            current = self.head
            while(current.value != value):
                current = current.next
            node.next = current.next
            current.next = node


    def list_length(self):
        current=self.head
        length=0
        while (current):
            length+=1
            current=current.next
        return length


    def kth_from_end(self,k):
        list_length=self.list_length()
        if type(k)!=int or k<0:
            raise TypeError('You entered a non valid value , enter positive integer number')
        elif k>list_length-1:
            raise IndexError('index out of range')
        elif list_length==0:
            raise Exception('List is empty')    

        else:
            result=[]
            current=self.head

        while (current):
            result+=[current.value]
            current=current.next
            if current==None:
                break

        return result[::-1][k]            

                        



      
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

    array.append(5)
    array.insertAfter(1,3)
    array.insertBefor(5,10)

    print(array)
    # print(array.includes(0),array.includes(8)) 
    # print(array.head.value)
    print(array.kth_from_end(4))
    # print(array.kth_from_end(-1))
    # print(array.kth_from_end('q'))
    # print(array.kth_from_end(10))
    
    print(array)


