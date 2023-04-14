#%%
"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            return("The queue is empty.")
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        del self.queue[high_pri_index]
        return value

        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Add a new item to the queue
# Expected Result: Bob (Pri:6), Mark (Pri:4), Sal (Pri:2), May (Pri:3), Chad (Pri:5), Snape (Pri:1)
print("Test 1")
Queue = Priority_Queue()
#print(Queue)
Queue.enqueue("Bob",6)
Queue.enqueue("Mark",4)
Queue.enqueue("Sal",2)
Queue.enqueue("May",3)
Queue.enqueue("Chad",5)
Queue.enqueue("Snape",1)
print(Queue)

# Defect(s) Found: 
    #The Priority and Value was switched in the enqueue funcion, resulting in the values being saved in reverse. Fixed on line 49

print("=================")

# Test 2
# Scenario: Print the cue's values in their priority
# Expected Result: Bob, Chad, Mark, May, Sal, Snape
print("Test 2")
Queue = Priority_Queue()
#print(Queue)
Queue.enqueue("Bob",6)
Queue.enqueue("Mark",4)
Queue.enqueue("Sal",2)
Queue.enqueue("May",3)
Queue.enqueue("Chad",5)
Queue.enqueue("Snape",1)
#print(Queue)
for i in range(6):
    print(Queue.dequeue())

# Defect(s) Found: 
    #dequeue does not seem to remove the item returned from the list after retrieving it

print("=================")

# Test 3
# Scenario:  If there are more than one node with the highest priority, then the item closest to the front of the queue will be removed and its value returned.
# Expected Result: Bob, May, Chad, Mark, Sal, Snape
print("Test 3")
Queue = Priority_Queue()
#print(Queue)
Queue.enqueue("Bob",6)
Queue.enqueue("Mark",4)
Queue.enqueue("Sal",2)
Queue.enqueue("May",6)
Queue.enqueue("Chad",5)
Queue.enqueue("Snape",2)
#print(Queue)
for i in range(6):
    print(Queue.dequeue())


# Defect(s) Found: 
    #On line 66 the searcher was starting at the first item, working back.  That ment that it would overite an earlier value with the newer one later in the list, 
    #even if they had the same priority.  Changed it to require the new value to be greater in order to overite, since it will then save the first high value it finds.

print("=================")

# Test 4
# Scenario: If the queue is empty, then an error message will be displayed.
# Expected Result: An error message should be displayed
print("Test 4")
Queue = Priority_Queue()
#print(Queue)
print(Queue.dequeue())
# Defect(s) Found: 
    #The error message is printed seperate to the returned value, causing a "None" to folow each error message



# %%
