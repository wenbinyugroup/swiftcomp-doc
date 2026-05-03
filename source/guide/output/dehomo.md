
In the outputs of dehomogenization, the primary local field such as the displacement field for elastic analysis or the temperature field for conduction analysis is reported at each node. However, other fields calculated based on gradients from the primary local field such as stresses and strains are usually more accurate if reported at Gaussian integration points. However, because nodal values are more convenient for postprocessing of the results, only nodal values are reported. If you need Gaussian values, please contact the author. 

The local 3D displacement results obtained through dehomogenization are stored in input file name.u. The values are listed for each node identified by its location as: 

node no $u _ { 1 }$ u2 u3 

where $u _ { i }$ are the local 3D displacements at this node. Note if analysis=2, the outputs in this file are the local temperature for each node instead. 

If analysis=3, 4, the outputs will be 

node no u1 u2 u3 $\phi ^ { * }$ 

with $\phi ^ { * }$ as the scaled electric potential. 

If analysis=5, 6, the outputs will be 

node no u1 u2 u3 φ∗ ψ∗ 

with $\psi ^ { * }$ as the scaled magnetic potential. 

The local 3D strain/stress results at nodes obtained through dehomogenization are stored in input file name.sn. These values are identified by its location as: 

y1 y2 y3 11 22 33 223 213 212 σ11 σ22 σ33 σ23 σ13 σ12 

where $\epsilon _ { i j }$ and $\sigma _ { i j }$ are the components of the local 3D strain tensor and 3D stress tensor, respectively, 

at the node. Note if analysis=2, the outputs in this file are instead the local temperature gradient and heat flux instead arranged as 

y1 y2 y3 T,1 T,2 T,3 q1 q2 q3. 

If analysis=3, 4, the outputs will be 

y1 y2 y3 11 22 33 223 213 212 −E∗1 −E∗2 −E∗3 σ11 σ22 σ33 σ23 σ13 σ12 D1 D2 D3 

If analysis=5, 6, the outputs will be 

y1 y2 y3 11 22 33 223 213 212 −E∗1 −E∗2 −E∗3 −H∗1 −H∗2 −H∗3 σ11 σ22 σ33 σ23 σ13 σ12 $D _ { 1 }$ D2 D3 B1 B2 B3. 

If the local results are desired to be output in Gmsh format (arg3=LG or LAG), the recovered 3D strain/stress results at nodal points are stored in input file name.sn. This file contains a block for each generalized strain or stress component as follows: 

elem no nodes nodal value 

where elem no is the corresponding element number, nodes is the total number of nodes in this element, and nodal values is an array holding nodes nodal values of the strain or strain component. Each block contains nelem lines and blocks are separated by a blank line. For example, if analysis=5,6, there will be 24 blocks of data arranged according to the order first for the generalized strains, then for the generalized stresses according to SwiftCompTM convention specified in Eqs. (29) and (30). 

The above local 3D strain/stress results are expressed in the problem coordinate system. Sometimes it is more convenient to have strain/stress values expressed in the material coordinate system. These values at nodal points are stored in the file input file name.snm. 

The failure analysis results are stored in the file input file name.fi, the content of which depends on the type of analysis. For failure index analysis (FI), the failure index and strength ratio for each element are stored in input file name.fi with the first number is an integer indicating the element number and the trailing two numbers are the initial failure index and the initial strength ratio for each element under given loads. For Hashin failure criterion, the failure modes are also output for the corresponding element. For initial strength analysis (F), this file stores the initial failure strengths in both tensile and compressive directions. For failure envelope analysis (FE), this file stores the failure envelope points with the first number being the number of the failure point, the two trailing read numbers being the values for corresponding given two loading directions needed for plotting the failure envelope. 
