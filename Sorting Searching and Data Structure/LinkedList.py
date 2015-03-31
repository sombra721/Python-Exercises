# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
Created on Sun Mar 02 02:32:37 2014

@author: Michael
"""
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
         
    def reverse( self ) :
        if None == self.head or None == self.head.next:
            return
 
        a = self.head
        b = a.next
        c = b.next
     
        # swaps
        a.next = None
        b.next = a;
        a = b;
        while None != c:
          b = c
          c = c.next
          b.next = a
          a = b
     
        self.head = b
 

List = LinkedList()
List.AddNode(1)
List.AddNode(2)
List.AddNode(3)
List.AddNode(7)
List.RemoveNode(2)

List.PrintList()

List.reverse()

List.PrintList()