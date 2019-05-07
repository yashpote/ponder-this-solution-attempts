import networkx as nx
from networkx.algorithms import isomorphism as iso

G = nx.Graph()
edges = 0
for i in range(512):
    for j in range(512):
        count = 0  
        flag = 0      
        for k in range(3,11):
            if ((bin(i//2+256)[k] == "1") and (bin(j//2+256)[k]=="0")):
                flag+=1
            if ((bin(i//2+256)[k] == "0") and (bin(j//2+256)[k]=="1")):
                count+=1

        if( i%2 == 0 and bin(i//2+256)[3:11].count('1') == 0 and j%2 == 1 and bin(j//2+256)[3:11].count('1')  == 1):
            flag+=1

        if(3 > count > 0 and flag == 0 and i%2 == 0 and j%2 == 1):
            G.add_edge(i,j)
            edges+=1
            # print(i,j)

len_path = 92
P = nx.path_graph(len_path)

for i in range(len_path-1):
    P.add_node(i, end = "no")
P.add_node(len_path-1, end='yes')

for i in range(511):
    G.add_node(i, end = "no")
G.add_node(511, end='yes')

def match(x,y):
    return x['end'] == y['end']

gm = iso.GraphMatcher(G, P, node_match=match)

genpath = gm.subgraph_isomorphisms_iter()

path1 = next(genpath)
new_list = [bin(i+512)[3:11] for i in path1]
print([bin(i+512)[3:11].count('1') for i in path1])
print([bin(i+512)[3:11] for i in path1])
