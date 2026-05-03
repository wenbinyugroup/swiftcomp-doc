# Material block


The next nmate blocks define the material properties. They are arranged as: 

mat id isotropy ntemp 

where mat id is the material type, and isotropy is an integer to indicate whether the material is isotropic (0), orthotropic (1), or general anisotropic (2). The integer ntemp is number of material property sets according to different temperature followed by ntemp blocks of real numbers: 

$T _ { i }$ $\rho$ 

const1 const2 .... 

where $\tau _ { i } ^ { \prime } , i = 1 , \dots , n t e m p$ is the temperature, $\rho$ is the density, and the rest are material constants the details of which will be given in the next section. For the convenience to compute secant values contained in thermal properties, $T _ { 1 }$ is used as the reference temperature and $T _ { i }$ must be arranged in an increasing fashion. 

If analysis=7 or $\delta$ , the material properties could be provided by time dependent functions. The first line of the block will become: 

$T _ { i }$ ρ time function nprony 

where time function is a character and nprony is an integer. If time function is $C$ , properties do not depend on time and nprony can be an arbitrary number and nprony is not used in the code. This line will be followed by material constants input in the same way as for other analysis options. If time function= $P$ or $T$ , nprony denotes the total number of property sets used to define the time dependent properties. If time function= $P$ , the time dependency is defined using the Prony series and nprony is number of Prony series terms plus 1 because the long term properties are also input in the first block. If time function=T, the time dependency is defined by a user defined time function with linear interpolation between adjacent time values. The material block followed by nprony sets of material properties arranged as 

$t _ { i }$ 

const1 const2 .... 

where $t _ { i }$ is a real number indicating the real time if time function= $T$ or the relaxation constants if time function= $P$ . If time function= $P$ , $t _ { 1 }$ can be arbitrary because it is followed by the long term properties and the corresponding $t _ { 1 }$ is not used in computing the time-dependent material properties. 

# 8.3 Conductivity

For conduction analysis (analysis=2), if the material is isotropic (isotropy= $\boldsymbol { \mathit { 0 } }$ ), there is only one constant specifying the conductivity arranged as: 

$k$ 

If isotropy=1 (orthotropic), there are three constants arranged as: 

$k _ { 1 1 } k _ { 2 2 } k _ { 3 3 }$ 

where $k _ { 1 1 } , k _ { 2 2 } , k _ { 3 3 }$ are conductivities along three principal directions. 

If isotropy= $\mathcal { Z }$ (general anisotropic), there are six constants arranged as: 

$k _ { 1 1 }$ $k _ { 1 2 }$ $k _ { 1 3 }$ 

$k _ { 2 2 }$ $k _ { 2 3 }$ 

$k _ { 3 3 }$ 

where $k _ { i j }$ are the components of the second-order conductivity tensor. 

# 8.4 Elastic Properties

For all other analyses, we need to first provide elastic properties. If isotropy= $\boldsymbol { \mathit { 0 } }$ , there are two constants arranged as: 

E ν 

where $E$ is the Young’s modulus, $\nu$ is the Poisson’s ratio. Elasticity theory restricts that Poisson’s ratio must be greater than -1.0 and less than 0.5 for linear, elastic, isotropic materials, although SwiftCompTM allows users to input values that are very close to those limits. 

If isotropy=1, there are nine constants arranged as: 

$E _ { 1 }$ $E _ { 2 }$ $E _ { 3 }$ 

$G _ { 1 2 } ~ G _ { 1 3 } ~ G _ { 2 3 }$ 

ν12 ν13 ν23 

including Young’s moduli ( $E _ { 1 }$ , $E _ { 2 }$ , and $E _ { 3 }$ ), shear moduli ( $G _ { 1 2 }$ , $G _ { 1 3 }$ , and $G _ { 2 3 }$ ), and Poisson’s ratios ( $\nu _ { 1 2 }$ , $\nu _ { 1 3 }$ , and $\nu _ { 2 3 }$ ). The convention of values is such that these values will be used to form the Hooke’s law for the orthotropic material in Eq. (6). 

If isotropy=2 , there are 21 constants arranged as: 

$C _ { 1 1 }$ $C _ { 1 2 }$ $C _ { 1 3 }$ C14 C15 C16 

These values are defined using the Hooke’s law given in Eq. (3). For orthotropic and general anisotropic materials, SwiftCompTM does not check the validity of the material inputs and it is the user’s responsibility to make sure that the material properties satisfy the positive definiteness requirement of the stiffness matrix and compliance matrix found in a typical textbook on mechanics 

of composite materials. 

# 8.5 CTE and Specific Heat

For thermally coupled analysis (analysis=1, 4, $\boldsymbol { \it 6 }$ ), if isotropy= $\boldsymbol { \mathit { 0 } }$ , there are two constants arranged as: 

$\alpha$ $c _ { v }$ 

where $\alpha$ is the CTE and $c _ { v }$ is the specific heat. 

If isotropy=1, there are four constants arranged as: 

$\alpha _ { 1 1 }$ α22 α33 $c _ { v }$ 

where $\alpha _ { 1 1 } , \alpha _ { 2 2 } , \alpha _ { 3 3 }$ are the CTEs along three principal directions. 

If isotropy=2, there are seven constants arranged as: 

α11 α22 α33 2α23 2α13 2α12 $c _ { v }$ 

where $\alpha _ { i j }$ are the components of the second-order CTE tensor. 

