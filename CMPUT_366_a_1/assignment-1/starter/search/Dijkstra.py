import heapq
def dijkstra (start, goal, gridded_map):
    OPEN=[]
    CLOSED ={}
    expand=0
    heapq.heappush(OPEN, start)
    CLOSED[start.state_hash()] = start.get_g()
    while OPEN:
        node = heapq.heappop(OPEN)
        expand += 1
        if node == goal:
            return node.get_g(), expand
        children = gridded_map.successors(node)
        for child in children:
            if child.state_hash() not in CLOSED.keys():
                cost = child.get_g()
                heapq.heappush(OPEN, child)
                CLOSED[child.state_hash()]=cost
            if child.state_hash() in CLOSED.keys() and cost< CLOSED[child.state_hash()]:
                CLOSED[child.state_hash()]=cost
                heapq.heappush(OPEN, child)
    return -1, expand