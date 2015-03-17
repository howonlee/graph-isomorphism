import numpy as np
import matplotlib.pyplot as plt
import dtw
import ast

#this is a naive dtw, meaning it'll be O(n^2)
#having that power law matching means that there will be one degree neighborhood with O(n) length
#easy check: don't even check if it's >1.2x length or <0.8 length, something like that

x_lists = {}
y_lists = {}

def cust_norm(x,y):
    global x_lists, y_lists
    x_list = x_lists[x[0]]
    y_list = y_lists[y[0]]
    dist = 0
    if len(x_list) > len(y_list):
        for idx, y in enumerate(y_list):
            dist -= y * x_list[idx]
    else:
        for idx, x in enumerate(x_list):
            dist -= x * y_list[idx]
    return dist

def lines_map(lines):
    global x_lists, y_lists
    curr_x_idx = 0
    curr_y_idx = 0
    l_x_map = {}
    l_y_map = {}
    for line in lines:
        if line[0][0] not in l_x_map:
            l_x_map[line[0][0]] = curr_x_idx
            x_lists[curr_x_idx] = line[0][1]
            curr_x_idx += 1
        if line[1][0] not in l_y_map:
            l_y_map[line[1][0]] = curr_y_idx
            y_lists[curr_y_idx] = line[1][1]
            curr_y_idx += 1
    inv_x = {v:k for k, v in l_x_map.iteritems()}
    inv_y = {v:k for k, v in l_y_map.iteritems()}
    return l_x_map, l_y_map, inv_x, inv_y

if __name__ == "__main__":
    with open("filtered_res", "r") as res_file:
        lines = res_file.readlines()
        lines_eval = map(ast.literal_eval, lines)
        l_x_map, l_y_map, inv_x, inv_y = lines_map(lines_eval)
        xs = []; ys = []
        for line in lines_eval:
            xs.append(l_x_map[line[0][0]])
            ys.append(l_y_map[line[1][0]])
        print xs
        print ys
        dist, cost, path = dtw.dtw(xs,ys,dist=cust_norm)
        print "dist: ", dist
        print "cost: ", cost
        print "path: ", path
        for member in path[0]:
            print inv_x[member]