# 8.6 Piezoelectric, Dielectric, and Pyroelectric Coefficients

If analysis=3,4,5,6, we then need to provide 18 piezoelectric coefficients arranged as: 

e11 e12 e13 e14 e15 e16 

e21 e22 e23 e24 e25 e26 

e31 e32 e33 e34 e35 e36 

The piezoelectric coefficients should be followed by dielectric properties. If isotropy=0, there is one constant for dielectric coefficient arranged as: 

$k$ 

If isotropy=1, there are three constants arranged as: 

$k _ { 1 1 } k _ { 2 2 } k _ { 3 3 }$ 

where $k _ { 1 1 } , k _ { 2 2 } , k _ { 3 3 }$ are the dielectric coefficients along three principal directions. 

If isotropy=2, there are six constants arranged as: 

k11 k12 k13 

$k _ { 2 2 }$ $k _ { 2 3 }$ 

where $k _ { i j }$ denotes the second-order dielectric tensor. 

If analysis=4,6, the above data should be followed by three pyroelectric coefficients arranged as: 

$p _ { 1 }$ p2 p3 

# 8.7 Piezomagnetic Coefficients, Magnetic Permeability, Electromagnetic and Pyromagnetic Coefficients

To carry out coupled piezoelectromagnetic analysis (analysis= ${ 5 , 6 }$ ), we then need to provide another 18 piezomagnetic coefficients arranged as: 

```txt
q11 q12 q13 q14 q15 q16   
q21 q22 q23 q24 q25 q26   
q31 q32 q33 q34 q35 q36 
```

The piezomagnetic coefficients should be followed by magnetic permeability and electromagnetic coefficients. If isotropy=0, there are two constants arranged as: 

$\mu$ a 

with $\mu$ as the magnetic permeability, and $a$ as the electromagnetic coefficient. 

If isotropy=1, there are six constants arranged as: 

$\mu_{11}$ $\mu_{22}$ $\mu_{33}$ $a_{11} a_{22} a_{33}$ 

where $\mu _ { 1 1 } , \mu _ { 2 2 } , \mu _ { 3 3 }$ are the magnetic permeability along three principal directions, and $a _ { 1 1 } , a _ { 2 2 } , a _ { 3 3 }$ are the electromagnetic coefficients along three principal directions. 

If isotropy= $\mathcal { Z }$ , there are 12 constants arranged as: 

$\mu_{11}$ $\mu_{12}$ $\mu_{13}$ $\mu_{22}$ $\mu_{23}$ $\mu_{33}$ $a_{11}$ $a_{12}$ $a_{13}$ $a_{22}$ $a_{23}$ $a_{33}$ 

where $\mu _ { i j }$ denotes the second-order magnetic permeability tensor and $a _ { i j }$ denotes the second-order electromagnetic coupling tensor. 

If analysis= $\it 6$ , the above data should be followed by three pyromagnetic coefficients arranged as: 

```txt
m1 m2 m3 
```

To clarify the order of input material properties, if analysis= $\it 6$ and isotropy=2, the material inputs should be arranged: 

$T_{i}$ $\rho$ $C_{11}$ $C_{12}$ C13 C14 C15 C16 $C_{22}$ C23 C24 C25 C26 $C_{33}$ C34 C35 C36 $C_{44}$ C45 C46 $C_{55}$ C56 $C_{66}$ 

<table><tr><td>α11</td><td>α22</td><td>α33</td><td>2α23</td><td>2α13</td><td>2α12</td><td>cv</td></tr><tr><td>e11</td><td>e12</td><td>e13</td><td>e14</td><td>e15</td><td>e16</td><td></td></tr><tr><td>e21</td><td>e22</td><td>e23</td><td>e24</td><td>e25</td><td>e26</td><td></td></tr><tr><td>e31</td><td>e32</td><td>e33</td><td>e34</td><td>e35</td><td>e36</td><td></td></tr><tr><td>k11</td><td>k12</td><td>k13</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>k22</td><td>k23</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>k33</td><td></td><td></td><td></td><td></td></tr><tr><td>p1</td><td>p2</td><td>p3</td><td></td><td></td><td></td><td></td></tr><tr><td>q11</td><td>q12</td><td>q13</td><td>q14</td><td>q15</td><td>q16</td><td></td></tr><tr><td>q21</td><td>q22</td><td>q23</td><td>q24</td><td>q25</td><td>q26</td><td></td></tr><tr><td>q31</td><td>q32</td><td>q33</td><td>q34</td><td>q35</td><td>q36</td><td></td></tr><tr><td>μ11</td><td>μ12</td><td>μ13</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>μ22</td><td>μ23</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>μ33</td><td></td><td></td><td></td><td></td></tr><tr><td>a11</td><td>a12</td><td>a13</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>a22</td><td>a23</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>a33</td><td></td><td></td><td></td><td></td></tr><tr><td>m1</td><td>m2</td><td>m3</td><td></td><td></td><td></td><td></td></tr></table>

The material constants could be expressed either in the problem coordinate system $y _ { 1 } , y _ { 2 } , y _ { 3 }$ or in the material coordinate system. However, it is usually more convenient and simpler to provide these constants in the material coordinate system. If it is expressed in the material coordinate system, SwiftCompTM will perform the necessary transformations. The input quantities should be properly scaled as discussed previously for multiphysics modeling. It is also emphasized that if the users uses an arrangement of stresses and strains different from what SwiftCompTM uses, proper re-arrangement of the material properties is needed. 
