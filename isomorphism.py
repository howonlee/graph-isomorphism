import networkx as nx
import operator
import collections
import hashlib

def degrees(net):
    degree_dict = {}
    for node in net.nodes_iter():
        degree_dict[node] = net.degree(node)
    return degree_dict

def degree_neighborhoods(net, degree_dict):
    neighbor_dict = {}
    #really need a better sort of distance, I think
    #not distance measures actually
    for node in net.nodes_iter():
        neighbor_dict[node] = []
        for neigh in net.neighbors_iter(node):
            neighbor_dict[node].append(degree_dict[neigh])
        neighbor_dict[node].sort() #mutating sort
        #neighbor_dict[node] = len(neighbor_dict[node])
    return neighbor_dict

def stick(ls):
    return ",".join(map(str,ls))

def hash_degn(deg_n):
    """
    Check that a model doesn't fuck us over here
    """
    hashes = []
    m = hashlib.md5()
    for _, val in deg_n.iteritems():
        m.update(stick(val))
        hashes.append(m.digest())
    col = collections.Counter(hashes)
    for key, val in col.most_common():
        if val > 1:
            print "what the fuck"

def reverse_node_labels(net1):
    net2 = nx.Graph()
    len_nodes = len(net1.nodes())
    net2.add_nodes_from(range(len_nodes))
    for node_a, node_b in net1.edges_iter():
        net2.add_edge(len_nodes - 1 - node_a, len_nodes - 1 - node_b)
    return net2

if __name__ == "__main__":
    net1 = nx.barabasi_albert_graph(6000,15)
    net2 = reverse_node_labels(net1)
    deg = degrees(net2)
    deg_n = degree_neighborhoods(net2, deg)
