import networkx as nx
import operator
import collections
import hashlib
import matplotlib.pyplot as plt

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
    """
    Stick them together, right? right? ... that's a joke
    """
    return ",".join(map(str,sorted(ls)))

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

def plot_deg_neighborhood_sum(deg_n):
    deg_n_sums = sorted([sum(x[1]) for x in deg_n.items()], reverse=True)
    plt.loglog(deg_n_sums)
    plt.show()

if __name__ == "__main__":
    net1 = nx.barabasi_albert_graph(6000,15)
    #net2 = reverse_node_labels(net1)
    net2 = nx.barabasi_albert_graph(6000,15)
    deg1 = degrees(net1)
    deg2 = degrees(net2)
    deg_n1 = degree_neighborhoods(net1, deg1)
    deg_n2 = degree_neighborhoods(net2, deg2)
    #sum maybe not
    deg_n1_sums = sorted([sum(x[1]) for x in deg_n1.items()], reverse=True)
    deg_n2_sums = sorted([sum(x[1]) for x in deg_n2.items()], reverse=True)
    deg_n1s = [x[0] for x in sorted(deg_n1.items(), key=lambda x: stick(x[1]))]
    deg_n2s = [x[0] for x in sorted(deg_n2.items(), key=lambda x: stick(x[1]))]
    print zip(deg_n1s, deg_n2s)
