''''

It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. 
While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use `collections.deque` which was designed to have fast appends and pops from both ends.

ref:: collections.deque - https://docs.python.org/3/library/collections.html#collections.deque
'''

from collections import deque

queue = deque(['mike', 'kavin', 'layling', 'jenny'])

# with append()
queue.append('scarry') # scarry arrives
print(queue)
queue.append('jim') # jim arrives
print(queue)

# popleft()
queue.popleft() # The first('mike') to arrive now leaves
print(queue) # Remaining queue in order of arrival
queue.popleft() # 'kavin' is gone
print(queue)


# with appendleft()
queue.appendleft('john') # insert('john') from the begining of the list
print(queue)


# with pop()
queue.pop() # retrieve last element('jim') of the list
print(queue) # 'jim' has gone
