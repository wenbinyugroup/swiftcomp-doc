
# Inputs for Homogenization Run

Although general-purpose preprocessors can been developed to prepare SwiftComp input files, it is still beneficial for advanced users, particularly those who want to embed SwiftComp in their own software environments, to understand the meaning of the input data. 

## Extra Inputs for Dimensionally Reducible Structures

To construct a beam/plate/shell model, the beginning of the input file has two extra lines for a plate/shell model, and three extra lines for a beam model.

### Beam Model

```
  model
    k11     k12    k13
 cos_11  cos_21
```

:`model`:
    Integer. Beam model.
    - 0: Classical model (Euler-Bernoulli beam model)
    - 1: Shear refined model (Timoshenko beam model)
    - 2: Vlasov beam model
    - 3: Beam model with the trapeze effect

:`k11  k12  k13`:
    Real numbers. Initial twist/curvatures of the structure. If the structure is initially straight, zeroes should be provided instead.

:`cos_11  cos_21`:
    Real numbers. Oblique cross-section, see Figure 13 for a sketch of such a cross-section.
    - `cos_11`: Cosine of the angle between normal of the oblique section ($y_1$) and beam axis $x_{1}$.
    - `cos_21`: Cosine of the angle between $y_{2}$ of the oblique section and beam axis ($x_{1}$).
    The summation of the square of these two numbers should not be greater than 1.0 in double precision.
    The inputs including coordinates, material properties, etc. and the outputs including mass matrix, stiffness matrix, etc. are given in the oblique system, the $y_{i}$ coordinate system as shown in Figure 13.
    For normal cross-sections, we provide `1.0  0.0` on this line instead.


### Plate/Shell Model

```
  model
    k12    k21
```

:`model`:
    Integer. Plate/shell model.
    - 0, it will construct a classical model (Euler-Bernoulli beam model or Kirchhoff-Love plate/shell model).
    - 1, it will construct a shear refined model (Timoshenko beam model or Reissner-Mindlin plate/shell model).

:`k12  k21`:
    Real numbers. Initial twist/curvatures of the structure.
    If the structure is initially straight, zeroes should be provided instead.


## Inputs for All Structural Models

### Control parameters


The following line (note: to construct a 3D structural model, the previous three lines do not exist and the input file starts from this line.) has four integers providing the problem control parameters as: 

```
analysis  elem_flag  trans_flag  temp_flag 
```

The parameter analysis is an integer denoting the type of analysis: 0-elastic; 1-thermoelastic; 2- conduction; 3-piezoeletric/piezomagnetic; 4-thermopiezoeletric/thermopiezomagnetic; 5-piezoeletromagnetic; 6-thermopiezoeletromagnetic; 7-viscoelastic; 8-thermoviscoelastic; 9-homogenization to 

![image](notes/dev/sc/_resources/44b3576b2055f3d1cfc0ab4470b03d87_MD5.jpg)



Figure 13: Sketch of an oblique reference cross-section.


8-node 3D element; 10- homogenization to 20-node 3D element. It is pointed out here that piezoelectric effects are mathematically equivalent to piezomagnetic effects. In other words, the same equation or code used for modeling piezoelectric materials can be used to model piezomagnetic materials if we replace electric displacement $D _ { i }$ with magnetic induction $B _ { i }$ , electric field $E _ { i }$ with magnetic field $H _ { i }$ , piezoelectric properties $e _ { k i j }$ with piezomagnetic properties $q k i j$ , pyroelectric properties $p _ { i }$ with pyromagnetic properties $m _ { i }$ . Later, for analysis=3 or 4, in the inputs we used piezoelectric materials as example. It is directly applicable to piezomagnetic materials. 

The parameter elem flag is an integer denoting the type of elements. If elem flag is equal to 0, the regular elements as shown in Figures 8, 9, 10 will be used for 1D, 2D or 3D SGs. If it is equal to 1, elements with one dimension degenerated will be used to model the SG. For example, 2D shell elements based on relative degrees of freedom will be used to mesh a 3D SG or 1D elements will be used to mesh a 2D SG. If it is equal to 2, 1D elements will be used to mesh a 3D SG. For example, 1D beam elements can be used to model a 3D SG composed of slender truss-like members. Currently only regular elements are implemented. 

