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

        if(3 > count > 0 and flag == 0 and i%2 == 0 and j%2 == 1):
            G.add_edge(i,j)
            edges+=1
            #print(count, bin(i//2+256), bin(j//2+256))

print(edges)

def similar(a,b,c,d):
    if ((a==b) and ( c==d)):
        return True

P = nx.Graph()
for i in range(87):
    P.add_edge(i,i+1)
P = nx.path_graph(86)

gm = iso.GraphMatcher(G, P)
generator_of_paths = gm.subgraph_isomorphisms_iter()



path1 = next(generator_of_paths)
new_list = [bin(i+512)[3:11] for i in path1]
print([i for i in path1])
print(new_list)