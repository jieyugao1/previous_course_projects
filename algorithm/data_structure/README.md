# Data Structure

## Elementary Data Structures

### Stacks

The stack implements a last-in, first-out or LIFO policy. 

The insert operation on a stack is often called **PUSH**, and the delete operation is often called **POP**. 

**Steps**:
    
    1. Implement a stack of at most n elements wiht an array S[1,...,n]
    2. The array has an attribute S.top that indexes the most recently inserted element. The stack consists of elements S[1,...,S.top]
    3. WHen S.top = 0, the stack contains no element and is empty. If we attemp to pop an empty stack, we say the stack **underflows*, which is normally an error. If S.top exceeds n, the stack **overflows**.

### Queues

In a queue, the element deleted is always the one that has been in the set for the longest time. The queue implements a first-in, first-out or FIFO policy. 

**Steps**:
    
    1. Implement a queue of at most n-1 elements using an array Q[1,...,n]
    2. The queue has an attribute Q.head that indexes or points to its head.
    3. The queue has an attribute Q.tail indexes at the next location at which a newly arriving element will be inserted into the queue. 
    4. The elements in teh queue reside in locations Q.head, Q.head+1, ..., Q.tail-1, where we wrap around in the sense that location 1 immdediately follows location n in a circular order. 
    5. When Q.tail = Q.head, the queue is empty. Initially, we have Q.head =Q.tail = 1. If we attemp to dequeue an element from an empty queue, the queue underflows. When Q.head = Q.tail+1, the queue is full. If we attemp to enqueue an element, then the queue overflows. 

### Linked List

A linked list is a data structure in which the objects are arranged in an linear oder. (search takes O(n) time; insert and delete takes O(1) time. Note that for the delete case, if we need to find the keys fo the item instead of the object itself, need to do search first, which takes linear time).

Normally there are two types of linked list, **doubly linked list** and **singly linked list**, in which the latter omit the prev pointer in each elemnet. 

## Hash Tables

A hash table is an effective data structure for implementing dictionaries. Under reasonable assumptions, the average time to search fro an element in a hash table is O(1).

### Direct-address tables

This is a simple technique that works well when the universe U of keys is reasonale small. T[x.key] =x. Each of the operations, including search, insert and delete takes O(1) time. 

If U is large, storing a table T of size |U| may be impractical or impossible. 

### Hash Tables

WHen the set K of keys sotred in a dictionary is much smaller than the universe U of all possible keys, a hash table requires much less storage than a direct address table. We cna reduce the storage requirment to O(|K|) while we maintain the benefit that searching for an element in the hash table still requires only O(1) time. This bound is for average-case time. Direct addressing holds for worst-case time. 

While direct addressing, an element with key k is stored in slot k. With hashing, this element is stored in slot h(k). We use a **hash function** h to compute the slot from the key k. Hence, h maps the universe U into the slot of a hash table T[0,...,m-1]

```math
    h: U \rightarrow \{0, 1, ..., m-1\}
```
where the size m of the hash table is typically much less than |U|. 

We say that an element with key k hashes to slot h(k). h(k) is the **hash value** of key k. 

If two or multiple keys hash to the same slot, we call this situation a **collision**. 

#### Collision Solutions:
    
##### Solution 1 Chaining 

In chaining, we place all the elements that has to the same slot into the same linked list. 

The worst-case running time for **insertion** is O(1). For searching, the worst-case running time is proportional to the length of the list. We can delete the element in O(1) time if doubly linked. If the list is singly linked, we need to search for x in the list T[(x.key)] to update the next attribute of x's predecessor, which takes O(n) time. 

The worst case behaviro of hashing with chaining is terrible: all n keys hash to the same slot, creating a length n. 

The average case performance of hashing depends on how well the hash function h distributes the keys to be stored among the m slots, on the average. 

**Simple Uniform hashing assumption**: any given element is equally likely to hash into any of the m slots, independently of where any other element has hashed to. 

for j = 0, 1, ..., m-1, let us denote the lenght of T[j] by n_j, so that n = n_0 + n_1 + ... + n_(m-1), and the expected value of n_j is alpha = n/m.

Search takes average-case time O(1+alpha) under the simple uniform hashing assumption. 

If the number of hash-tale slots is at least proportional to the number of elements in the table, alpha = 1. Thus searching takes constant time on average. We can support all dictionary operations in O(1) time on average. 

#### Hash Functions


