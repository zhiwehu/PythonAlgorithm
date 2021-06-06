#!/usr/bin/env python
# coding: utf-8

# In[7]:


class ArrayStack:
    def __init__(self,size):
        self.size=size
        self.List=[0 for i in range(size)]
        self.top=0
    def Push(self,value):
        if self.top!=self.size:
            self.List[self.top]=value
            self.top=self.top+1
            print(self.List)
        else:
            print("Stack Overflow")
    def Pop(self):
        if self.IsEmpty():
            print("Stack Underflow")
        self.top=self.top-1
        x=self.List[self.top]
        return x
        
    def IsEmpty(self):
        if self.top==0:
            print("Stack Underflow")
    def Peek(self):
        return (self.List[self.top - 1])
    def Count(self):
        print ("The number of elements in stack is",self.size,"!!!")
    def strExp(self,String):
        s=ArrayStack(len(String))
        for i in String:
            if i == "(" or i== "{" or i == "[":
                s.Push(i)
            
            elif i == ")" or i== "}" or i== "]":
                s.Pop()
            
        if s.IsEmpty() == True:
            print("True")
    def Print(self):
        print(self.List)

        
# Driver Code 

size=4
ob=ArrayStack(size)

print("Pushing elements into stack: ")

ob.Push(7)
ob.Push(2)
ob.Push(8)
ob.Push(9)
print("\n")
ob.Push(2)
ob.Print()

print("\nPopping element from stack: ")

ob.Pop()
ob.Print()

print("\nPeek in stack: ")


ob.Peek()
ob.Print()

print("\nCounting elements in stack: ")
ob.Count()

print("\nString expression in stack: ")
String = "{}()["
ob.strExp(String)


# In[6]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.rear = None # head
        self.front = None # tail
        
    def enqueue(self,value):
        newnode=Node(value)
        if self.rear==None:
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
            
    def dequeue(self):
        if self.front==None:
            print("Stack underflow")
        else:
            self.front=self.front.next 
    
    def Print(self):
        a=self.front
        while a!=None:
            print(a.value,end=" ")
            a=a.next
        print()
            
            
ob=Queue()
print("when inserted in queue")
ob.enqueue(4)
ob.enqueue(3)
ob.enqueue(2)
ob.Print()
print("when deleted from queue")
ob.dequeue()
ob.Print()


# In[ ]:




