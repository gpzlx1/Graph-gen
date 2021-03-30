import math
import random
import numpy as np
from tqdm import tqdm

def random_gen(num_node, num_edge):
    num_node = int(num_node)
    num_edge = int(num_edge)
    src = []
    dst = []
    edges = set()
    for _ in tqdm(range(num_edge)):
        x = random.randint(0, num_node)
        y = random.randint(0, num_node)
        if (x, y) in edges:
            continue
        edges.add((x,y))
        src.append(x)
        dst.append(y)
    return src, dst

#Kronecker Prob kernel KPK = []
#num_node must be 2^m
def kronecker_gen(num_node, num_edge, prob_kernel = [0.99, 0.54, 0.49, 0.13]):
    num_node = int(num_node)
    num_edge = int(num_edge)
    pre_sum_prob_kernel = [0]

    for index, prob in enumerate(prob_kernel):
        pre_sum_prob_kernel.append(pre_sum_prob_kernel[index] + prob)
    pre_sum_prob_kernel = [ i / np.sum(prob_kernel) for i in pre_sum_prob_kernel]

    num_node = math.ceil(math.log2(num_node)) ** 2
    M = int(math.log2(num_node))

    src = []
    dst = []
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
            continue
        edges.add((x,y))
        src.append(x)
        dst.append(y)
    return src, dst

a, b = kronecker_gen(1000, 1000)
print(len(a))
print(len(b))