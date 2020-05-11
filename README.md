# HUFS20-1_DataStructue
Labs and personal insights through the course

Prof - Chan Su Shin <br>
Labs and personal thoughts/trials about HUFS 2020-1 Data Structure class

## 01. Time Complexity
Calculate Big-O time complexity. Comapre and find which one is faster and suitable to use. <br>
|Time Complexity|Big-O|
|:---:|:---:|
| O(1) | all numeric time to go through the process |
| O(n) | when all time compelxity is calculated and your biggest degree of polynomial is 1 |
| O(n^2) | when all time compelxity is calculated and your biggest degree of polynomial is 2 |
| O(n^3) | when all time compelxity is calculated and your biggest degree of polynomial is 3 |
<br>
It works the same with exponentials and logarithms wise. (O(logn), O(n^1/2)

## 02. Stack and Queue
- Stack
- Queue
- LABS
  - ParenthesisCheck.py
  - PostfixCalculation.py

## 03. Linked List
- Singly Linked List
  - It can be used instead of Array. Node is made of the data and link. Data contains key value, and link contains the adress of the next node. At the end of the list, there is a node called None, which means there are no more nodes connected to the node, and it is the last end of the node. The first node of the list is called head, and the node before the None, last node with value, is called tail.
- Doubly Linked List
  - It covers the problem of deleting a node. Since singly Linked list needs to know the previous node of target to redirect the links of nodes. Doubly Linked List helps with deleting a node, or several nodes connected to each other, from a original list without searching for the previous node. But it doubles in the number of nodes to redirect. It may be complicated, but is worth doing because there are so much to earn by it.
  - In the course, I learned circular doubly linked list as a model form of doubly linked list.
-LABS
  - SinglyLinkedList.py
  - DoublyLinkedList.py
  - Josephus.py
  
## 04. Hash Table
- Hash tabel works like a dictionary. Map a key to a index with a hash function. If a slot is full with other item, collision occurs. To solve the collision and insert the value to a slot, we use Collision Resolution Method. 
- There are 3 different points to keep in mind to make the Hash table to work efficiently. 
  - Table is controlled with a list.
  - Hash function - How to insert a key, determining f(key).
  - Collision resolution methtod - How to solve a collisio if occured.
-LABS
  - HT_LinearProbing.py : Defining a class of Hash Table that works in open addressing way. Also known as linear probing, they both work in same way, filling the underneath of slot that is already filled. 
  - HT_FindSum.py : find a total number of pairs that sums up to k from a given list n. Used a class defined in HT_linear_probing.py, with a few change applied.
  
## 05. Heap
- Heap works in a way of tree structure. It needs to satisfy couple conditions to be a heap structure. 
  - All of parent node contains a key value that is not smaller than it's child node. 
  - The formation of tree needs to be in complete binary tree. 
- LAB
  - StreamOfMedian.py : Make a list of given integers and calculate a median of given variable k. Medians are stored as a list, and none of sorting algoritms, quick select, MOM structures can be used. Used two heaps to solve the problem. It adds all the medians stored in a list and returns the summation of it.

## 06. Tree

## 07. Balanced Binary Search Tree

## 08. Graph
