import networkx as nx
from networkx.algorithms import isomorphism as iso


hex_string = input()
binary_string = bin(int(hex_string,16))[2:]
binary_string_appender=['1']*128
print(binary_string)

for i in range(len(binary_string)):
    add=''
    for k in bin(i+128)[3:]:
        if(k=='1'):
            add+='0'
        else:
            add+='1'
    print(add)        
    binary_string_appender[int(add,2)]='0'
print(binary_string_appender)    
binary_string+=''.join(binary_string_appender)                

print(binary_string)

G = nx.Graph()
for i in range(len(binary_string)):
    for j in range(len(binary_string)):
        count = 0  
        flag = 0
        if (binary_string[i]=='1' or binary_string[j]=='1'):
            flag+=1      
        for k in range(3,10):
            if ((bin(i+256)[k] == "1") and (bin(j+256)[k]=="0")):
                flag+=1
            if ((bin(i+256)[k] == "0") and (bin(j+256)[k]=="1")):
                count+=1

        if(3 > count > 0 and flag == 0):
            G.add_edge(i+256,j+256)
            G.add_edge(i,j)
            print(i,j)
            print(i+256,j+256)
        if(2 > count >= 0 and flag == 0):
            G.add_edge(i,j+256)
            print(i,j+256)
P = nx.Graph()
for i in range(87):
    P.add_edge(i,i+1)
P = nx.path_graph(86)
exit()
gm = iso.GraphMatcher(G, P)
generator_of_paths = gm.subgraph_isomorphisms_iter()



path1 = next(generator_of_paths)
new_list = [bin(i+512)[3:11] for i in path1]
print([i for i in path1])
print(new_list)