from re import S
from search.algorithms import State
from search.map import Map
import heapq
def dijkstra (start, goal, gridded_map):
    OPEN=[]
    CLOSED ={}
    expand=0
    heapq.heappush(OPEN, [start.get_g(),start])
    CLOSED[start.state_hash()] = start
    while OPEN:
        node = heapq.heappop(OPEN)
        expand += 1
        if node[1] == goal:
            return node, expand
        for child in gridded_map.successors(node):
            if child.state_hash() not in CLOSED.keys():
                cost = child.get_g()
                heapq.heappush(OPEN, [child.get_g(), child])
                CLOSED[child.state_hash()] = cost
            if child.state_hash() in CLOSED.keys() and cost< CLOSED[child.state_hash()]:
                CLOSED[child.state_hash()].set_g(cost)
                heapq.heappush(OPEN, child)
    return -1, expand
