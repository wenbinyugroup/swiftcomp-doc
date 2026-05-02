# Homogenization Input

## Control parameters

```
    format_flag          nlayer
timoshenko_flag    damping_flag    thermal_flag
     curve_flag    oblique_flag    trapeze_flag    vlasov_flag
           <k1>            <k2>            <k3>
        <cos11>         <cos21>
          nnode           nelem           nmate
```

:`format_flag`:
    Format of the input file.
    - If it is 1, the input is prepared in the new format
    - Otherwise, it is prepared in the old format.

:`nlayer`:
    Number of layers in the section.
    - If `format_flag` is 1, this should be always given a value greater than 0
    - This is not used when using the old format.

    ```{note}
    Here layer is defined as a unique combination of material type and layup orientation, it does not necessarily corresponds to the definition used in the manufacturing sense.
    For example, even if a section is made of a single isotropic material, we consider it has one layer.
    ```

:`timoshenko_flag`:
    Beam model. Choose one from:
    - 0: Classical model (aka Euler-Bernoulli model).
    - 1: Classical model and Timoshenko model.

:`damping_flag`:
    Compute damping matrix. Choose between:
    - 0: Not compute the damping matrix for the section.
    - 1: Will compute the damping matrix.

:`thermal_flag`:
    Carries out thermal analysis. Choose between:
    - 0: Carry out a pure mechanical analysis.
    - 3: Carry out a one-way coupled thermoelastic analysis.

:`curve_flag`:
    Model initially curved and twisted beam. Choose between:
    - 0: Model initially straight beam.
    - 1: Model initially curved and twisted beam. Provide three numbers in the very next line: 
        - `k1`: Twist ($k_1$)
        - `k2`: Curvature around $x_2$ ($k_2$)
        - `k3`: Curvature around $x_3$ ($k_3$)

:`oblique_flag`:
    Model oblique cross-sections. Choose between:
    - 0: Not oblique cross-section.
    - 1: Oblique cross-section. Provide two numbers in the following line to specify the orientation of an oblique reference cross-section, see {numref}`fig-oblique` for a sketch of such a cross-section.
        - `cos11`: Cosine of the angle between normal of the oblique section ($y_1$) and beam axis ($x_1$).
        - `cos21`: Cosine of the angle between ($y_2$) of the oblique section and beam axis ($x_1$).
        
        ```{note}
        The summation of the square of these two numbers should not be greater than 1.0 in double precision.
        The inputs including coordinates, material properties, etc. and the outputs including mass matrix, stiffness matrix, etc. are given in the oblique system, the $y_i$ coordinate system as shown in {numref}`fig-oblique`.
        ```
        ```{note}
        This feature is only enabled for the classical beam model.
        ```

:`trapeze_flag`:
    Model trapeze effect. Choose between:
    - 0: Not model trapeze effect.
    - 1: Model trapeze effect.

:`vlasov_flag`:
    Obtain Vlasov model. Choose between:
    - 0: Not obtain Vlasov model.
    - 1: Obtain Vlasov model.
    ```{note}
    This flag can be 1 only if `timoshenko_flag` is 1.
    VABS will first construct the Timoshenko model, which determines the location of the shear center.
    If the shear center is not at the origin of the beam coordinate system, VABS will move the origin of beam coordinate system to the shear center and repeat the calculation to obtain the Vlasov model.
    ```

:`nnode`:
    Total number of nodes.

:`nelem`:
    Total number of elements.

:`nmate`:
    Total number of materials.


:::{figure-md} fig-oblique
![](../../_static/oblique.jpeg)

Sketch of an oblique reference cross-section
:::




## Mesh


The next `nnode` lines are the coordinates for each node arranged as

```
node_id  x2  x3
```

where

:`node_id`:
    A positive integer representing the unique number assigned to each node

:`x2`:
    A real number for the $x_2$ location of the node.

:`x3`:
    A real number for the $x_3$ location of the node.

```{note}
Although the arrangement of node no is not necessary to be consecutive, every node starting from 1 to `nnode` should be present.
```

The next `nelem` lines are the connectivity relations.
Each line list 10 integers for the nodes for each element, which are arranged as:
```
elem_id  node_1  node_2  node_3  node_4  node_5  node_6  node_7  node_8  node_9
```

where

:`elem_id`:
    Element ID

:`node_1` ... `node_9`:
    Node IDs of this element.
    If a node is not present in the element, the value is 0.
    For a triangular element, set `node_4` to 0.
    See {numref}`fig-tri_elem` and {numref}`fig-quad_elem` for the VABS numbering convention.

