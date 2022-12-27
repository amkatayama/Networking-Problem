# Networking-Problem

## Problem 

Consider a problem that online game designers and Internet radio providers face: How can you efficiently transfer a piece of information to everyone who may be listening. This is important in real-time gaming so that all the players know the very latest position of every other player; this is important
for Internet radio so that all the listeners that are tuned in are getting all the data they need to reconstruct the song they are listening to.

## Approach 

### Broadcast 

Broadcast performs a network-flooding to ensure that the intended destination receives the packet successfully. This approach does the job of sending packets from sender to destination, however it is extremely inefficient as it is sending it to hosts which was not registered as the destination. In my implementation of broadcast I am keeping track of TTL. Keeping track of TTL is important because by giving a finite possible hop amount for each packet, we can prevent it from looping inside the network. TTL decreases every time it reaches a host, and when it reaches 0, this means that the packet can no longer be sent forwards. 

### Djikstra's Algorithm

Djikstra's algorithm finds the lowest cost path from the sender to destination, by looking through the neighbor nodes and recording the total cost from the origin to the current node. Djikstra's algorithm is a greedy optimal algorothm, because it gets the most optimal solution at a given condition. 

### Prim's Algorithm 
The only difference between Djikstra's algorithm and Prim's algorithm is that Prim's algorithm only keeps track of the current cost from the parent node to the current node, rather than the total cost from the origin to the current node. Prim's algorithm is also a greedy optimal algorithm, and this is often used to create a minimal spanning tree, A.K.A. MST. 
