# -*- coding: utf-8 -*-
"""
Created on Thu Mar 06 20:46:35 2014

@author: Michael
"""

# Write code to remove duplicates from an unsorted linked list
# Follow up
# How would you solve this problem if a temporary buffer is not allowed

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def AddNode(self, data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node
    
    def RemoveNode(self, index):
        node = self.head
        previous = None
        following = None
        
        if index == 0:
            self.head = node.next
        else:    
            for i in range (index+1):
                if(i == index - 1):
                    previous = node 
                node = node.next           
            following = node
            previous.next = following
            if node == self.tail:
                self.tail = previous 
            else: 
                previous.next = following
                self.tail = following
    
    def PrintList( self ):
      node = self.head

      while node != None:
         print node.data
         node = node.next

List = LinkedList()
List.AddNode(1)
List.AddNode(2)
List.AddNode(3)
List.AddNode(2)

List.PrintList()

def deleteDups(List):
    if (List.head != None):
        currNode = List.head
        dic =  {currNode.value: True}
        while currNode.next != None:
            if currNode.next.value in dic:
                currNode.next = currNode.next.next
            else:
                dic[currNode.next.value] = True
                currNode = currNode.next

deleteDups(List)
print List