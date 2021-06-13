#  a data structure linked list in python usind two class , Node and LinkedList

## checklist
- Can successfully instantiate an empty linked list
array = LinkedList()

- Can properly insert into the linked list
array.insert(0)    {0}->Null

- The head property will properly point to the first node in the linked list
print(array.head.value)     0

- Can properly insert multiple nodes into the linked list
array.insert(0)
array.insert(1)

- Will return true when finding a value within the linked list that exists otherwise return false

print(array.includes(0),array.includes(8))      True   False
