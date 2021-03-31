import math
import random
import numpy as np
from tqdm import tqdm
import queue

def random_gen(num_node, num_edge):
    num_node = int(num_node)
    num_edge = int(num_edge)
    edges = set()
    for _ in tqdm(range(num_edge)):
        x = random.randint(0, num_node)
        y = random.randint(0, num_node)
        if (x, y) in edges:
            continue
        edges.add((x,y))
    return edges

#Kronecker Prob kernel KPK = []
#num_node must be 2^m
def kronecker_gen(num_node, num_edge, prob_kernel = [0.99, 0.54, 0.49, 0.13]):
    num_node = int(num_node)
    num_edge = int(num_edge)
    pre_sum_prob_kernel = [0]

    for index, prob in enumerate(prob_kernel):
        pre_sum_prob_kernel.append(pre_sum_prob_kernel[index] + prob)
    pre_sum_prob_kernel = [ i / np.sum(prob_kernel) for i in pre_sum_prob_kernel]

    num_node = 2 ** math.ceil(math.log2(num_node))
    M = int(math.log2(num_node))

    edges = set()

    for _ in tqdm(range(num_edge)):
        x = 0
        y = 0
        for i in range(1, M+1):
            random_choice = random.uniform(0,1)
            base = 2 ** (M-i)
            if random_choice < pre_sum_prob_kernel[1]:
                x = x + 0 * base
                y = y + 0 * base
            elif random_choice < pre_sum_prob_kernel[2]:
                x = x + 0 * base
                y = y + 1 * base
            elif random_choice < pre_sum_prob_kernel[3]:
                x = x + 1 * base
                y = y + 0 * base
            else:
                x = x + 1 * base
                y = y + 1 * base
        if (x, y) in edges:
            #print(x,y)
            continue
        edges.add((x,y))
    return edges

def Gorder(edges, order = 'out'):      
    graph_dict = {}
    for src, dst in edges:

        if order == 'in':
            src, dst = dst, src

        if src in graph_dict:
            graph_dict[src].append(dst)
        else:
            graph_dict[src] = [dst]

    unvisited = [ i for i in graph_dict.keys() ]
    unvisited.sort(key=lambda x:len(graph_dict[x]), reverse=True)
    q = queue.Queue()
    visited = []

    for src in tqdm(unvisited):
        if src in visited:
            continue
        q.put(src)
        while not q.empty():
            src = q.get()
            if src in visited:
                continue
            visited.append(src)
            dsts = graph_dict.get(src, [])
            for dst in dsts:
                q.put(dst)

    map_dict = {}
    for index, src in enumerate(visited):
        map_dict[src] = index

    order_edges = set()
    for src, dst in edges:
        order_edges.add((map_dict.get(src, src), map_dict.get(dst, dst)))
    return order_edges