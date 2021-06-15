
from linked_list import LinkedList



def zipLists(list_one,list_two):
    if (list_one.head!=None):
        current_one=list_one.head
        current_two=list_two.head
        
        print(current_one)
      
    while current_one:

        list_one.insertAfter(current_one.value,current_two.value)
        current_one=current_one.next.next
        current_two=current_two.next
        if current_one==None:
            break

    while current_two:
        list_one.append(current_two.value)
        current_two=current_two.next

if __name__ == '__main__':

    array2 = LinkedList()
    array = LinkedList()
    array.append(1)
    array.append(2)

    array.append(3)
    array2.append(4)
    array2.append(5)

    

    array2.append(6)
    

    zipLists(array,array2)
    print(array)
