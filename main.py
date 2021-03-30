import random
import numpy as np
import math

def random_gen(num_node, num_edge):
    num_node = int(num_node)
    num_edge = int(num_edge)
    src = [None] * num_node
    dst = [None] * num_node
    for index, _ in enumerate(range(num_edge)):
        src[index] = random.randint(0, num_node)
        dst[index] = random.randint(0, num_node)
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

    src = [None] * num_edge
    dst = [None] * num_edge

    for index, _ in enumerate(range(num_edge)):
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
        src[index] = x
        dst[index] = y
    return src, dst

