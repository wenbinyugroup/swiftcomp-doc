# Dehomogenization Input File

If the command argument `ANALYSIS` is 1, 10, 2, 20, or 3, users should provide additional information in the dehomogenization input file for VABS to perform a dehomogenization analysis.

```{note}
A corresponding homogenization analysis must be run before carrying out the dehomogenization analysis.
```

The overall arrangement of the dehomogenization input file is as follows:
```
[MATERIAL_STRENGTHS]

{GLOBAL_RESPONSES}
```
where
:`[MATERIAL_STRENGTHS]`:
    Strength properties for each material.
    This block of data is needed only if `analysis`=3.
:`{GLOBAL_RESPONSES}`:
    Global beam responses obtained from the 1D global beam analysis.
    This block of data is needed only if `analysis`=1 or 2.


## Material Strengths

```{note}
This block of data is needed only if the command argument `ANALYSIS` is 3.
```

Strength properties for each material include a failure criterion and corresponding strength constants.
Two lines will be inserted and the inputs needed for failure analyses should be arranged as:
```
failure_criterion  num_of_constants
{CONSTANTS}
```
where
:`failure_criterion`:
    A positive integer indicator for the failure criterion.
    A number from 1 to 5 indicates a built-in failure criterion.
    A number greater than 10 indicates a user-defined failure criterion.
:`num_of_constants`:
    The number of strength constants needed for the corresponding material type and failure criterion.
:`CONSTANTS`:
    List of corresponding strength constants.

:::{note}
The order of the materials should be the same as the order in the homogenization input file.
:::

Depending on the type of material, specifications of these arguments are different.

### Isotropic materials (`type` is 0)

For isotropic material, the following five built-in failure criteria are available:

#### `failure_criterion` is 1: Max principal stress criterion

Two strength constants are needed:
- one for tensile strength ($X$) and
- one for compressive strength ($X^′$ ), arranged as $X$, $X^′$.

```none
1  2
X  X'
```

#### `failure_criterion` is 2: Max principal strain criterion

Two strength constants in terms of strains are needed:
- one for tensile strength ($X_\varepsilon$) and
- one for compressive strength ($X^′_{\varepsilon}$), arranged as $X_\varepsilon$, $X^′_\varepsilon$.

```none
2  2
X_e  X'_e
```

#### `failure_criterion` is 3: Max shear stress (Tresca) criterion

One strength constant is needed:
- shear strength constant ($S$).

```none
3  1
S
```

#### `failure_criterion` is 4: Max shear strain criterion

One strength constant in terms of strains is needed:
- shear strength constant in terms of strains ($S_\varepsilon$).

```none
4  1
S_e
```

#### `failure_criterion` is 5: Mises criterion

One strength constant ($X$) is needed.

```none
5  1
X
```

### Non-isotropic materials (`type` is not 0)

For non-isotropic materials (transversely isotropic, orthotropic, or general anisotropic), the following five built-in failure criteria are available:

#### `failure_criterion` is 1: Max stress criterion

Nine strength constants are needed:
- tensile strengths ($X$, $Y$, $Z$) in three directions
- compressive strengths ($X^′$ , $Y^′$ , $Z^′$ ) in three directions
- shear strengths ($R$, $T$, $S$) in three principal planes

```none
1  9
X  Y  Z  X'  Y'  Z'  R  T  S
```

#### `failure_criterion` is 2: Max strain criterion

Nine strength constants in terms of strains are needed:
- tensile strengths ($X_\varepsilon$, $Y_\varepsilon$, $Z_\varepsilon$) in three directions
- compressive strengths ($X^′ _\varepsilon$, $Y^′_\varepsilon$, $Z^′_\varepsilon$) in three directions
- shear strengths ($R_\varepsilon$, $T_\varepsilon$, $S_\varepsilon$) in three principal planes

```none
2  9
X_e  Y_e  Z_e  X'_e  Y'_e  Z'_e  R_e  T_e  S_e
```

#### `failure_criterion` is 3: Tsai-Hill criterion

Six strength constants are needed:
- normal strengths in three directions
- shear strengths in three principal planes

```none
3  6
X  Y  Z  R  T  S
```

#### `failure_criterion` is 4: Tsai-Wu criterion

Nine strength constants are needed:
- tensile strengths (X, Y, Z) in three directions
- compressive strengths ($X^′$, $Y^′$, $Z^′$) in three directions
- shear strengths ($R$, $T$, $S$) in three principal planes

```none
4  9
X  Y  Z  X'  Y'  Z'  R  T  S
```

#### `failure_criterion` is 5: Hashin criterion

Six strength constants are needed:
- tensile strengths ($X$, $Y$) in two directions
- compressive strengths ($X^′$, $Y^′$) in two directions
- shear strengths ($R$, $S$) in two principal planes

