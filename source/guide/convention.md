# Conventions


To understand the inputs and interpret outputs of the program correctly, we need to explain some conventions used in SwiftComp.

## Elements

SwiftComp meshes 1D SGs using two-node, three-node, four-node, or five-node elements for as shown in [](#fig-1d-element-nodal-numbering).
Nodes 3, 4, 5 are optional and one or more of these nodes can be missing for a valid 1D element.
It is recommended to use 2-node elements for 3D structures with a 1D SG (see Figure 3a) and 5-node elements for 2D plate/shell models with a 1D SG (see Figure 5a). 

:::{figure-md} fig-1d-element-nodal-numbering
![](../_static/1d-element-nodal-numbering.png)

1D element nodal numbering.
:::

SwiftComp meshes 2D SGs using either triangular or quadrilateral elements as shown in Figure 9.
It is also shown in the figure that SwiftComp numbers the nodes of each 2D elements in the counterclockwise direction.
Nodes 1, 2, and 3 of the triangular elements and nodes 1, 2, 3, and 4 of the quadrilateral elements are at the corners.
For triangular element, the fourth node is zero to inform SwiftComp that it is a triangular element.
Nodes 5, 6, 7 of the triangular elements and nodes 5, 6, 7, 8, 9 of quadrilateral elements are optional.
Any one or more of these nodes can be missing for a valid 2D element. 

:::{figure-md} fig-2d-element-nodal-numbering
![](../_static/2d-element-nodal-numbering.png)

2D element nodal numbering.
:::

SwiftComp meshes 3D SGs using tetrahedral elements, brick elements, or wedge elements as shown in Figure 10.
For tetrahedral elements, the fifth node is zero to inform SwiftComp that it is a tetrahedral element.
For wedge elements, the seventh node is zero to inform SwiftComp that it is a wedge element.
The nodes other than the corners are optional.
Any one or more of these nodes can be missing for a valid 3D element.

:::{figure-md} fig-3d-element-nodal-numbering
![](../_static/3d-element-nodal-numbering.png)

3D element nodal numbering.
:::


## Local Coordinate System, Elemental Coordinate System, and Material Coordinate System

First, SwiftComp uses a right-hand Cartesian coordinate system, also called the *local coordinate system*, denoted as $y_1$, $y_2$ and $y_3$, to describe a 3D SG, $y_{2}$ and $y_{3}$ to describe a 2D SG, and $y_{3}$ to describe a 1D SG (see Figure 11).
$y_{1}$, $y_{2}, and $y_{3}$ are parallel to the *global coordinates* $x_{1}$, $x_{2}, and $x_{3}$, respectively.
The global coordinates $x_{1}$, $x_{2}$, and $x_{3}$ are used to describe the original structure and the macroscopic structure.
Note that if the material properties are provided in a coordinate system different from $y_{1}$, $y_{2}$, $y_{3}$, an additional coordinate system called the *material coordinate system* should be defined and a transformation of the material properties from the material coordinate system into those expressed in the local coordinate system is automatically carried out by SwiftComp.

:::{figure-md} fig-local-coordinate-system
![](../_static/6b42f9c580a25670aaee1b3dc281723d_MD5.jpg)

Local coordinate system describing SG.
:::

In SwiftComp, an elemental coordinate system $y_{i}^{\prime}$ can be defined for each element denoted by three points $a$, $b$, $c$, with the line from point $c$ to point $a$ denoting $y_{1}^{\prime}$ direction and the line from point $c$ to point $b$ denoting a line located in the $y_{1}^{\prime}$-$y_{2}^{\prime}$ plane; see Figure 12 for a sketch.
Speaking in the language of vectors, the new coordinate system is defined by three points with position vectors in the local coordinate system ( $y_{i}$ with $\hat{\mathbf{e}}_{i}$ as the unit vectors) by $\mathbf{a}$, $\mathbf{b}$, and $\mathbf{c}$.
$\mathbf{a}-\mathbf{c}$ denotes $\hat{\mathbf{e}}_{1}^{\prime}$, $\mathbf{b}-\mathbf{c}$ is a vector in the $y_{1}^{\prime}$-$y_{2}^{\prime}$ plane.
With this information, one can compute the direction cosine matrix relating $y_{i}$ to $y_{i}^{\prime}$ according to the following steps: 

- Obtain $\hat{\mathbf{e}}_{1}^{\prime}$ through normalization of $\mathbf{a} - \mathbf{c}$: $\hat{\mathbf{e}}_{1}^{\prime} = \frac{\mathbf{a}-\mathbf{c}}{|\mathbf{a}-\mathbf{c}|}$;
- Obtain $\hat{\mathbf{e}}_{3}^{\prime}$ through normalization of the cross product of $\hat{\mathbf{e}}_{1}^{\prime}$ and $\mathbf{b}-\mathbf{c}$: $\hat{\mathbf{e}}_{3}^{\prime} = \frac{\hat{\mathbf{e}}_{1}^{\prime} \times (\mathbf{b} - \mathbf{c})}{|\hat{\mathbf{e}}_{1}^{\prime} \times (\mathbf{b} - \mathbf{c})|}$;
- Obtain $\hat{\mathbf{e}}_{2}^{\prime}$ through the cross product of $\hat{\mathbf{e}}_{3}^{\prime}$ and $\hat{\mathbf{e}}_{1}^{\prime}$: $\hat{\mathbf{e}}_{2}^{\prime} = \hat{\mathbf{e}}_{3}^{\prime} \times \hat{\mathbf{e}}_{1}^{\prime}$


:::{figure-md} fig-elemental-coordinate-system
![](../_static/5a8d1b762963f7bd4d37dd1800f1457d_MD5.jpg)

Elemental coordinate system defined by three points.
:::

SwiftComp allows the user to define the material properties in the local coordinate system $y_{i}$ or in the material coordinate system.
The material coordinate system could be the elemental coordinate system or a coordinate system defined in such a way that it can be obtained by a simple rotation about $y_{3}^{\prime}$ of the elemental coordinate system.
Clearly for composite laminates, this simple rotation corresponds to the layup angle. 


## Constituent Constitutive Models

Generally speaking, the constituents contained in a SG could be responsive to thermal, mechanical, electric, and magnetic fields. If these effects are not coupled, the linear elastic behavior can be modeled using the Hooke’s law in Eq. (3). 

To deal with uncoupled thermal, electric, and magnetic effects, conduction can be modeled using the following constitutive relation: 

$$
\left\{ \begin{array}{l} q _ {1} \\ q _ {2} \\ q _ {3} \end{array} \right\} = - \left[ \begin{array}{c c c} k _ {1 1} & k _ {1 2} & k _ {1 3} \\ k _ {1 2} & k _ {2 2} & k _ {2 3} \\ k _ {1 3} & k _ {2 3} & k _ {3 3} \end{array} \right] \left\{ \begin{array}{l} T _ {, 1} \\ T _ {, 2} \\ T _ {, 3} \end{array} \right\} \tag {25}
$$

where $q _ { i }$ is the heat flux, $k _ { i j }$ is the conductivity, and $T _ { , i }$ is the gradient of the temperature $T$ .
Since conduction is mathematically analogous to electrostatics, magnetostatics, and diffusion, SwiftComp can also be used to predict effective dielectric, magnetic, and diffusive properties of composite materials and the corresponding local fields.
For example, to obtain the effective dielectric properties, we just need to let $q _ { i }$ denote the electric displacements, $T$ denote the electric potential, and $k _ { i j }$ denote the corresponding dielectric properties. 

For coupled mutliphysics modeling, we will have piezoelectric and piezomagnetic effects as well as pyroelectric, pyromagnetic, and electromagnetic effects.
For linear behavior among all these fields, the constitutive equations can be expressed as: 

$$
\sigma_ {i j} = C _ {i j k l} \varepsilon_ {k l} - e _ {k i j} E _ {k} - q _ {k i j} H _ {k} + \Lambda_ {i j} \theta
$$

$$
D _ {i} = e _ {i k l} \varepsilon_ {k l} + k _ {i k} E _ {k} + a _ {i k} H _ {k} + p _ {i} \theta \tag {26}
$$

$$
B _ {i} = q _ {i k l} \varepsilon_ {k l} + a _ {i k} E _ {k} + \mu_ {i k} H _ {k} + m _ {i} \theta
$$

where $C _ { i j k l }$ , $e _ { k i j }$ , $q k i j$ , and $\Lambda _ { i j }$ are the elastic, the piezoelectric, the piezomagnetic, and the thermal stress tensors, respectively (note that $\Lambda _ { i j } = - C _ { i j k l } \alpha _ { k l }$ with $\alpha _ { k l }$ as the thermal expansion tensor); $\sigma _ { i j }$ and $\varepsilon _ { i j }$ are the stress tensor and strain tensor, respectively; $k _ { i k }$ , $a _ { i k }$ , and $\mu _ { i k }$ are the dielectric, electromagnetic, and magnetic permeability tensors, respectively; and $p _ { i }$ and $m _ { i }$ are the pyroelectric and pyromagnetic vectors, and $D _ { i }$ , $E _ { k }$ , $B _ { i }$ , and $H _ { k }$ are the electric displacement, electric field, magnetic induction, and magnetic field vectors, respectively. $\theta$ denotes the difference between the actual temperature and the reference temperature.
SwiftComp $^ \mathrm { r } \mathrm { { 1 1 } } \mathrm { { M } }$ does not restrict $\theta$ to be small. If $\theta$ is not small, $\Lambda _ { i j } , p _ { i } , m _ { i }$ are not the tangent or instantaneous properties, but the secant properties which are defined as average over a change of temperature. For example, let $\alpha _ { t } ( T )$ denote the tangent or instantaneous coefficient of thermal expansion (CTE), the secant CTE is defined as 

$$
\alpha (T) = \frac {1}{T - T _ {1}} \int_ {T _ {1}} ^ {T} \alpha_ {t} (\zeta) d \zeta = \frac {1}{\theta} \int_ {T _ {1}} ^ {T _ {1} + \theta} \alpha_ {t} (\zeta) d \zeta \tag {27}
$$

with $T _ { 1 }$ as the reference temperature and $\theta = T - T _ { 1 }$ . For convenience, SwiftComp uses tangent or instantaneous properties for $\alpha _ { i j } , p _ { i } , m _ { i }$ as inputs and computes the secant properties internally for constitutive modeling of temperature dependent properties. 

Linear multiphysics behavior is modeled based on the following energy functional corresponding to the constitutive equation in Eq. (26): 

$$
U = \frac {1}{2} \epsilon^ {T} L \epsilon + \epsilon^ {T} \beta \theta - \int_ {T _ {1}} ^ {T} \int_ {T _ {1}} ^ {\zeta} \frac {c _ {v} (0 , \rho)}{\rho} d \rho d \zeta \tag {28}
$$

where 

$$
\epsilon = \left\lfloor \varepsilon_ {1 1} \quad \varepsilon_ {2 2} \quad \varepsilon_ {3 3} \quad 2 \varepsilon_ {2 3} \quad 2 \varepsilon_ {1 3} \quad 2 \varepsilon_ {1 2} - E _ {1} - E _ {2} - E _ {3} - H _ {1} - H _ {2} - H _ {3} \right\rfloor^ {T} \tag {29}
$$

is a multiphysical field array containing the 3D strain field $\varepsilon _ { i j }$ , the 3D electric field $E _ { i }$ , and the 3D magnetic field $H _ { i }$ . The conjugate multiphysical field array $\sigma$ can be expressed as 

$$
\sigma = \left\lfloor \sigma_ {1 1} \sigma_ {2 2} \sigma_ {3 3} \sigma_ {2 3} \sigma_ {1 3} \sigma_ {1 2} D _ {1} D _ {2} D _ {3} B _ {1} B _ {2} B _ {3} \right\rfloor^ {T} \tag {30}
$$

$L$ is a $1 2 \times 1 2$ multiphysics matrix containing all the necessary material constants for characterizing fully coupled thermoelectromagnetoelastic materials such that 

$$
L = \left[ \begin{array}{c c c} C & e & q \\ e ^ {T} & - k & - a \\ q ^ {T} & - a ^ {T} & - \mu \end{array} \right] \tag {31}
$$

where $C$ is a $6 \times 6$ submatrix for elastic constants, $e$ is a $6 \times 3$ submatrix for piezoelectric coefficients, $q$ is a $6 \times 3$ submatrix for piezomagnetic coefficients, $k$ is a $3 \times 3$ submatrix for dielectric coefficients, $a$ is a $3 \times 3$ submatrix for electromagnetic coefficients, and $\mu$ is a $3 \times 3$ submatrix for magnetic permeability. Note $C , k , \mu , a$ are symmetric matrices. The explicit form of the $1 2 \times 1 2$ matrix is as follows 

$$
\left[ \begin{array}{c c c c c c c c c c c c c} C _ {1 1} & C _ {1 2} & C _ {1 3} & C _ {1 4} & C _ {1 5} & C _ {1 6} & e _ {1 1} & e _ {2 1} & e _ {3 1} & q _ {1 1} & q _ {2 1} & q _ {3 1} \\ C _ {1 2} & C _ {2 2} & C _ {2 3} & C _ {2 4} & C _ {2 5} & C _ {2 6} & e _ {1 2} & e _ {2 2} & e _ {3 2} & q _ {1 2} & q _ {2 2} & q _ {3 2} \\ C _ {1 3} & C _ {2 3} & C _ {3 3} & C _ {3 4} & C _ {3 5} & C _ {3 6} & e _ {1 3} & e _ {2 3} & e _ {3 3} & q _ {1 3} & q _ {2 3} & q _ {3 3} \\ C _ {1 4} & C _ {2 4} & C _ {3 4} & C _ {4 4} & C _ {4 5} & C _ {4 6} & e _ {1 4} & e _ {2 4} & e _ {3 4} & q _ {1 4} & q _ {2 4} & q _ {3 4} \\ C _ {1 5} & C _ {2 5} & C _ {3 5} & C _ {4 5} & C _ {5 5} & C _ {5 6} & e _ {1 5} & e _ {2 5} & e _ {3 5} & q _ {1 5} & q _ {2 5} & q _ {3 5} \\ C _ {1 6} & C _ {2 6} & C _ {3 6} & C _ {4 6} & C _ {5 6} & C _ {6 6} & e _ {1 6} & e _ {2 6} & e _ {3 6} & q _ {1 6} & q _ {2 6} & q _ {3 6} \\ e _ {1 1} & e _ {1 2} & e _ {1 3} & e _ {1 4} & e _ {1 5} & e _ {1 6} & - k _ {1 1} & - k _ {1 2} & - k _ {1 3} & - a _ {1 1} & - a _ {1 2} & - a _ {1 3} \\ e _ {2 1} & e _ {2 2} & e _ {2 3} & e _ {2 4} & e _ {2 5} & e _ {2 6} & - k _ {1 2} & - k _ {2 2} & - k _ {2 3} & - a _ {1 2} & - a _ {2 2} & - a _ {2 3} \\ e _ {3 1} & e _ {3 2} & e _ {3 3} & e _ {3 4} & e _ {3 5} & e _ {3 6} & - k _ {1 3} & - k _ {2 3} & - k _ {3 3} & - a _ {1 3} & - a _ {2 3} & - a _ {3 3} \\ q _ {1 1} & q _ {1 2} & q _ {1 3} & q _ {1 4} & q _ {1 5} & q _ {1 6} & - a _ {1 1} & - a _ {2 1} & - a _ {3 1} & - \mu_ {1 1} & - \mu_ {1 2} & - \mu_ {1 3} \\ q _ {2 1} & q _ {2 2} & q _ {2 3} & q _ {2 4} & q _ {2 5} & q _ {2 6} & - a _ {1 2} & - a _ {2 2} & - a _ {3 2} & - \mu_ {1 2} & - \mu_ {2 2} & - \mu_ {2 3} \\ q _ {3 1} & q _ {3 2} & q _ {3 3} & q _ {3 4} & q _ {3 5} & q _ {3 6} & - a _ {1 3} & - a _ {2 3} & - a _ {3 3} & - \mu_ {1 3} & - \mu_ {2 3} & - \mu_ {3 3} \end{array} \right] \tag {32}
$$

Other terms in Eq. (28) include $\beta$ , which is a $1 2 \times 1$ matrix containing the second-order thermal stress tensor $\Lambda _ { i j }$ , the vector of pyroelectric $p _ { i }$ , and the vector of pyromagnetic $m _ { i }$ expressed as 

$$
\beta = \left\lfloor \Lambda_ {1 1} \Lambda_ {2 2} \Lambda_ {3 3} \Lambda_ {2 3} \Lambda_ {1 3} \Lambda_ {1 2} p _ {1} p _ {2} p _ {3} m _ {1} m _ {2} m _ {3} \right\rfloor^ {T} \tag {33}
$$

The coefficient in the last term $c _ { v }$ is the specific heat per unit volume at constant strain. Note in the input, we actually input CTE $\alpha _ { k l }$ to be consistent with what has been normally used in thermoelastic analyses. The code automatically computes $\Lambda _ { i j }$ according to the following formula: 

$$
\left\{ \begin{array}{l} \Lambda_ {1 1} \\ \Lambda_ {2 2} \\ \Lambda_ {3 3} \\ \Lambda_ {2 3} \\ \Lambda_ {1 3} \\ \Lambda_ {1 2} \end{array} \right\} = - \left[ \begin{array}{c c c c c c} C _ {1 1} & C _ {1 2} & C _ {1 3} & C _ {1 4} & C _ {1 5} & C _ {1 6} \\ C _ {1 2} & C _ {2 2} & C _ {2 3} & C _ {2 4} & C _ {2 5} & C _ {2 6} \\ C _ {1 3} & C _ {2 3} & C _ {3 3} & C _ {3 4} & C _ {3 5} & C _ {3 6} \\ C _ {1 4} & C _ {2 4} & C _ {3 4} & C _ {4 4} & C _ {4 5} & C _ {4 6} \\ C _ {1 5} & C _ {2 5} & C _ {3 5} & C _ {4 5} & C _ {5 5} & C _ {5 6} \\ C _ {1 6} & C _ {2 6} & C _ {3 6} & C _ {4 6} & C _ {5 6} & C _ {6 6} \end{array} \right] \left\{ \begin{array}{l} \alpha_ {1 1} \\ \alpha_ {2 2} \\ \alpha_ {3 3} \\ 2 \alpha_ {2 3} \\ 2 \alpha_ {1 3} \\ 2 \alpha_ {1 2} \end{array} \right\} \tag {34}
$$

Note in the right hand side, the off-diagonal CTEs are multiplied by 2 so that we have $2 \alpha _ { 1 2 }$ , $2 \alpha _ { 1 3 }$ , $2 \alpha _ { 2 3 }$ according to the engineering notation. 

As it is a constant confusion among users regarding the units used in the multiphysics modeling, we will provide a detailed description of those units. According to the International Standard unit system, we use Pa (i.e., $\mathbf { N } / \mathbf { m } ^ { 2 }$ ) for the elastic constants $C _ { i j k l }$ and the stress field $o _ { i j }$ (note the strain field $\varepsilon _ { i j }$ is unitless), $\mathbf { C } / \mathbf { m } ^ { 2 }$ for piezoelectric constants $e _ { i j k }$ and electric displacement $D _ { i }$ , $\mathbf { N } / ( \mathbf { A } { \cdot } \mathbf { m } )$ for piezomagnetic constants $q _ { i j k }$ and magnetic induction $B _ { i }$ , $\mathbf { C } / ( \mathbf { V } { \cdot } \mathbf { m } )$ for dielectric constants $k _ { i j }$ , $\mathbf { N } / \mathbf { A } ^ { 2 }$ (or $\mathbf { N } { \cdot } \mathbf { s } ^ { 2 } / \mathbf { C } ^ { 2 }$ ) for magnetic permeability $\mu _ { i j }$ , $\mathbf { C } / ( \mathbf { A } { \cdot } \mathbf { m } )$ for electromagnetic coefficients $a _ { i j }$ , $\mathbf { V } / \mathbf { m }$ for electric field $E _ { i }$ , $\mathbf { A } / \mathbf { m }$ for magnetic field $H _ { i }$ , $\mathbf { K }$ for the temperature field $\theta$ (note $^ \circ \mathbf { C }$ has the same unit dimension as $\mathbf { K }$ ), $\mathbf { 1 } / \mathbf { K }$ for CTE $\alpha _ { i j }$ (correspondingly $\mathbf { P a } / \mathbf { K }$ for thermal stress coefficients $\Lambda _ { i j }$ ), $\mathbf { C } / \mathbf { m } ^ { 2 } { \cdot } \mathbf { K }$ for pyroelectric constants $p _ { i }$ , $\mathbf { N } / ( \mathbf { A } { \cdot } \mathbf { m } { \cdot } \mathbf { K } )$ for pyromagnetic $m _ { i }$ , and $\mathbf { J } / ( \mathbf { m } ^ { 3 } { \cdot } \mathbf { K } )$ for the specific heat . With all these units, the energy density $U$ will be in the $c _ { v }$ unit of $\mathbf { N } / \mathbf { m } ^ { 2 }$ , which is the same as $\mathbf { J } / \mathbf { m } ^ { 3 }$ . Note N=C·V/m and J=N·m. 

Although the units aforementioned are consistent with each other, direct use of these units will introduce an extremely ill-conditioned material matrix $L$ as for regular materials, we have $C _ { i j k l }$ in the order of $1 0 ^ { 1 1 }$ , while $k _ { i j }$ in the order of $1 0 ^ { - 9 }$ . Proper scaling is needed even if double precision is used in computing. To this end, we define $\begin{array} { r } { E _ { i } ^ { * } = \frac { E _ { i } } { 1 0 ^ { 9 } } , H _ { i } ^ { * } = \frac { H _ { i } } { 1 0 ^ { 9 } } } \end{array}$ , then the energy density in Eq. (28) can be rewritten as: 

$$
\frac {U}{1 0 ^ {9}} = \frac {1}{2} \left\{ \begin{array}{l} \varepsilon \\ - E ^ {*} \\ - H ^ {*} \end{array} \right\} ^ {T} \left[ \begin{array}{c c c} C ^ {*} & e & q \\ e ^ {T} & - k ^ {*} & - a ^ {*} \\ q ^ {T} & - a ^ {* T} & - \mu^ {*} \end{array} \right] \left\{ \begin{array}{l} \varepsilon \\ - E ^ {*} \\ - H ^ {*} \end{array} \right\} + \left\{ \begin{array}{c} \varepsilon \\ - E ^ {*} \\ - H ^ {*} \end{array} \right\} ^ {T} \left\{ \begin{array}{c} - C ^ {*} \alpha \\ p \\ m \end{array} \right\} \theta - \int_ {T _ {1}} ^ {T} \int_ {T _ {1}} ^ {\zeta} \frac {c _ {v} ^ {*} (0 , \rho)}{\rho} d \rho d \zeta \tag {35}
$$

with 

$$
C ^ {*} = \frac {C}{1 0 ^ {9}}, \quad c _ {v} ^ {*} = \frac {c _ {v}}{1 0 ^ {9}}, \quad k ^ {*} = k \times 1 0 ^ {9}, \quad a ^ {*} = a \times 1 0 ^ {9}, \quad \mu^ {*} = \mu \times 1 0 ^ {9} \tag {36}
$$

The generalized Hooke’s law given in Eq. (26) can be rewritten in the following matrix form: 

$$
\sigma^ {*} = C ^ {*} \varepsilon - e E ^ {*} - q H ^ {*} + \Lambda^ {*} \theta
$$

$$
D = e ^ {T} \varepsilon + k ^ {*} E ^ {*} + a ^ {*} H ^ {*} + p \theta \tag {37}
$$

$$
B = q ^ {T} \varepsilon + a ^ {* T} E ^ {*} + \mu^ {*} H ^ {*} + m \theta
$$

with $\begin{array} { r } { \sigma ^ { * } = \frac { \sigma } { 1 0 ^ { 9 } } } \end{array}$ . For SwiftComp $^ \mathrm { { 4 M } }$ to perform multiphysics homogenization, we input $C ^ { \ast } , c _ { v } ^ { \ast } , e , q , k ^ { \ast }$ $a ^ { * } , \mu ^ { * } , \alpha , p , m$ as material properties, and for SwiftComp to perform multiphysics dehomogenization, we input $\varepsilon , E ^ { * } , H ^ { * }$ as the global fields. In other words, if the quantities are given in IS units, we need to divide $C , c _ { v } , E , H$ by $1 0 ^ { 9 }$ , and multiply $k , a , \mu$ by $1 0 ^ { 9 }$ , and all the other quantities remain the same. The output effective properties are also scaled the same way as the input material properties. As far as the local fields out of dehomogenization are concerned, the mechanical displacement, strains, electric displacements, and magnetic induction are the same as SI units, however one needs to multiply the electromagnetic potential, the stresses, electric and magnetic fields with $1 0 ^ { 9 }$ to convert these quantities in SI units. Note, it is just one suggestion for users to scale SwiftComp inputs to avoid numerical difficulties. This scaling is done externally by the end user of the code. One can certainly devise a different scaling following the same idea given here. 