The parameter trans flag is an integer denoting whether transformation of the element orientation is needed. If trans flag is equal to 0, element orientation is the same as the problem coordinate system and transformation is not needed. If it is equal to 1, elemental coordinate systems are defined for each element and elemental orientations will be provided in a later block for the transformation. 

The parameter temp flag is an integer denoting whether the temperature is uniform within the SG. For thermally coupled analysis (analysis=1, 4, $\boldsymbol { \mathit { 6 } }$ ), if temp flag is equal to 0, temperature distribution within SG is uniform; if it is equal to 1, temperature distribution is not uniform and nodal temperature should be provided to describe the temperature field. Note this input is used only if it is a thermally coupled analysis. 

If analysis=7 or 8, the next line will list three real numbers arranged as: 

$t _ { 0 }$ , $t _ { e }$ , dt 

where $t _ { 0 }$ is the starting time, $t _ { e }$ is the ending time, and $d t$ is the increment of time. Note, in the current version we follow the conventional practice of thermoviscoelastic analysis. The real time ranges from $1 0 ^ { t _ { 0 } }$ to $1 0 ^ { t _ { e } }$ with time increment of $1 0 ^ { d t }$ . The code will compute time-dependent effective properties at $1 0 ^ { t _ { 0 } } , 1 0 ^ { t 0 + d t } , \ldots , 1 0 ^ { t _ { e } }$ . 

If the SG is aperiodic or partially periodic, the next line will list three integers arranged as: 

py1 py2 py3 

where py1, py2 py3 could be 1, or 0 indicating whether it is aperiodic or periodic along $y _ { 1 } , y _ { 2 } , y _ { 3 }$ directions, respectively. For example, for a 3D SG which is aperiodic along $y _ { 2 }$ direction, we will have 

0 1 0 

It noted that for the 2D plate/shell model, only $y _ { 1 }$ or $y _ { 2 }$ can be periodic or aperiodic and for the 1D beam model, only $y _ { 1 }$ can be periodic or aperiodic. 

The next line lists six integers arranged as: 

nSG nnode nelem nmate nslave nlayer nsurf nodes 

where $n S G$ is the dimensionality of the SG, nnode is the total number of nodes, nelem is the total number of elements, nmate is the total number of material types, nslave is the number of slave nodes on periodic boundaries for periodic microstructures, and nlayer is the total number of layers defined by different types of materials and layup angle. nsurf nodes is the total number of nodes for the outside surfaces of the SG. For the current version, nsurf nodes is only implemented for analysis=9 or 10. If nslave= $\boldsymbol { \mathit { 0 } }$ , SwiftComp will search for corresponding node on periodic boundaries. For this reason, the SG must be regular rectangles (for 2D SG) or cuboids (for 3D SG) with the FE mesh having corresponding nodes on periodic edges. For other periodic SG shapes, the paired nodes on corresponding boundaries must be provided through setting nslave not equal to zero. 

### Mesh

The next nnode lines are the coordinates for each node arranged as: 

```
node_no  y1  y2  y3 
```