```none
5  6
X  Y  X'  Y'  R  S
```

:::{note}
For failure analyses, general anisotropic materials are approximated using orthotropic materials due to limited number of strength constants.
:::

In VABS, both the tensile strengths and compressive strengths are expressed using positive numbers.
In other words, in the uniaxial compressive test along $y_1$ direction, $\sigma_{11}=−X^′$ when material fails.

## Global Responses

The rest of inputs in the dehomogenization input file contains the global beam responses obtained from the 1D global beam analysis.

```
u1   u2   u3

C11  C12  C13
C21  C22  C23
C31  C32  C33

{BEAM_STRAIN/STRESS_RESULTANTS}
```
where
:`u1`, `u2`, `u3`:
    1D beam displacements along $x_1$, $x_2$, $x_3$, respectively.
:`Cij`:
    Direction cosine matrix defined as $\mathbf{B}_{i} = C_{i1}\mathbf{b}_{1} + C_{i2}\mathbf{b}_{2} + C_{i3}\mathbf{b}_{3} \text{    with } i = 1, 2, 3$ where $B_1$, $B_2$, and $B_3$ are the base vectors of the deformed beam and $b_1$, $b_2$, and $b_3$ are the base vectors of the undeformed beam.
:`{BEAM_STRAIN/STRESS_RESULTANTS}`:
    Beam strain/stress resultants obtained from the 1D global beam analysis.
    The arrangement of these data is different for different beam models.

:::{note}
`ui` and `Cij` are needed only for recovering 3D displacements.
If the user is not interested in 3D displacements, these values can be arbitrary real numbers.
:::

### Classical model

To carry out a dehomogenization analysis based on the classical model, VABS requires the following data:
```none
F1   M1   M2   M3
```
where
- `F1` is the axial force
- `M1` is the torque
- `M2` is the bending moment around $x_2$, and
- `M3` is the bending moment around $x_3$.

:::{admonition} Example
:class: tip

If the user wants to compute these quantities under 1 unit tensile axial force along with 1 unit bending moment around $x_2$, the inputs can be arranged as:
```none
0  0  0

1  0  0
0  1  0
0  0  1

1  0  1  0
```
:::

To perform dehomogenization for multiple load cases, the user needs to insert corresponding lines of `F1`, `M1`, `M2`, `M3` after the end of this block.

:::{admonition} Example
:class: tip

To perform dehomogenization for two more load cases with `F1` = 2, `M1` = 2, `M2` = `M3` = 0 and `F1` = 2, `M1` = 3, `M2` = 4, `M3` = 5, we must provide the following inputs:
```none
0  0  0

1  0  0
0  1  0
0  0  1

1  0  1  0
2  2  0  0
2  3  4  5
```
:::


### Timoshenko model

To carry out a dehomogenization analysis based on the Timoshenko model, VABS requires the following data:
```none
F1   M1   M2   M3
F2   F3
f1     f2     f3     m1     m2     m3
f1'    f2'    f3'    m1'    m2'    m3'
f1''   f2''   f3''   m1''   m2''   m3''
f1'''  f2'''  f3'''  m1'''  m2'''  m3'''
```
where
- the additional data `F2` and `F3` are transverse shear forces along $x_2$ and $x_3$, respectively.
- `f1`, `f2`, `f3` are distributed forces (including both applied forces and inertial forces) per unit span along $x_1$, $x_2$, $x_3$ respectively.
- `m1`, `m2`, `m3` are distributed moments (including both applied and inertial moments) per unit span along $x_1$, $x_2$, $x_3$ respectively.
- The prime denotes derivative with respect to beam axis, that is $()^{'}=\partial/\partial x_1$, $()^{''} = \partial^2/\partial x_1^2$, and $()^{'''} = \partial^3/\partial x_1^3$.

If `nload` > 1, at the end of the above data block, we need to append two lines (one line for $F_1$, $M_1$, $M_2$, $M_3$ and one line for $F_2$, $F_3$) for each load case.

### Vlasov model

To carry out a dehomogenization analysis based on the Vlasov model, VABS requires the following data:
```none
gamma11  kappa1  kappa2  kappa3  kappa1'  kappa1''  kappa'''
```
where
- `gamma11` is the beam axial strain,
- `kappa1` is the twist ,
- `kappa2` and `kappa3` are the curvatures around $x_2$ and $x_3$ respectively.

:::{note}
The global behavior needed for dehomogenization analyses should not violate the small strain assumption.
Otherwise, you might get some unexpected results.
For example, if your transverse shear stiffness is 2.5 N, then inputting a shear force resultant of 1 N is too large as the shear strain will be about 0.4, which cannot be considered as small, the basic assumption of the VABS theory.
:::

