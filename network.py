# CS310 Assignment 4
# Name: Arata Katayama
# Date: Dec 8th 2022
# Collaboration Declaration: assistance received from classmates and professor
import sys
from collections import defaultdict, deque
from heap import heap

def broadcast(src, graph, ttl):  # DFS
    res = defaultdict(dict)
    # keeping track of ttl using dictionary
    _ttl = defaultdict(dict)
    _ttl[src] = ttl
    # initialize deque with src
    s = deque([src])

    while len(s)!=0:
        par = s.pop()
        if _ttl[par] != 0:
            for dest in graph[par].keys():
                # if the neighbor is already included in the stack then skip interation
                if dest not in res.keys():
                    s.append(dest)
                    res[dest] = par  # update result
                    _ttl[dest] = _ttl[par]-1  # update ttl
    return res

def direct(src, graph):
    # initialize heap using all the nodes and cost as inf
    node = []
    cost = []
    res = defaultdict(dict)
    for n in graph.keys():
        node.append(n)
        if n == src:
            cost.append(0)
        else:
            cost.append(float('inf'))

    # creating heap object
    q = heap(node, cost)
    while not q.is_empty():
        u = q.pop()
        # u is a tuple (cost, node)
        for w in graph[u[1]].keys():
            c = u[0] + graph[u[1]][w]  # getting the cost from src to dest
            if c < q.prio(w):
                q.decrease_key(w, c)
                res[w] = u[1]
    return res

def mst(src, graph):
    # Prims to find MST -> already has a path
    node = []
    cost = []
    res = defaultdict(dict)
    for n in graph.keys():
        node.append(n)
        if n == src:
            cost.append(0)
        else:
            cost.append(float('inf'))

    q = heap(node, cost)
    while not q.is_empty():
        u = q.pop()[1]
        for w in graph[u].keys():
            c = graph[u][w]  # getting the relative cost from parent to destination
            if c < q.prio(w):
                q.decrease_key(w, c)
                res[w] = u
    return res

def print_paths(graph, prev, msg, src):
    for v in graph.keys():
        if v == src:
            continue
        if not v in prev:
            print("Could not find path to", v)
            continue
        path = v
        cost = 0
        u = v
        while u != src:
            past = u
            u = prev[u]
            cost += graph[u][past]
            path = u + " " + path
        print(v, "received", msg, "along path", path, "with cost", cost)

if __name__ == "__main__":
    graph = defaultdict(dict)

    infile = open(sys.argv[1], "r")

    for line in infile:
        data = line.split(" ")
        start = data[0]
        end = data[1]
        cost = int(data[2])

        graph[start][end] = cost
        graph[end][start] = cost

    cmd = input()
    while cmd != "exit":
        print("Command:", cmd)
        method, msg, src = cmd.split(" ")[:3]
        prev = None
        if method == "broadcast":
            ttl = int(cmd.split(" ")[-1])
            prev = broadcast(src, graph, ttl)
        elif method == "direct":
            prev = direct(src, graph)
        elif method == "MST":
            prev = mst(src, graph)
        else:
            print("Invalid command!")
        if prev != None:
            print_paths(graph, prev, msg, src)
        cmd = input()
    print("Goodbye!")