```{note}
Although the arrangement of elem no is not necessary to be consecutive, every element starting from 1 to `nelem` should be present.
```


## Element property and orientation

### New format (`format_flag` is 1)

The next `nelem` lines list the layer type and the layer plane angle ($\theta_1$) for each element as:
```
elem_id  layer_type  theta_1
```
where

:`elem_id`:
    Element ID

:`layer_type`:
    A positive integer representing which layer the element belongs to

:`theta_1`:
    A real number describing the layer plane angle ($\theta_1$) of the element.
    Here, $\theta_1$ is assumed to be constant for each element, thus it can be calculated at any material point belonging to the element, such as the centroid, or computed as the average of $\theta_1$ of all the points within the element.

    ```{note}
    For isotropic materials, `theta_1` will not enter the calculations.
    ```

```{note}
Although the arrangement of `elem_no` is not necessary to be consecutive, every element starting from 1 to `nelem` should be present.
```

The next `nlayer` lines define the layers used in the section:
```
layer_id  mate_id  theta_3  <damping_layer>
```
where

:`layer_id`: 
    A positive integer denoting the identification number for the layer.

:`mate_id`:
    A positive integer denoting the material ID used by the layer.

:`theta_3`:
    A real number denoting the layup orientation.

    For example, if layer 1 is made of material 1 and having $−15^{\circ}$ layup, we will provide the information as `1  1  −15.0`.

:`damping_layer`:
    A real number denoting the damping coefficient for the layer.


### Old format (`format_flag` is not 1)

The next `nelem` lines list the material type and layup parameters for each element as
```
elem_id  mate_id  theta_3  theta_1(9)
```
where

:`elem_id`:
    Element ID

:`mate_id`:
    A positive integer representing the type of the material for the element.

:`theta_3`:
    A real number representing the layup angle in degrees for this element.

:`theta_1(9)`:
    An array storing nine real numbers for the layer plane angles at the nodes of this element.
    For simplification, if the ply orientation can be considered as uniform for this element, `theta_1(1)` stores the layer plane angle and `theta_1(2)` = $540^{\circ}$, and all the rest can be zeros or other real numbers because they do not enter the calculation.
    If the element has fewer than nine nodes, zeros are to be input for the corresponding missing nodes, as in the case for connectivity.

    ```{note}
    For isotropic materials, neither `theta_3` nor `theta_1(9)` will enter the calculations.
    ```

```{note}
Although the arrangement of `elem_no` is not necessary to be consecutive, every element starting from 1 to `nelem` should be present.
```


## Materials

The next `nmate` blocks defines the material properties:
```
mate_id  type
{CONSTANTS}
```
where

:`mate_id`:
    A positive integer representing the ID of the material.

:`type`:
    Indicator for the material type. Choose one of the following:
    - 0: Isotropic
    - 1: Orthotropic
    - 2: General anisotropic

:`{CONSTANTS}`:
    Block of material constants depending on the material type `type`.

### Isotropic materials (`type` is 0)

For isotropic materials, `type` is 0, if `thermal_flag` is 0, there are 3 constants arranged as
```
E  nu
rho
```
where `E` is the Young's modulus, `nu` is the Poisson's ratio, and `rho` is the density of the material.
Poisson's ratio must be greater than -1.0 and less than 0.5 for isotropic materials, although VABS allows users to input values that are very close to those limits.

If `thermal_flag` is 3 and `type` is 0, and there are 4 constants arranged as
```
E  nu
rho
alpha
```
where `alpha` is the coefficient of thermal expansion (CTE).


### Orthotropic materials (`type` is 1)

For orthotropic materials, `type` is 1, if `thermal_flag` is 0, there are 10 constants arranged as
```
 E1    E2    E3
 G12   G13   G23
nu12  nu13  nu23
rho
```
including the Young's moduli (`E1`, `E2`, and `E3`), the shear moduli (`G12`, `G13`, and `G23`), the Poisson's ratios (`nu12`, `nu13`, and `nu23`), and the mass density (`rho`).
The convention of values is such that these values will be used to form the following the Hooke's law for composite materials:

