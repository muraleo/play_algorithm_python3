# -*- coding: utf-8 -*-
import re
from DenseGraph import *
from SparseGraph import * 

# New read graph function
def ReadGraph(aGraph,filePath):
    graphList=[]
    with open(filePath,'r') as f:
        for line in f:
            graphList.append([int(x) for x in re.split(r'\s+',line.strip())])
    for i in range(len(graphList)):
        aGraph.addEdge(graphList[i][0],graphList[i][1])