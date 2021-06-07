#!/usr/bin/python3

#
# netstat2graphviz.py
#
# Drawing a graph according to the output of netstat.
# (*) netstat edited data are required.
#
# [netstat edited data](input)
#   protocol,sourceip:sourceport,destip:destport
# 
# InputSample
#  tcp,10.0.0.1:514,10.0.0.2:10023
#  tcp,0.0.0.0:514,*:*
#  udp,10.0.0.1:10001,10.0.0.3:514
#
# [inet-henge formated json data](output)
#  output.png
#
# [Pre-requirement]
# 1. pip install graphviz
# 2. Install Graphviz for displaying.
#    See here for more detailed.
#    https://graphviz.org/download/
# 
# [Warning]
# IP of * or 0.0.0.0(listed in exclideips)are ignored.
# 

import sys
import json
from graphviz import Digraph

if len(sys.argv)!=2:
  print("Usage: inputFile")
  sys.exit(0)

excludeips=["*","0.0.0.0"]
fp=sys.argv[1]
nodes=[]
edges=[]
edge_labels=[]

with open(fp,"r") as f:
  for line in f.readlines():
    line=line.strip()
    sps=line.split(",")
    proto=sps[0]
    (si,sp)=sps[1].split(":")
    (di,dp)=sps[2].split(":")

    isExclude=True
    if si not in excludeips:
      nodes.append(si)
      isExclude=False
    if di not in excludeips:
      nodes.append(di)
      isExclude=False

    # If not numeric, link is not created.
    if not isExclude and ( sp=="HIGH" or sp.isnumeric() ) and ( dp=="HIGH" or dp.isnumeric()):
      # sp is normally destination port.
      if dp=="HIGH" or int(sp)<int(dp):
        edges.append([di,si])
        edge_labels.append(proto+"/"+sp)
      else:
        edges.append([si,di])
        edge_labels.append(proto+"/"+dp)

nodes = sorted(list(set(nodes)))

dg = Digraph(format='png')
# Add nodes
for node in nodes:
  dg.node(node)
# Add edges
alreadyAdded=[]
for i in range(0,len(edges)):
  checkstr = "+".join([edges[i][0],edges[i][1],edge_labels[i]])
  if checkstr in alreadyAdded:
    continue
  alreadyAdded.append(checkstr)
  dg.edge(edges[i][0],edges[i][1],edge_labels[i])
dg.view()

#output = {}
#output["nodes"]=[]
#output["links"]=[]
#for node in nodes:
#  output["nodes"].append({"name":node,"icon":"./images/router.png"})
#for sip in links.keys():
#  for dip in links[sip]:
#    output["links"].append({"source":sip,"target":dip})
#print(json.dumps(output,indent=4))
