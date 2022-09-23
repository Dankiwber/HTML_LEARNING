import heapq
from json.encoder import INFINITY
def Bi_bs (start, goal, gridded_map):
    OPEN_forward=[]
    OPEN_backward=[]
    CLOSED_forward ={}
    CLOSED_backward ={}
    expand_forward=0
    expand_backward=0
    heapq.heappush(OPEN_forward, start)
    heapq.heappush(OPEN_backward, goal)
    CLOSED_forward[start.state_hash()] = start.get_g()
    CLOSED_backward[start.state_hash()] = goal.get_g()
    u = INFINITY
    while OPEN_forward and OPEN_backward:

        if u < OPEN_forward[0].get_g()+OPEN_backward[0].get_g():
            return u,expand_forward+expand_backward

        if OPEN_forward[0].get_g() < OPEN_backward[0].get_g():
            node = heapq.heappop(OPEN_forward)
            expand_forward+=1

            children = gridded_map.successors(node)
            for child in children:
                if child.state_hash() in CLOSED_forward.keys():
                    u = min(u, CLOSED_forward[child.state_hash()]+child.get_g())

                if child.state_hash() in CLOSED_forward.keys() and cost< CLOSED_forward[child.state_hash()]:
                    CLOSED_forward[child.state_hash()]=cost
                    heapq.heappush(OPEN_forward,child)

                if child.state_hash() not in CLOSED_forward.keys():
                    cost = child.get_g()
                    heapq.heappush(OPEN_forward, child)
                    CLOSED_forward[child.state_hash()]=cost
        else:
            node = heapq.heappop(OPEN_backward)
            expand_backward+=1

            children = gridded_map.successors(node)
            for child in children:

                if child.state_hash() in CLOSED_backward.keys():
                    u = min(u, CLOSED_backward[child.state_hash()]+child.get_g())

                if child.state_hash() in CLOSED_backward.keys() and cost< CLOSED_backward[child.state_hash()]:
                    CLOSED_backward[child.state_hash()]=cost
                    heapq.heappush(OPEN_backward,child)
                    
                if child.state_hash() not in CLOSED_backward.keys():
                    cost = child.get_g()
                    heapq.heappush(OPEN_backward, child)
                    CLOSED_backward[child.state_hash()]=cost
    return -1, u