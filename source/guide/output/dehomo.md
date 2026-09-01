
# Dehomogenization

In the outputs of dehomogenization, the primary local field such as the displacement field for elastic analysis or the temperature field for conduction analysis is reported at each node.
However, other fields calculated based on gradients from the primary local field such as stresses and strains are usually more accurate if reported at Gaussian integration points.
However, because nodal values are more convenient for postprocessing of the results, only nodal values are reported.
If you need Gaussian values, please contact the author.

## Local 3D displacements

The local 3D displacement results obtained through dehomogenization are stored in `input_file_name.u`.
The values are listed for each node identified by its location as: 
```
node_no  u_1  u_2  u_3 
```
where `u_i` are the local 3D displacements at this node.

**If `analysis` is 2**, the outputs in this file are the local temperature for each node instead. 

**If `analysis` is 3 or 4**, the outputs will be 
```
node_no  u_1  u_2  u_3  phi_star
```
with `phi_star` as the scaled electric potential. 

**If `analysis` is 5 or 6**, the outputs will be 
```
node_no  u_1  u_2  u_3  phi_star  psi_star 
```
with `psi_star` as the scaled magnetic potential. 


## Local 3D strain/stress

The local 3D strain/stress results at nodes obtained through dehomogenization are stored in `input_file_name.sn`.
These values are identified by its location as: 
```
y_1  y_2  y_3  epsilon_11  epsilon_22  epsilon_33  2epsilon_23  2epsilon_13  2epsilon_12  sigma_11  sigma_22  sigma_33  sigma_23  sigma_13  sigma_12 
```
where `epsilon_ij` and `sigma_ij` are the components of the local 3D strain tensor and 3D stress tensor, respectively, at the node.

**If `analysis` is 2**, the outputs in this file are instead the local temperature gradient and heat flux instead arranged as 
```
y_1  y_2  y_3  T_p_1  T_p_2  T_p_3  q_1  q_2  q_3 
```
**If `analysis` is 3 or 4**, the outputs will be 
```
y_1  y_2  y_3  epsilon_11  epsilon_22  epsilon_33  2epsilon_23  2epsilon_13  2epsilon_12  −E_1_star  −E_2_star  −E_3_star  sigma_11  sigma_22  sigma_33  sigma_23  sigma_13  sigma_12  D_1 D_2 D_3 
```
**If `analysis` is 5 or 6**, the outputs will be 
```
y_1  y_2  y_3  epsilon_11  epsilon_22  epsilon_33  2epsilon_23  2epsilon_13  2epsilon_12  −E_1_star  −E_2_star  −E_3_star  −H_1_star  −H_2_star  −H_3_star  sigma_11  sigma_22  sigma_33  sigma_23  sigma_13  sigma_12  D_1  D_2  D_3  B_1  B_2  B_3 
```


If the local results are desired to be output in Gmsh format (`arg3` is `LG` or `LAG`), the recovered 3D strain/stress results at nodal points are stored in `input_file_name.sn`.
This file contains a block for each generalized strain or stress component as follows: 

```
elem_no  nodes  {NODAL_VALUE}
```

:`elem_no`:
    Integer.
    Element ID

:`nodes`:
    Integer.
    Total number of nodes in this element

:`{NODAL_VALUE}`:
    Array of reals.
    Nodal values of the stress or strain component.

Each block contains `nelem` lines and blocks are separated by a blank line.
For example, if `analysis` is 5 or 6, there will be 24 blocks of data arranged according to the order first for the generalized strains, then for the generalized stresses according to SwiftComp convention specified in Eqs. (29) and (30). 

The above local 3D strain/stress results are expressed in the problem coordinate system.
Sometimes it is more convenient to have strain/stress values expressed in the material coordinate system.
These values at nodal points are stored in the file `input_file_name.snm`. 


## Failure analysis

The failure analysis results are stored in the file `input_file_name.fi`, the content of which depends on the type of analysis.
For failure index analysis (FI), the failure index and strength ratio for each element are stored in `input_file_name.fi` with the first number is an integer indicating the element number and the trailing two numbers are the initial failure index and the initial strength ratio for each element under given loads.
For Hashin failure criterion, the failure modes are also output for the corresponding element.
For initial strength analysis (F), this file stores the initial failure strengths in both tensile and compressive directions.
For failure envelope analysis (FE), this file stores the failure envelope points with the first number being the number of the failure point, the two trailing read numbers being the values for corresponding given two loading directions needed for plotting the failure envelope. 
