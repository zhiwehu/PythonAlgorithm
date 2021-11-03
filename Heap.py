#!/usr/bin/env python
# coding: utf-8

# In[103]:


# Algo : 1 - Max Heapify

class heap:
    
# Heap Function
    
    def MaxHeapify(self,array):
        
# Getting lengtyh of array

        length = len(array)
        
#  Initiating a loop which starts from the element before mid of array 
#  to last index while skipping an element
    
        for i in range((length//2) - 1, -1, -1):
            
# Calling Wrapper Function

            self._MaxHeapify(array, length, i)
            
    
# Making wrapper function - Separating logic from main function
    
    def _MaxHeapify(self, array, length, index):
        
# Here, we'll first build our max heap
        
# For inserting the left child of node

        left = 2 * index + 1
    
# For inserting the right child of node

        right = 2 * index + 2
    
# Defining condition to set the left child as root
        
        if left < length and array[left] > array[index]:
            largest = left
        
        else:
            largest = index
            
# Defining condition to set the right child as root 

        
        if right < length and array[right] > array[largest]:
            largest = right
            
# Condition to check if current node isn't the largest
   
        if (largest != index):
            
# Swapping to fulfil max heap property of getting the highest value to upper levels of heap

            array[largest], array[index] = array[index], array[largest]
            self._MaxHeapify(array, length, largest)
            

            
# Driver Code

array = [550,4520,3,2340,12]
print("Array before Max Heapify = ", array)
ob = heap()

ob.MaxHeapify(array)
print('Array after Max Heapify =',array)


# In[120]:


# Algo : 2 - Building Max Heap

def heapify(array, length, index):
    
    # Initializing the largest value as root of heap
  
    largest = index
    
    # Defining formula to insert the left chikd of node
    
    left = 2 * index + 1
    
    # Defining formula to insert the right chikd of node
    
    right = 2 * index + 2
  
    # Condition to check if left child is larger than root
    
    if left < length and array[left] > array[largest]:
        largest = left
  
    # Condition to check if right child is larger than the current largest node
    
    if right < length and array[right] > array[largest]:
        largest = right
  
    #  Condition to check if current node isn't the largest
    
    if largest != index:
        
        #   Swapping to fulfil max heap property of getting the highest value to upper levels of heap

        array[index], array[largest] = array[largest], array[index]
        heapify(array, length, largest)

# Function to build a Max-Heap from the given array

def buildHeap(array, length):
  
    # Index of last node which isn't a leaf
    
    startingIndex = length // 2 - 1
    
    # Initializing a loop from the last node that isn't a leaf to the last node of array skipping 1 element

    for i in range(startingIndex, -1, -1):
        heapify(array, length, i)

def printHeap(array, length):
    print("Array representation of Heap is:")
  
    for i in range(length):
        print(array[i], end = " ")
    print()
    

    
# Driver Code

array = [ 1, 3, 5, 4, 6, 13, 10, 9, 8, 18, 17 ]
length = len(array);
buildHeap(array, length);
printHeap(array, length);


# In[142]:


# Algo : 3 - Extract_Heap_Max ;  Remove any node

# Here we'll utilize the code of Algo 2, as algo 2 gives us a max heap in the form of array, therefore 
# element at the zeroth index of array will have the maximum value


def getMax(array, length):
    maximum = array[0]
    print("The maximum value in heap is ", maximum)
    
# Driver Code

array = [ 1, 3, 5, 4, 6, 13, 10, 9, 8, 18, 17 ]
length = len(array);
buildHeap(array, length);
getMax(array, length);


# To check by removing any node from our heap, remove any value in our array. Here's a sample of it

# Removing 18 from above array,

array = [ 1, 3, 5, 4, 6, 13, 10, 9, 8, 17 ]
length = len(array);
buildHeap(array, length);

print("After Removal:")
getMax(array, length)


# In[175]:


# Algo : 4 - Heap_Increase_key  Increase to value stored at any node

def IncreaseKey(Array, index, key):

#     Setting Key
    
    Array[index] = key
    
#     Setting Parent
    Parent = index//2
    
#     Condition to traverse the heap
    
    while i > 1 and Array[Parent] < Array[i]:
        if Parent < A[i]:
            
#   Swapping current counter node with its parent
            
            Array[i], Array[Parent(i)] = Array[Parent(i)], Array[i]
        
# Setting the increased key to the index     

            i = Parent(i)

Array = [3,52,2,57,1]            
increase(Array, Array[2], 5)
print(arr)


# In[140]:


# Algo : 5 - Insert_MaxHeap Insert new node

import sys
  
class MaxHeap:
  
    def __init__(self, maxsize):
          
    # Defining attributes of heap
    
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1
  
    # To return the position of parent of node at a specific position 
    
    def parent(self, pos):
          
        return pos // 2
  
    # To return the position of the left child of node at a specific position
    
    def leftChild(self, pos):
          
        return 2 * pos
  
    # To return the position of the right child of node at a specific position
    
    def rightChild(self, pos):
          
        return (2 * pos) + 1
    
    #  Ti check if the node is a leaf or not
    
    def isLeaf(self, pos):
          
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    # To swap two nodes of the heap
    
    def swap(self, fpos, spos):
          
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])
  
    # To max heapify the node at a specific position
    
    def maxHeapify(self, pos):
  
    # Condition to check node is not at leaf position
        
        if not self.isLeaf(pos):
            
            # Condition to check node is smaller than its left child

            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                
                # Condition to check node is smaller than its right child

                self.Heap[pos] < self.Heap[self.rightChild(pos)]):


                if (self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]):
                    
                    #  Swapping with left child
                    
                    self.swap(pos, self.leftChild(pos))
                    
                    #  Max-Heapifying left child

                    
                    self.maxHeapify(self.leftChild(pos))
  
                # Swap with the right child 
    
                else:
                    self.swap(pos, self.rightChild(pos))
                    
                    #  Max-Heapifying right child

                    self.maxHeapify(self.rightChild(pos))
  
    # To insert a node into the heap
    
    def insert(self, element):
          
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
  
        current = self.size
    
#   Comparing values of current node to parent node

        while (self.Heap[current] > self.Heap[self.parent(current)]):
    
#  Swap if value of current node is bigger than that of parent's

            self.swap(current, self.parent(current))
    
#   Setting the current node as parent fter swapping

            current = self.parent(current)

        
# To remove and extract maximum value of heap
    
    def extractMax(self):
  
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
          
        return popped


# Driver Code
      
maxHeap = MaxHeap(15)
maxHeap.insert(5)
maxHeap.insert(3)
maxHeap.insert(17)
maxHeap.insert(10)
maxHeap.insert(84)
maxHeap.insert(19)
maxHeap.insert(6)
maxHeap.insert(22)
maxHeap.insert(9)
  
      
print("The Maximum value is " + str(maxHeap.extractMax()))

