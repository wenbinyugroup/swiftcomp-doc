
# Failure Analysis

A corresponding homogenization analysis must be run before carrying out any failure analysis. 

For failure analysis (including initial failure strength, initial failure index/strength ratio, and initial failure envelope), the `*.glb` file will be used to store the data needed for failure analysis instead.


## Shared Inputs for All Types of Failure Analysis

First, additional material properties are needed for each material at each given temperature including a failure criterion and corresponding strength constants.
Three lines will be inserted and the inputs needed for failure analyses should be arranged as: 

```
failure_criterion  num_of_constants 
l_c
{STRENGTH_CONSTANTS}
```

:`failure_criterion`:
    Integer.
    Identifier for the failure criterion.
    A number from 1 to 5 indicates a built-in failure criterion.
    A number greater than 10 indicates a user-defined failure criterion.

:`num_of_constants`:
    Integer.
    Number of strength constants needed for the corresponding failure criterion.

    If `failure_criterion` is 1, 2, 3, 4, or 5, `num_of_constants` is not used.
    If it is a user-defined failure criterion, then `num_of_constants` will be used to input the right number of strength constants.
    It is assumed that the number of strength constants will not be greater than 9 for a material.

:`l_c`:
    Real.
    Characteristic length used in the nonlocal approach for initial failure analysis.

    If $l _ { c }$ is equal to zero, the local approach based on element averaged values will be used.

:`{STRENGTH_CONSTANTS}`:
    Array of reals.
    Strength constants.

    It is noted that this block of data should be corresponding to the material block in the main input file.
    In other words, for each material with mat id, we need to provide such information for each temperature. 


### Strength Constants

#### Isotropic material

For isotropic material, the following five built-in failure criteria are available:

`failure_criterion` is 1: **Max principal stress criterion**

Two strength constants are needed:
- one for tensile strength ($X$) and
- one for compressive strength ($X^′$ ), arranged as $X$, $X^′$.

```none
1  2
X  X'
```

`failure_criterion` is 2: **Max principal strain criterion**

Two strength constants in terms of strains are needed:
- one for tensile strength ($X_\varepsilon$) and
- one for compressive strength ($X^′_{\varepsilon}$), arranged as $X_\varepsilon$, $X^′_\varepsilon$.

```none
2  2
X_e  X'_e
```

`failure_criterion` is 3: **Max shear stress (Tresca) criterion**

One strength constant is needed:
- shear strength constant ($S$).

```none
3  1
S
```

`failure_criterion` is 4: **Max shear strain criterion**

One strength constant in terms of strains is needed:
- shear strength constant in terms of strains ($S_\varepsilon$).

```none
4  1
S_e
```

`failure_criterion` is 5: **Mises criterion**

One strength constant ($X$) is needed.

```none
5  1
X
```


#### Non-isotropic material

For non-isotropic materials (transversely isotropic, orthotropic, or general anisotropic), the following five built-in failure criteria are available:

`failure_criterion` is 1: **Max stress criterion**

Nine strength constants are needed:
- tensile strengths ($X$, $Y$, $Z$) in three directions
- compressive strengths ($X^′$ , $Y^′$ , $Z^′$ ) in three directions
- shear strengths ($R$, $T$, $S$) in three principal planes

```none
1  9
X  Y  Z  X'  Y'  Z'  R  T  S
```

`failure_criterion` is 2: **Max strain criterion**

Nine strength constants in terms of strains are needed:
- tensile strengths ($X_\varepsilon$, $Y_\varepsilon$, $Z_\varepsilon$) in three directions
- compressive strengths ($X^′ _\varepsilon$, $Y^′_\varepsilon$, $Z^′_\varepsilon$) in three directions
- shear strengths ($R_\varepsilon$, $T_\varepsilon$, $S_\varepsilon$) in three principal planes

```none
2  9
X_e  Y_e  Z_e  X'_e  Y'_e  Z'_e  R_e  T_e  S_e
```

`failure_criterion` is 3: **Tsai-Hill criterion**

Six strength constants are needed:
- normal strengths in three directions
- shear strengths in three principal planes

```none
3  6
X  Y  Z  R  T  S
```

`failure_criterion` is 4: **Tsai-Wu criterion**

Nine strength constants are needed:
- tensile strengths (X, Y, Z) in three directions
- compressive strengths ($X^′$, $Y^′$, $Z^′$) in three directions
- shear strengths ($R$, $T$, $S$) in three principal planes

```none
4  9
X  Y  Z  X'  Y'  Z'  R  T  S
```

`failure_criterion` is 5: **Hashin criterion**

Six strength constants are needed:
- tensile strengths ($X$, $Y$) in two directions
- compressive strengths ($X^′$, $Y^′$) in two directions
- shear strengths ($R$, $S$) in two principal planes

```none
5  6
X  Y  X'  Y'  R  S
```


It is noted that for failure analysis, general anisotropic materials are also approximated using orthotropic materials due to limited number of strength constants.
In SwiftComp, both the tensile strengths and compressive strengths are expressed using positive numbers.
In other words, in the uniaxial compressive test along $y_{1}$ direction, $\sigma_{11} = -X^{\prime}$ when material fails. 


### Output type

After the material block for strength parameters, we need to provide the following line in the `*.glb` file containing one integer if `analysis` is not 9 or 10. 

```
id_1
```

This indicates whether the strength is expressed in terms of generalized stresses or generalized strains.
- If it is 0, the strength is expressed in terms of generalized stresses;
- If it is 1, the strength is expressed in terms of generalized strains. 

---

## Extra Inputs for Failure Envelope Analysis

For failure envelope analysis, we need to provide the following line in the `*.glb` file containing two integers if `analysis` is not 9 or 10. 

```
istr1  istr2
```

These indicate the two load directions that one would like to predict a failure envelope for.
The values could be 1, 2, 3, 4, ..., corresponding to the arrangement of the generalized stresses (if `id_1` is 0 ) or generalized strains (if `id_1` is 1 ).
For example for the 3D model, the stress/strain are arranged in the order of 11, 22, 33, 23, 13, 12.
If we want to draw a failure envelope in the plane $\sigma_{22}$ — $\sigma_{13}$, the input should be `2  5`. 

---

## Extra Inputs for Failure Index Analysis

For failure index analysis, this above line is not necessary.
Instead we need to provide the following line in the `*.glb` file containing $n$ real numbers with $n$ equal to the total number of generalized stresses or generalized strains. 

```
str_1  str_2  str_3  ...  str_n
```

These indicate the given loads used to compute the strength ratio and the failure index.
These values can be given in terms of generalized stresses or generalized strains depending on whether the required strength outputs are in generalized stresses ( `id_1` is 0 ) or generalized strains ( `id_1` is 1 ).
If `analysis` is 9 or 10, corresponding nodal displacements should be provided as the inputs instead as those described at the end of the previous section. 

---

Both input files, `input_file_name` and `input_file_name.glb`, should be ended with a blank line to avoid any possible incompatibility of different computer operating systems.
The input file can be given any name as long as the total number of the characters of the name including extension is not more than 256.
For the convenience of the user to identify mistakes in the input file, all the inputs are echoed in a file named `input_file_name.ech`.
Error messages are also written at the end of `input_file_name.ech` and on the output screen. 
