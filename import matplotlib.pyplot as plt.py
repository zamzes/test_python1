import matplotlib.pyplot as plt
from mayavi import mlab
import numpy as np
import pandas as pd
    
    
pos = [[0.1, 2, 0.3], [40, 0.5, -10],
       [0.1, -40, 0.3], [-49, 0.1, 2],
       [10.3, 0.3, 0.4], [-109, 0.3, 0.4]]
pos = pd.DataFrame(pos, columns=['x', 'y', 'z'])
    
ed_ls = [(x, y) for x, y in zip(range(0, 5), range(1, 6))]
    
G = nx.Graph()
G.add_edges_from(ed_ls)
remove = [node for node, degree in dict(G.degree()).items() if degree < 2]
G.remove_nodes_from(remove)
pos.drop(pos.index[remove], inplace=True)

print(G.edges)
    
nx.draw(G)
plt.show()
    
mlab.figure(1, bgcolor=bgcolor)
mlab.clf()
    
for i, e in enumerate(G.edges()):
    
# ----------------------------------------------------------------------------
    # the x,y, and z co-ordinates are here
    pts = mlab.points3d(pos['x'], pos['y'], pos['z'],
                        scale_mode='none',
                        scale_factor=1)
# ----------------------------------------------------------------------------
    pts.mlab_source.dataset.lines = np.array(G.edges())
    tube = mlab.pipeline.tube(pts, tube_radius=edge_size)
    
    mlab.pipeline.surface(tube, color=edge_color)
    
mlab.show()  # interactive window