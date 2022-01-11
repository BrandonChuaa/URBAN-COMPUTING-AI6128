import os
import csv
from fmm import FastMapMatch,Network,NetworkGraph,UBODTGenAlgorithm,UBODT,FastMapMatchConfig
from fmm import Network,NetworkGraph,STMATCH,STMATCHConfig

network = Network("./data/portoNetCity/edges.shp","fid", "u", "v")
print "Nodes {} edges {}".format(network.get_node_count(),network.get_edge_count())
graph = NetworkGraph(network)

## Precompute an UBODT table

# Can be skipped if you already generated an ubodt file
ubodt_gen = UBODTGenAlgorithm(network,graph)
status = ubodt_gen.generate_ubodt("./data/portoNetCity/ubodt.txt", 0.02, binary=False, use_omp=True)      ###threshold of 2km
print status

### Read UBODT
ubodt = UBODT.read_ubodt_csv("./data/portoNetCity/ubodt.txt")
### Create FMM model
model = FastMapMatch(network,graph,ubodt)

### Define map matching configurations
k = 8
radius = 0.003   ### search radius 
gps_error = 0.0005  ##gps error 
fmm_config = FastMapMatchConfig(k,radius,gps_error)

train1000 = []
ignoreFirst = 0 #ignore first line since its POLYLINE

with open("./data/train_1000.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    
    for line in reader:
        if ignoreFirst == 0:
            ignoreFirst = 1
        else:
            train1000.append(line[8])

mapMatched = []

for index in range(len(train1000)):
    gps = eval(train1000[index])
    wkt = 'LINESTRING('+','.join([' '.join([str(j) for j in i]) for i in gps])+')'
    output = model.match_wkt(wkt, fmm_config)
    
    candidates = list(output.candidates)

    mapMatched.append(dict(cpath=str(list(output.cpath)), mgeom=output.mgeom.export_wkt(), opath=str(list(output.opath)),
    offset=str([c.offset for c in candidates]), length=str([c.length for c in candidates]),spdist=str([c.spdist for c in candidates])))

# cpath, opath, offset, length, spdist, mgeom
with open("./data/matchedMaps.csv","w") as csvfile:
    w = csv.writer(csvfile)
    w.writerow(["Index", "cpath", "opath", "offset", "length", "spdist", "mgeom"])

    entry = []

    for index in range(len(train1000)):
        pointer = mapMatched[index]
        entry.append([index+1, pointer['cpath'], pointer['opath'], pointer['offset'], pointer['length'], pointer['spdist'], pointer['mgeom']])
    w.writerows(entry)


