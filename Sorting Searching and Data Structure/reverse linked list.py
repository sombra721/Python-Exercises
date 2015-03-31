
class SinglyLinkedList( object ):
 
  def __init__( self ):
    self.head , self.tail = None, None
 
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
 
 
class Node( object ):
 
  def __init__( self, data, next = None ):
    self.data = data
    self.next = next
    
