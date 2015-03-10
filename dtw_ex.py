import numpy as np
import matplotlib.pyplot as plt
import dtw

#this is a naive dtw, meaning it'll be O(n^2)
#having that power law matching means that there will be one degree neighborhood with O(n) length
#easy check: don't even check if it's >1.2x length or <0.8 length, something like that

if __name__ == "__main__":
    x = [0,0,1,1,2,4,2,1,2,0]
    y = [1,1,1,2,2,2,2,3,2,0]
    dist, cost, path = dtw.dtw(x, y)
    print "dist: ", dist
    print "cost: ", cost
    print "path: ", path