$$
\begin{Bmatrix}
\varepsilon_{11} \\
2\varepsilon_{12} \\
2\varepsilon_{13} \\
\varepsilon_{22} \\
2\varepsilon_{23} \\
\varepsilon_{33}
\end{Bmatrix} =
\begin{bmatrix}
\frac{1}{E_1} & 0 & 0 & -\frac{\nu_{12}}{E_1} & 0 & -\frac{\nu_{13}}{E_1} \\
0 & \frac{1}{G_{12}} & 0 & 0 & 0 & 0 \\
0 & 0 & \frac{1}{G_{13}} & 0 & 0 & 0 \\
-\frac{\nu_{12}}{E_1} & 0 & 0 & \frac{1}{E_2} & 0 & -\frac{\nu_{23}}{E_2} \\
0 & 0 & 0 & 0 & \frac{1}{G_{23}} & 0 \\
-\frac{\nu_{13}}{E_1} & 0 & 0 & -\frac{\nu_{23}}{E_2} & 0 & \frac{1}{E_3}
\end{bmatrix}
\begin{Bmatrix}
\sigma_{11} \\
\sigma_{12} \\
\sigma_{13} \\
\sigma_{22} \\
\sigma_{23} \\
\sigma_{33}
\end{Bmatrix}
$$

If `thermal_flag` is 3 and `type` is 1, and there are 13 constants arranged as:
```
E1  E2  E3
G12  G13  G23
nu12  nu13  nu23
rho
alpha11  alpha22  alpha33
```
where `alpha11`, `alpha22`, `alpha33` are the CTEs along three directions.

### General anisotropic materials (`type` is 2)

For general anisotropic materials, `type` is 2, if `thermal_flag` is 0, there are 22 constants arranged as:
```
c11 c12 c13 c14 c15 c16
    c22 c23 c24 c25 c26
        c33 c34 c35 c36
            c44 c45 c46
                c55 c56
                    c66
                    rho
```
These values are defined using the following Hooke's law:

$$
\begin{Bmatrix}
\sigma_{11} \\
\sigma_{12} \\
\sigma_{13} \\
\sigma_{22} \\
\sigma_{23} \\
\sigma_{33}
\end{Bmatrix} =
\begin{bmatrix}
c_{11} & c_{12} & c_{13} & c_{14} & c_{15} & c_{16} \\
c_{12} & c_{22} & c_{23} & c_{24} & c_{25} & c_{26} \\
c_{13} & c_{23} & c_{33} & c_{34} & c_{35} & c_{36} \\
c_{14} & c_{24} & c_{34} & c_{44} & c_{45} & c_{46} \\
c_{15} & c_{25} & c_{35} & c_{45} & c_{55} & c_{56} \\
c_{16} & c_{26} & c_{36} & c_{46} & c_{56} & c_{66}
\end{bmatrix}
\begin{Bmatrix}
\varepsilon_{11} \\
2\varepsilon_{12} \\
2\varepsilon_{13} \\
\varepsilon_{22} \\
2\varepsilon_{23} \\
\varepsilon_{33}
\end{Bmatrix}
$$

If `thermal_flag` is 3 and `type` is 2, there are 28 constants arranged as:

```
c11 c12 c13 c14 c15 c16
    c22 c23 c24 c25 c26
        c33 c34 c35 c36
            c44 c45 c46
                c55 c56
                    c66
                    rho
alpha11  2alpha12  2alpha13  alpha22  2alpha23  alpha33
```
where `alphaij` , with i = 1, 2, 3 and j = 1, 2, 3, are the components of the second-order CTE tensor.
CTEs corresponding to the shear strains are multiplied by two because the engineering shear strains are twice of the corresponding tensorial shear strains.
The material constants are expressed in the material coordinate system (see {numref}`fig-local_coord_sys`).
If the material properties are given in a different coordinate system, or the arrangement of stresses and strains are different from what VABS uses, a proper transformation of the material properties is needed.

If `damping_flag` is 1, a damping coefficient is input on the very next line following the density input.
For example, if `type`=0 and `thermal_flag`=3 (thermoelastic analysis with isotropic materials), the material constants are arranged as:
```
E nu
rho
gamma
alpha
```
where `gamma` is a scalar representing the material damping property.
It is noted that the damping coefficients for each layer and for each material are additive.
In other words, the total damping coefficient used to scale the stiffness-related matrices is `damping_layer`+`gamma`.

If `thermal_flag` is equal to 3, we also need to provide the following `nnode` lines for temperature for each node arranged as
```
node_no  T
```
where `node_no` is an integer representing the unique number assigned to each node and `T` is a real number describing the temperature of the node.
These temperature values can be calculated either from a 3D heat conduction analysis or using VABS Conduction, which is a generalization of the VABS approach for heat conduction analysis.
Although the arrangement of `node_no` is not necessary to be consecutive, every node starting from 1 to `nnode` should be present.

Now, we have prepared all the inputs necessary for performing the homogenization run to compute the inertial properties and structural properties of the cross-section.

