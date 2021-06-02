#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Node:
    
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    
    def __init__(self):
        self.root = None
        
    def Insert(self, value):
        self.root = self.__InsertWrap(self.root, value)
        
    def __InsertWrap(self,x, value):
        if x == None:
            x = Node(value)
            
        else:
            if value < x.value:
                #print("left")
                x.left = self.__InsertWrap(x.left, value)
            else:
                #print("right")
                x.right = self.__InsertWrap(x.right, value)
        return x
    
    def InOrder(self):
        return self.__InOrder(self.root)
    
    def __InOrder(self, x):
        if x:
            self.__InOrder(x.left)
            print(x.value)
            self.__InOrder(x.right)

            
    def PreOrder(self):
        return self.__PreOrder(self.root)
    
    def __PreOrder(self,x):
        if x:
            print(x.value)
            self.__PreOrder(x.left)
            self.__PreOrder(x.right)
            
    def PostOrder(self):
        return self.__PostOrder(self.root)
    
    def __PostOrder(self,x):
        if x:
            self.__PostOrder(x.left)
            self.__PostOrder(x.right)
            print(x.value)
            
    def FindMin(self, x ):
        while(x.left != None):
            x = x.left
        return (x.value)
    
    def FindMax(self, x ):
        while(x.right != None):
            x = x.right
        return (x.value)
    
    def successor(self, x): 
        if x.right !=  None:
            xx = x.right
            while (xx.left != None):
                xx = xx.left
        return xx.value
    
    def predecessor(self, x ):
        if x.left != None:
            xx = x.left
            while(xx.right != None):
                xx = x.right
        return xx.value
    
    def Height(self, x ):
        y = self.__Height(x)
        return y
    
    def __Height(self,x):
        if x==None:
            return 0
        else:
            return 1 + max(self.__Height(x.left),self.__Height(x.right))
    
    def delete(self, node):
        x = self.root       #rootNode, {Parent Node of desired Node}
        
        if node > x.value:
            y = x.right      #desiredNode {Node to be delted} [iff on right]
        
        else:
            y = x.left      #desiredNode [iff left]
        
        while(y.value != node):   # Searching the Node to delete
            if node > y.value:
                x = x.right
                y = y.right
        
            else:
                x = x.left
                y = y.left
                
        
        #print("xr", x.right.value)
        #print("y", y.value)
        
        left = x.left          #left of ParentNode
        right = x.right         #right of ParentNode
        
        # Case 01
        
        if left.value == y.value and left.left is None and left.right is None:
            #print("left", x.left.value)
            x.left = None
            
        elif right.value == y.value and right.left is None and right.right is None:
            #print("right", x.right.value)
            x.right = None
            
        # Case 02
        
        elif left.value == y.value and (left.left is not None and left.right is None) or (left.left is None and left.right is not None):
            if left.left is not None:
                child = left.left
            
            elif left.right is not None:
                child = left.right
            x.left = None
            x.left = child
            #print("x",x.left.value)
            
        elif right.value == y.value and (right.left is not None and right.right is None) or (right.left is None and right.right is not None):
            if right.left is not None:
                child = right.left
            
            elif right.right is not None:
                child = right.right
            x.right = None
            x.right = child
            
        # Case 03
        
        elif left.value == y.value and left.left is not None and left.right is not None:
            lChild = left.left
            rChild = left.right
            min = self.successor(left)
            self.delete(min)
            minNode = Node(min)
            minNode.left = lChild
            minNode.right = rChild
            x.left = None
            x.left = minNode
            
        elif right.value == y.value and right.left is not None and right.right is not None:
            lChild = right.left
            rChild = right.right
            min = self.successor(right)
            self.delete(min)
            minNode = Node(min)
            minNode.left = lChild
            minNode.right = rChild
            x.right = None
            x.right = minNode

# Driver Code

a = BST()
a.Insert(20)
a.Insert(40)
a.Insert(12)
a.Insert(1)

root = a.root

print("Getting Inorder:")
a.InOrder()

print("\nGetting Preorder:")
a.PreOrder()

print("\nGetting PostOrder:")
a.PostOrder()

print("\nGetting Height:")
print(a.Height(root))

print("\nGetting Minimum Node:")
print(a.FindMin(root))

print("\nGetting Maximum Node:")
print(a.FindMax(root))

print("\nGetting Successor:")
print(a.successor(root))

print("\nGetting Predecessor:")
print(a.predecessor(root))

print("\nDeleting a specific Node:")
a.delete(12)

print("\nTo cross-check deletion, printing preorder:")
a.PreOrder()


# In[ ]:




