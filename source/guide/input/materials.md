# Material block

The next `nmate` blocks define the material properties.
They are arranged as: 

```
mat_id  isotropy  ntemp 
```

:`mat_id`:
    Integer.
    Material ID.

:`isotropy`:
    Integer.
    Material isotropy.
    - 0: isotropic
    - 1: orthotropic
    - 2: general anisotropic

:`ntemp`:
    Integer.
    Number of sets of material properties at different temperatures.


Next are `ntemp` blocks of material properties: 

```
T_i  rho

{property blocks}
```

:`T_i`:
    Real.
    Temperature.
    `i` is 1 to `ntemp`.

:`rho`:
    Real.
    Density.

:`{property blocks}`:
    Material property constants.
    Given below.

```{note}
For the convenience to compute secant values contained in thermal properties, `T_1` is used as the reference temperature and `T_i` must be arranged in an ascending order. 
```



## If `analysis` is 7 or 8

The material properties could be provided by time dependent functions.
The first line of the block will become: 

```
T_i  rho  time_function  nprony
t_j
{property blocks}
```

:`time_function`:
    Character.
    Type of the time function.
    - C: Properties do not depend on time. `nprony` can be an arbitrary number and is not used.
    - P: Time dependency is defined using the Prony series.
    - T: Time dependency is defined by a user-defined time function with linear interpolation between adjacent time values.

:`nprony`:
    Integer.
    Total number of property sets used to define the time dependent properties.
    If `time_function` is `P`, this is the number of Prony series terms plus 1 because the long term properties are also input in the first block.

The material block followed by `nprony` sets of material properties arranged as 

:`t_j`:
    Real.
    `j` is 1 to `nprony`.
    If `time_function` is `P`, this is the relaxation constants. `t_1` can be arbitrary because it is followed by the long term properties and is not used in computing the time-dependent material properties.
    If `time_function` is `T`, this is the real time.



## Properties

## Elastic

For analyses other than conduction (`analysis` is not 2), we need to first provide elastic properties.

### If `isotropy` is 0

There are two constants arranged as: 
```
E  nu 
```

:`E`:
    Real.
    Young's modulus.

:`nu`:
    Real.
    Poisson's ratio.
    Elasticity theory restricts that Poisson’s ratio must be greater than -1.0 and less than 0.5 for linear, elastic, isotropic materials, although SwiftComp allows users to input values that are very close to those limits.


### If `isotropy` is 1

There are nine constants arranged as: 

```
  E_1    E_2    E_3 
  G_12   G_13   G_23
 nu_12  nu_13  nu_23
```

including Young’s moduli ( $E _ { 1 }$ , $E _ { 2 }$ , and $E _ { 3 }$ ), shear moduli ( $G _ { 1 2 }$ , $G _ { 1 3 }$ , and $G _ { 2 3 }$ ), and Poisson’s ratios ( $\nu _ { 1 2 }$ , $\nu _ { 1 3 }$ , and $\nu _ { 2 3 }$ ).
The convention of values is such that these values will be used to form the Hooke’s law for the orthotropic material in Eq. (6). 

### If `isotropy` is 2

There are 21 constants arranged as: 

```
C_11  C_12  C_13  C_14  C_15  C_16 
      C_22  C_23  C_24  C_25  C_26 
            C_33  C_34  C_35  C_36 
                  C_44  C_45  C_46 
                        C_55  C_56 
                              C_66 
```

These values are defined using the Hooke’s law given in Eq. (3). For orthotropic and general anisotropic materials, SwiftComp does not check the validity of the material inputs and it is the user’s responsibility to make sure that the material properties satisfy the positive definiteness requirement of the stiffness matrix and compliance matrix found in a typical textbook on mechanics of composite materials. 



## Conductivity

For conduction analysis (`analysis` is 2)

### If the material is isotropic (`isotropy` is 0)

There is only one constant specifying the conductivity arranged as: 
```
k
``` 

### If `isotropy` is 1 (orthotropic)

There are three constants arranged as: 

```
$k _ { 1 1 } k _ { 2 2 } k _ { 3 3 }$ 
```

where $k _ { 1 1 } , k _ { 2 2 } , k _ { 3 3 }$ are conductivities along three principal directions. 

### If `isotropy` is 2 (general anisotropic)

There are six constants arranged as: 

```
$k _ { 1 1 }$ $k _ { 1 2 }$ $k _ { 1 3 }$ 
$k _ { 2 2 }$ $k _ { 2 3 }$ 
$k _ { 3 3 }$ 
```

where $k _ { i j }$ are the components of the second-order conductivity tensor. 


## CTE and Specific Heat

For thermally coupled analysis (`analysis` is 1, 4, or 6)

### If `isotropy` is 0

There are two constants arranged as: 

```
$\alpha$ $c _ { v }$ 
```

where $\alpha$ is the CTE and $c _ { v }$ is the specific heat. 

### If `isotropy` is 1

There are four constants arranged as: 

```
$\alpha _ { 1 1 }$ α22 α33 $c _ { v }$ 
```

where $\alpha _ { 1 1 } , \alpha _ { 2 2 } , \alpha _ { 3 3 }$ are the CTEs along three principal directions. 

### If `isotropy` is 2

There are seven constants arranged as: 

```
α11 α22 α33 2α23 2α13 2α12 $c _ { v }$ 
```

where $\alpha _ { i j }$ are the components of the second-order CTE tensor. 



## Piezoelectric, Dielectric, and Pyroelectric Coefficients

If `analysis` is 3, 4, 5, or 6, we then need to provide 18 piezoelectric coefficients arranged as: 

```
e11 e12 e13 e14 e15 e16 
e21 e22 e23 e24 e25 e26 
e31 e32 e33 e34 e35 e36 
```

The piezoelectric coefficients should be followed by dielectric properties.

### If `isotropy` is 0

There is one constant for dielectric coefficient arranged as: 

```
k
```

### If `isotropy` is 1

There are three constants arranged as: 

```
k _ { 1 1 } k _ { 2 2 } k _ { 3 3 }
```

where $k _ { 1 1 } , k _ { 2 2 } , k _ { 3 3 }$ are the dielectric coefficients along three principal directions. 

### If `isotropy` is 2

There are six constants arranged as: 

```
k11 k12 k13 
$k _ { 2 2 }$ $k _ { 2 3 }$ 
```

where $k _ { i j }$ denotes the second-order dielectric tensor. 


If `analysis` is 4 or 6, the above data should be followed by three pyroelectric coefficients arranged as:

```
$p _ { 1 }$ p2 p3 
```



## Piezomagnetic Coefficients, Magnetic Permeability, Electromagnetic and Pyromagnetic Coefficients

To carry out coupled piezoelectromagnetic analysis (`analysis`is 5 or 6), we then need to provide another 18 piezomagnetic coefficients arranged as: 

```
q11 q12 q13 q14 q15 q16   
q21 q22 q23 q24 q25 q26   
q31 q32 q33 q34 q35 q36 
```

The piezomagnetic coefficients should be followed by magnetic permeability and electromagnetic coefficients.

**If `isotropy` is 0**, there are two constants arranged as: 

```
$\mu$ a 
```

with $\mu$ as the magnetic permeability, and $a$ as the electromagnetic coefficient. 

**If `isotropy` is 1**, there are six constants arranged as: 

```
$\mu_{11}$ $\mu_{22}$ $\mu_{33}$ $a_{11} a_{22} a_{33}$ 
```

where $\mu _ { 1 1 } , \mu _ { 2 2 } , \mu _ { 3 3 }$ are the magnetic permeability along three principal directions, and $a _ { 1 1 } , a _ { 2 2 } , a _ { 3 3 }$ are the electromagnetic coefficients along three principal directions. 

**If `isotropy` is 2**, there are 12 constants arranged as: 

```
$\mu_{11}$ $\mu_{12}$ $\mu_{13}$ $\mu_{22}$ $\mu_{23}$ $\mu_{33}$ $a_{11}$ $a_{12}$ $a_{13}$ $a_{22}$ $a_{23}$ $a_{33}$ 
```

where $\mu _ { i j }$ denotes the second-order magnetic permeability tensor and $a _ { i j }$ denotes the second-order electromagnetic coupling tensor. 

If `analysis` is 6, the above data should be followed by three pyromagnetic coefficients arranged as: 

```
m1 m2 m3 
```

To clarify the order of input material properties, if `analysis` is 6 and `isotropy` is 2, the material inputs should be arranged: 

```
Ti  rho

C_11  C_12  C_13  C_14  C_15  C_16
      C_22  C_23  C_24  C_25  C_26
            C_33  C_34  C_35  C_36
                  C_44  C_45  C_46
                        C_55  C_56
                              C_66

alpha_11  alpha_22  alpha_33  2alpha_23  2alpha_13  2alpha_12  c_v

e_11  e_12  e_13  e_14  e_15  e_16
e_21  e_22  e_23  e_24  e_25  e_26
e_31  e_32  e_33  e_34  e_35  e_36

k_11  k_12  k_13
      k_22  k_23
            k_33

p_1  p_2  p_3

q_11  q_12  q_13  q_14  q_15  q_16
q_21  q_22  q_23  q_24  q_25  q_26
q_31  q_32  q_33  q_34  q_35  q_36

mu_11  mu_12  mu_13
       mu_22  mu_23
              mu_33

a_11  a_12  a_13
      a_22  a_23
            a_33

m_1  m_2  m_3
```


```{note}
The material constants could be expressed either in the problem coordinate system $y _ { 1 } , y _ { 2 } , y _ { 3 }$ or in the material coordinate system.
However, it is usually more convenient and simpler to provide these constants in the material coordinate system.
If it is expressed in the material coordinate system, SwiftComp will perform the necessary transformations.
The input quantities should be properly scaled as discussed previously for multiphysics modeling.
It is also emphasized that if the users uses an arrangement of stresses and strains different from what SwiftComp uses, proper re-arrangement of the material properties is needed. 
```