where node no is an integer representing the unique number assigned to each node and $y _ { 1 }$ , $y _ { 2 }$ , y3 are three real numbers describing the location $( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ of the node (only $y _ { 3 }$ exists for 1D SGs, and $y _ { 2 }$ and $y _ { 3 }$ exist for 2D SGs). Arrangement of node no is not necessary to be consecutive, but all nodes from 1 to nnode should be present. 

The next nelem lines list the layer number and nodes for each element. They are arranged as:

```
elem_no  mate_id  node_1  node_2 ...
```

where elem no is the number of element, mate id is an integer to indicate the material number of 

the element, and node i ( $i = 1 , 2 , \dots ,$ ) are nodes belonging to this element. If nlayer is not equal to zero, then mate id should be replaced with layer id which will be defined later. Arrangement of elem no is not necessary to be consecutive, but all elements starting from 1 to nelem should be present. If the SG is meshed using regular elements (e.g., elements having the same dimension as the SG, 

• 1D elements could have up to 5 nodes. If a node is not present in the element, the value is 0; see Figure 8. 

• 2D elements could have up to 9 nodes. If a node is not present in the element, the value is 0. If the fourth node is zero, it is a triangular element; see Figure 9. 

• 3D elements could have up to 20 nodes. If a node is not present in the element, the value is 0. If the fifth node is zero, it is a tetrahedral element; If the fifth node is not zero, but the seventh node is zero, it is a wedge element; see Figure 10. 

If trans flag is equal to 1, the next nelem lines list the orientation for each element. They are arranged as 

elem no $a _ { 1 } \ a _ { 2 } \ a _ { 3 } \ b _ { 1 } \ b _ { 2 } \ b _ { 3 } \ c _ { 1 } \ c _ { 2 } \ c _ { 3 }$ 

where elem no is the number of element, $a _ { 1 } , a _ { 2 } , a _ { 3 }$ are coordinates of point $a$ , $b _ { 1 } , b _ { 2 } , b _ { 3 }$ are coordinates of point $b$ , $c _ { 1 } , c _ { 2 } , c _ { 3 }$ are coordinates of point $c$ . The local coordinate system for the element is defined by the three points $a , b , c$ as described previously. Arrangement of elem no is not necessary to be consecutive, but all elements starting from 1 to nelem should be present. 

If temp flag is equal to 1, the temperature distribution within the SG is not uniform, the next nnode lines list the corresponding nodal temperature. They are arranged as: 

node no $T$ 

where node no is the nodal number and $T$ is the corresponding temperature. 

If analysis is equal to 9, the next line lists the nodes of the macroscopic 3D 8-node element. They are arranged as: 

node 1 node 2 node 3 . . . node 8 

where $n o d e _ { i }$ corresponds to the 8 nodes of the macroscopic 3D 8-node element numbered in the same order as those in Figure 10. 

If analysis is equal to 10, the next line lists the nodes of the macroscopic 3D 20-node element. They are arranged as: 

node 1 node 2 node 3 . . . node 20 

where nodei corresponds to the 20 nodes of the macroscopic 3D 20-node element numbered in the same order as those in Figure 10. 

If analysis is equal to 9 or 10, the next one or more lines list the nodes on the surfaces. The total number of surface nodes is nsurf nodes. No specific format is needed. 

If nslave is not equal to 0, the next nslave lines list the slave nodes and corresponding master nodes periodic to the slave nodes. They are arranged as: 

slave node master node 

where slave node is an integer indicating the node slaved to the master node denoted by master node. 

If nlayer is not equal to 0, the next nlayer lines list the definition for each layer. They are arranged as: 

layer id mate id angle 

where layer id is the layer number, mate id is the material type, and angle is a real number for the layup angle in degrees. 



[materials](sc-inputs-homo-material.md)



The following line is used to input $\omega$ , the volume of the domain spanned by the remaining coordinates in the macroscopic structural model. For 3D structural models, $\omega$ will be the volume of the homogenized material including both the volume of the material and the volume of possible voids in the SG. $\omega$ can be computed by any mesh generator. For regular SG such as cubes, it can be easily calculated by hand. Of course, for 1D SGs, the volume is the length and for 2D SGs, the volume is the area. For plate/shell models, $\omega$ will be the area spanned by $y _ { 1 }$ and $_ { y 2 }$ for 3D SGs, the length along $y _ { 2 }$ for 2D SGs and 1.0 for 1D SGs. For beam models, $\omega$ will be the length along $y _ { 1 }$ for 3D SGs and 1.0 for 2D SGs. 

Till now, we have prepared all the inputs necessary for the homogenization run. 
