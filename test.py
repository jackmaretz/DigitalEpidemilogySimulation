import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
n = 100  # Number of nodes
m = 1  # Number of initial links
seed = 100
G = nx.barabasi_albert_graph(n, m, seed)

ncols = 10
pos = {i : (i % ncols, (n-i-1) // ncols) for i in G.nodes()}
nx.draw(G, pos, with_labels=True)
plt.show()
#$#############################
# degree_sequence=sorted(nx.degree(G).values(),reverse=True) # degree sequence
# #print "Degree sequence", degree_sequence
# dmax=max(degree_sequence)
#
# plt.loglog(degree_sequence,'b-',marker='o')
# plt.title("Degree rank plot")
# plt.ylabel("degree")
# plt.xlabel("rank")
#
# # draw graph in inset
# plt.axes([0.45,0.45,0.45,0.45])
# Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
# pos=nx.spring_layout(Gcc)
# plt.axis('off')
# nx.draw_networkx_nodes(Gcc,pos,node_size=20)
# nx.draw_networkx_edges(Gcc,pos,alpha=0.4)
#
# plt.savefig("degree_histogram.png")
# plt.show()
#########################
# pos=nx.spring_layout(G)
# colors=range(20)
# nx.draw(G,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)
# plt.savefig("edge_colormap.png") # save as png
# plt.show() # display
# ###########################
# import collections
#
#
# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# # print "Degree sequence", degree_sequence
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
#
# fig, ax = plt.subplots()
# plt.bar(deg, cnt, width=0.80, color='b')
#
# plt.title("Degree Histogram")
# plt.ylabel("Count")
# plt.xlabel("Degree")
# ax.set_xticks([d + 0.4 for d in deg])
# ax.set_xticklabels(deg)
#
# # draw graph in inset
# plt.axes([0.4, 0.4, 0.5, 0.5])
# Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
# pos = nx.spring_layout(G)
# plt.axis('off')
# nx.draw_networkx_nodes(G, pos, node_size=20)
# nx.draw_networkx_edges(G, pos, alpha=0.4)
#
# plt.show()