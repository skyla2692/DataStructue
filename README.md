# DataStructue
Personal note about Data Structure. <br>
Language used for lab : Python

## 01. Time Complexity
Calculate Big-O time complexity. Comapre and find which one is faster and suitable to use.

|Time Complexity|Big-O|
|:---:|:---:|
| O(1) | all numeric time to go through the process |
| O(n) | when all time compelxity is calculated and your biggest degree of polynomial is 1 |
| O(n^2) | when all time compelxity is calculated and your biggest degree of polynomial is 2 |
| O(n^3) | when all time compelxity is calculated and your biggest degree of polynomial is 3 |

It works the same with exponentials and logarithms wise. (O(logn), O(n^1/2)

- LAB :
  - three_way_GCD : Calculate GCD in three different ways, subtracion, modification, and recursive subraction.
  - time_complexity_calculation : calculate operating time for sum function defined in the code.
  - two_way_prefix_sum : Calculate prefix sum of a list of random number in two different ways. Compare operating time of two calculating functions. 

## 02. Stack and Queue
- Stack
  - It is a linear data structure, which follows Last In First Out (LIFO) rule. 
  - Data are saved in a list, and push(), pop(), top(), isEmpty(), size() functions are supported.
  - There are three expressions of stack, Infix, Prefix, Postfix.

| Infix Expression | Prefix Expression | Postfix Expression |
|:---:|:---:|:---:|
| A + B * C + D | + + A * B C D | A B C * + D + |
| (A + B) * (C + D) | * + A B + C D | A B + C D + * |
| A * B + C * D | + * A B * C D | A B * C D * + |
| A + B + C + D | + + + A B C D | A B + C + D + |

- Queue
  - It is also a linear data structure, which folllows First In First Out (FIFO) rule. 
  - Data are saved in a list, and enqueue(), dequeue(), isEmpty(), front(), len() functions are supported.
  - Dequeue : A list that can be inserted and deleted from both sides. But you need to write two versions of push and pop functions.

- LAB :
  - parenthesis_check.py : Check if a given string has matching parenthesis. Not only the numbers of each parenthesis, but the paring of it needs to match as well.
  - infix_to_postfix.py : Make a infix expression to a postfix expression. This will be calculating +, -, /, \*, % operators, and operands will be separated from operators with space. This code uses stack class to operate functions.
  - postfix_calculation.py : Calculate a postfix expression as a string, operands and operators are divided by a space. Only +, -, /, \*, % operators are used. Stack class will be used, and return value will be in a float number.
  - palindrome_check.py : This code will be updated soon.

## 03. Linked List
- Singly Linked List
  - It can be used instead of Array. Node is made of the data and link. Data contains key value, and link contains the adress of the next node. At the end of the list, there is a node called None, which means there are no more nodes connected to the node, and it is the last end of the node. The first node of the list is called head, and the node before the None, last node with value, is called tail.
  
- Doubly Linked List
  - It covers the problem of deleting a node. Since singly Linked list needs to know the previous node of target to redirect the links of nodes. Doubly Linked List helps with deleting a node, or several nodes connected to each other, from a original list without searching for the previous node. But it doubles in the number of nodes to redirect. It may be complicated, but is worth doing because there are so much to earn by it.
  - Circular doubly linked list is a model form of doubly linked list.
  
- LAB :
  - singly_linked_list.py : Write a Node class, and SinglyLinkedList class. SinglyLinkedList class supports pushFront, pushBack, popFront, popBack, search, remove and printList functions. It is an interactive program, which will get an input line from user (ex : pushFront 10), and will push 10 to a list defined in the code. All input should be in a form of "command (space) number" or "command".
  - doubly_linked_list.py : It works in a same way with singly_linked_list.py but with few functional changes. This code provides splice, moveAfter, moveBefore, InsertAfter, InsertBefore, pushFront, pushBack, deleteNode, popFront, popBack, search, first, last, isEmpty and printList functions. Input command must be in a form of "command (space) number" or "command" like singly_linked_list.py.
  - josephus.py : Make a code for josephus game using doubly_linked_list.
  
## 04. Hash Table
- Hash table works like a dictionary. Map a key to a index with a hash function. If a slot is full with other item, collision occurs. To solve the collision and insert the value to a slot, we use Collision Resolution Method. 
- There are 3 different points to keep in mind to make the Hash table to work efficiently. 
  - Table is controlled with a list.
  - Hash function - How to insert a key, determining f(key).
  - Collision resolution methtod - How to solve a collision if occured.
  
- LAB :
  - linear_probing.py : Defining a class of Hash Table that works in open addressing way. Also known as linear probing, they both work in same way, filling the underneath of slot that is already filled. 
  - find_sum.py : find a total number of pairs that sums up to k from a given list n. Used a class defined in linear_probing.py, with a few change applied.
  
## 05. Heap
- Heap works in a way of tree structure. It needs to satisfy couple conditions to be a heap structure. 
  - All of parent node contains a key value that is not smaller than it's child node. 
  - The formation of tree needs to be in complete binary tree. 
  
- LAB :
  - stream_of_median.py : Make a list of given integers and calculate a median of given variable k. Medians are stored as a list, and none of sorting algoritms, quick select, MOM structures can be used. Used two heaps to solve the problem. It adds all the medians stored in a list and returns the summation of it.

## 06. Tree
- Traversal
  - When you want to visit all of the node in binary tree, you go in traversal way. There are three common ways : preorder, inorder, postorder.
  - Pre-order : Middle node is the first to visit, then left subtree nodes then finally right subtree nodes are to visit.
  - In-order :  Left subtree is the first to visit and after its traversal, middle node, then lastly right subtree is visited for traversal.
  - Post-order : Left subtree is the first to visit, and right subtree nodes are visited, then the middle node is visited. <br>
  
 ![binaryTree](https://user-images.githubusercontent.com/42270720/120263392-8ed44d00-c2d6-11eb-8311-42488e3f2c94.jpg)
 
  - Looking at the binary tree from the picture above, the orders are as following.
    - Pre-order : 7-3-1-0-2-6-4-13-11-8-15-21
    - In-order : 0-1-2-3-4-6-7-8-11-13-15-21
    - Post-order : 0-2-1-4-6-3-8-11-21-15-13-7
  
- LAB : 
  - play_with_BST : Make a code that works for all traversals (preorder, inorder, postorder traversals) with several additional functions.
  
## 07. Balanced Binary Search Tree
- If one subtree of the binary tree is bigger than the other subtree, balance both sides by using 'rotation'.
- There are left rotation and right rotation, and they are symmetrical. 
- After the rotation, the Binary Search Tree nodes' order must be the same.
- AVL Tree, Red-Black tree, and Splay Tree are representing examples.

## 08. Graph
- When two nodes have a relationship between each other nodes, the edge connects each other.
- Linked list is one of the most simple form of the graph.
- V stands for vertex or node, and E stands for edge. <br>

![graph](https://user-images.githubusercontent.com/42270720/120265485-22a81800-c2db-11eb-9b54-37af5fc75532.jpg)

- For example, if we define a graph above, G = (V, E). 
- G => V = {1, 2, 3, 4, 5, 6}, E = { (1, 2), (3, 2), (1, 5), (2, 5), (4, 5), (6, 4), (3, 4)}

- Graph Representation
  - Adjacency matrix : If any edge exists in between node i and j, G\[i]\[j] = 1, else 0.
  - Adjacency list : If any edge exists in between nodes, they are shown as linked list. 

| Basic Operations | Adjacency matrix | Big-O | Adjacency list | Big-O |
|:---:|:---:|:---:|:---:|:---:|
| Is (u, v) edge? | G\[u]\[v] == 1 | O(1) | G\[u].search(v) != None | O(V)|
| For all adjacent edge of u, (u, v) | G\[u]\[v] for v in range(n) | O(V) | for edge in G\[u] | O(deg(u))/O(out-deg(u)) |
| Insert new edge (u, v) | G\[u]\[v] <- 1 | O(1) | G\[u].pushFront(v) | O(1) |
| Delete edge (u, v) | G\[u]\[v] <- 0 | O(1) | x <- G\[u].search(v), G\[u].remove(x) | O(deg(u))/O(out-deg(u)) |
| Memory for G || O(V^2) || O(E)|

