import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D # 3D display
import pickle 
import pyvista as pv
from geomdl import BSpline, operations


from ArterialTree import ArterialTree
from Simulation import Simulation
from Editor import Editor

import pyvista as pv


# Import centerline data to create an ArterialTree object
##centerline = "../../Data/Aneurisk/C0097/centerline/centerline.vtp"
##tree = ArterialTree("Test", "Aneurisk", centerline)

###Open a ArterialTree object in .obj format

f = open(r"../../C0083.obj",'rb')
tree = pickle.load(f)
tree.model_network()



###### MESHING WITHOUT GUI #########

#tree.low_sample(0.1) # Low sampling points to model faster (only if we have a lot of data points)
'''tree.show(True, False, False)
	
tree.model_network()  # Parametric modeling of the network
tree.show(False, True, False)

tree.compute_cross_sections(24, 0.2, False) # Mesh cross sections

	
surface_mesh = tree.mesh_surface() # Mesh surface
surface_mesh.plot(show_edges=True)
surface_mesh.save("Output/mesh/surface_mesh.vtk")

volume_mesh = tree.mesh_volume([0.2, 0.3, 0.5], 10, 10) # Mesh volume
volume_mesh.plot(show_edges=True)
volume_mesh.save("Output/mesh/volume_mesh.vtk")

target_surface_mesh = pv.read("../../Data/Example/example_surface_mesh.stl") # Deform mesh to target surface
target_surface_mesh.plot()

tree.deform_surface_to_mesh(target_surface_mesh)
volume_mesh_deformed = tree.mesh_volume([0.2, 0.3, 0.5], 10, 10)
volume_mesh_deformed.plot(show_edges = True)
volume_mesh_deformed.save("Output/mesh/volume_mesh_deformed.vtk")

'''

###### MESHING WITH GUI #########
# Open the editor
e = Editor(tree, 1500, 600)

###### WRITE OPENFOAM FILES #########
simu = Simulation(tree, "Output/openFoam")
simu.write_mesh_files()






