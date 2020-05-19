# HUFS20-1_DataStructue
Labs and personal insights through the course

Prof - Chan Su Shin <br>
Labs and personal thoughts/trials about HUFS 2020-1 Data Structure class

## 01. Time Complexity
Calculate Big-O time complexity. Comapre and find which one is faster and suitable to use.

|Time Complexity|Big-O|
|:---:|:---:|
| O(1) | all numeric time to go through the process |
| O(n) | when all time compelxity is calculated and your biggest degree of polynomial is 1 |
| O(n^2) | when all time compelxity is calculated and your biggest degree of polynomial is 2 |
| O(n^3) | when all time compelxity is calculated and your biggest degree of polynomial is 3 |

It works the same with exponentials and logarithms wise. (O(logn), O(n^1/2)

- LAB
  - three_way_GCD : Calculate GCD in three different ways, subtracion, modification, and recursive subraction.
  - time_complexity_calculation : calculate operating time for sum function defined in the code.
  - two_way_prefix_sum : Calculate prefix sum of a list of random number in two different ways. Compare operating time of two calculating functions. 

## 02. Stack and Queue
- Stack
- Queue
- LABS
  - parenthesis_check.py : Check if a given string has matching parenthesis. Not only the numbers of each parenthesis, but the paring of it needs to match as well.
  - infix_to_postfix.py : Make a infix expression to a postfix expression. This will be calculating +, -, /, \*, % operators, and operands will be separated from operators with space. This code uses stack class to operate functions.
  - postfix_calculation.py : Calculate a postfix expression as a string, operands and operators are divided by a space. Only +, -, /, \*, % operators are used. Stack class will be used, and return value will be in a float number.
  - palindrome_check.py : This code will be updated soon.

## 03. Linked List
- Singly Linked List
  - It can be used instead of Array. Node is made of the data and link. Data contains key value, and link contains the adress of the next node. At the end of the list, there is a node called None, which means there are no more nodes connected to the node, and it is the last end of the node. The first node of the list is called head, and the node before the None, last node with value, is called tail.
  
- Doubly Linked List
  - It covers the problem of deleting a node. Since singly Linked list needs to know the previous node of target to redirect the links of nodes. Doubly Linked List helps with deleting a node, or several nodes connected to each other, from a original list without searching for the previous node. But it doubles in the number of nodes to redirect. It may be complicated, but is worth doing because there are so much to earn by it.
  - In the course, I learned circular doubly linked list as a model form of doubly linked list.
  
- LABS
  - singly_linked_list.py : Write a Node class, and SinglyLinkedList class. SinglyLinkedList class supports pushFront, pushBack, popFront, popBack, search, remove and printList functions. It is an interactive program, which will get an input line from user (ex : pushFront 10), and will push 10 to a list defined in the code. All input should be in a form of "command (space) number" or "command".
  - doubly_linked_list.py : It works in a same way with singly_linked_list.py but with few functional changes. This code provides splice, moveAfter, moveBefore, InsertAfter, InsertBefore, pushFront, pushBack, deleteNode, popFront, popBack, search, first, last, isEmpty and printList functions. Input command must be in a form of "command (space) number" or "command" like singly_linked_list.py.
  - josephus.py : Make a code for josephus game using doubly_linked_list.
  
## 04. Hash Table
- Hash tabel works like a dictionary. Map a key to a index with a hash function. If a slot is full with other item, collision occurs. To solve the collision and insert the value to a slot, we use Collision Resolution Method. 
- There are 3 different points to keep in mind to make the Hash table to work efficiently. 
  - Table is controlled with a list.
  - Hash function - How to insert a key, determining f(key).
  - Collision resolution methtod - How to solve a collision if occured.
  
- LABS
  - linear_probing.py : Defining a class of Hash Table that works in open addressing way. Also known as linear probing, they both work in same way, filling the underneath of slot that is already filled. 
  - find_sum.py : find a total number of pairs that sums up to k from a given list n. Used a class defined in linear_probing.py, with a few change applied.
  
## 05. Heap
- Heap works in a way of tree structure. It needs to satisfy couple conditions to be a heap structure. 
  - All of parent node contains a key value that is not smaller than it's child node. 
  - The formation of tree needs to be in complete binary tree. 
  
- LAB
  - stream_of_median.py : Make a list of given integers and calculate a median of given variable k. Medians are stored as a list, and none of sorting algoritms, quick select, MOM structures can be used. Used two heaps to solve the problem. It adds all the medians stored in a list and returns the summation of it.

## 06. Tree

## 07. Balanced Binary Search Tree

## 08. Graph
