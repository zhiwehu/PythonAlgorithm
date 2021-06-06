#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Vertex:
    
    def __init__(self,value):
        
        self.value=value
        self.dist=float("inf")
        self.predecessor=value #jesy graph mai 1 sy 2 gaya aur phir 2 sy 3 edge hai tou 3 ka pred 2 hai
        self.visited=False
        
#MINIMUM PRIORITY QUEUE GIVES MINIMUM VALUE
#THEN WE PUT OBJECTS IN A LIST
#MINIMUM FUNCTION NEVER APPLYS ON OBJECTS THAT'S WHY WE WILL FIND MINIMUM VALUE FROM LINEAR SEARCH
#PRIORITY QUEUE APPLIES WRT MINIMUM VALUE


class PriorityQueue:
    
    def __init__(self):
        self.list=[]
    def is_empty(self):
        if self.list==[]:
            return True
        return False
   
    def Enqueue(self,v):
        self.list.append(v)
       
    def Extract_min(self):
        minloc=self.__Findmin()
        y=self.list[minloc]#pop kara re hain taky list emty hojai
        self.list.pop(minloc)
        return y
    
    def __Findmin(self):
        minloc= self.list[0]
        loc=0
       
        for i in range(len(self.list)):
            if self.list[i].dist<minloc.dist:
                minloc=self.list[i]
                location=i
        return loc
    
class DGraph:
    
    def __init__(self,vertex):
        self.vertex=vertex
        self.adjmat=[[0 for i in range(vertex)]for j in range(vertex)]
        
    def Add_Directed_edges(self,src,dest,weight):
        self.adjmat[src][dest]=weight
       
    def Get_Directed_neighbour(self,source):
        neg=[]
        for i in range(self.vertex):
            if self.adjmat[source][i]>0:
                neg.append(i)
        return neg
    
    def Dijkstra_shortest_path(self,source):
       #INTIALIZING A EMPTY LIST FOR SORTING VERTEX OBJECTS
        cost=[]
        q=PriorityQueue()
        
        #CREATE A VERTEX OBJECTS
        for i in range(self.vertex):
            cost.append(Vertex(i))
            
        #INTIALIZING THE OBJECTS FROM SOURCE TO ZERO AND OTHER VERTICES TO INFINITY
        for i in range(self.vertex):
            cost[i].dist=float("inf")
        cost[source].dist=0
       
        #ENQUEUE OBJECTS
        for i in range(self.vertex):
            q.Enqueue(cost[i])
            
        #CHECK UNTIL QUEUE IS EMPTY
        while not q.is_empty():
            z=q.Extract_min()
            self.visited=True
            print("visited {}".format(z.value))
           
            neighbours=self.Get_Directed_neighbour(z.value)
           
            for i in neighbours:
                if cost[i].visited ==False and cost[i].dist>z.dist+self.adjmat[z.value][i]:
                    cost[i].dist=z.dist+self.adjmat[z.value][i]
                    cost[i].pred=z.value
        for j in cost:
            print(j.value,j.dist,j.predecessor)

# Array Stack

a=DGraph(4)

class ArrayStack():
    
    def __init__(self, size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.top = 0
   
    def Push(self, value):
        if self.top != ((self.size)):
            self.data[self.top] = value
            self.top += 1
            return(self.top , value)
        else:
            return("STACK OVERFLOW")
    
    def Pop(self):
        
        if self.top != 0:
            x = self.data[self.top-1]
            self.top -= 1
            return(x)
        
        else:
            return("STACK UNDERFLOW")
    
    def Peek(self):
        return(self.data[self.top-1])
    
    def isEmpty(self):
        if self.top == 0:
            return True
        else:
            return False
    
    def Count(self):
        return len(self.data)
    
    def Print(self):
        print(self.data)

# Queue

class ArrayQueue:
    
    def __init__(self,size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.rear = 0
        self.front = -1
    
    def IsEmpty(self):
        if self.rear == 0:
            return True
        else:
            return False
    
    def Enqueue(self, value):
        self.data[self.rear] = value
        self.rear = (self.rear+1)%self.size
        return self.data
    
    def Dequeue(self):
        x = self.data[self.front]
        self.front = (self.front+1)%self.size
        return x
    
    def Count(self):
        return len(self.data)
    
    def Print(self):
        print(self.data)

# Graph

class Graph:
    
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj = [[0 for i in range(vertex)] for j in range(vertex)]
        
    def addEdge(self, src,dest):
        if src == dest:
            print("Source and dest r same")
        else:
            self.adj[src][dest] = 1
            self.adj[dest][src] = 1
            
    def printMatrix(self):
        for i in self.adj:
            for j in i:
                print(j, end="  ")
            print("\r")
            
    def getNeighbours(self,src):
        neighbours = []
        for i in range(len(self.adj)):
            k = self.adj[i]
            #print(i[src+1])
            if k[src] == 1:
                neighbours.append(i)
        return neighbours
    
    def DFS(self,source):
        visited = []
        s = ArrayStack(self.vertex)
        s.Push(source)
        visited.append(source)
        while not (s.isEmpty()):
            x = s.Pop()
            print("visited", x)
            n = self.getNeighbours(x)
            for i in range(len(n)+1):
                if i not in visited:
                    s.Push(i)
                    visited.append(i)
        return visited
    
    def BFS(self, src):
        visited = [False] * self.vertex
        q = ArrayQueue(self.vertex)
        q.Enqueue(src)
        visited[src] = True
               
        while not (q.IsEmpty()):
            x = q.Dequeue()
            print("visited", x)
            n = self.getNeighbours(x)
            for i in range(len(n)+1):
                if visited[i] == False:
                    print("HI", i)
                    q.Enqueue(i)
                    visited[i] = True
                    
    def newBFS(self, src):
        visited = []
        q = ArrayQueue(self.vertex)
        q.Enqueue(src)
        visited.append(src)
        while not q.IsEmpty():
            x = q.Dequeue()
            print("visited", x)
            neighbours = self.getNeighbours(x)
            for i in neighbours:
                if i not in visited:
                    q.Enqueue(i)
                    visited.append(i)
        return visited
    
# Driver Code

a = Graph(3)
a.addEdge(0,1)
a.addEdge(1,2)

print("Printing Matrix:")
a.printMatrix()

print("\nGetting Neighbours:")
print(a.getNeighbours(1))

print("\nPerforming DFS:")
print(a.DFS(2))

print("\nPerforming BFS:")
print(a.newBFS(2))


