# Assignment 2
- Download a road network of the Porto City, Portugal and download some trajectory data of taxies in the city from a Kaggle competition.

- Visualize the raw GPS points of the first 10 trips in the trajectory data dataset on a map with the road network of Porto (together with different colors or separately).

- Perform the map matching task to map the trajectory data to the road network using an
existing open-source tool. Each trajectory will be mapped to a sequence of road segments and we call a sequence of road segments a route.

- Visualize the routes that are mapped from the trajectories of the first 10 trips on the road
network (together with different colors or separately).

- Perform some analysis on the mapped routes. This includes (1) to return 5 road segments that are traversed the most often as indicated by the trajectory data; (2) to return 5 road
segments, whose average travelling time as indicated by the trajectory data are the largest (those road segments that are traversed by no trajectories can be ignored); and (3) and visualize the
road segments returned in (1) and (2) on the road network separately.

- (bonus and optional). If possible, identify those cases where the map matching algorithm do not work well, think of some solutions for the identified cases and implement the new ideas into the open source tools and perform the map matching task on the trajectory data again and compare the mapped routes before and after the changes are made.

# Dataset
- Road network data (https://www.openstreetmap.org/). Some Python code that can be used for downloading road network from OpenStreetMap can be found here: https://github.com/cyang-kth/fmm/blob/master/example/osmnx_example/download_network.ipynb
- The trajectory data can be downloaded from Kaggle (https://www.kaggle.com/c/pkdd-15-predict-taxi-service-trajectory-i/data)

# Members
- Brandon Chua Shaojie
- Chang Fuh Yong
- Cheong Kok Yuet
