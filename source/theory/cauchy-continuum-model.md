# Cauchy Continuum Model

The kinematics of the Cauchy continuum model contains three displacements $( u _ { 1 } , u _ { 2 } , u _ { 3 } )$ and six strains $( \varepsilon _ { 1 1 } , \varepsilon _ { 2 2 } , \varepsilon _ { 3 3 } , \varepsilon _ { 2 3 } , \varepsilon _ { 1 3 } , \varepsilon _ { 1 2 } )$ . The strain-displacement relations are given as 

$$
\varepsilon_ {1 1} = \frac {\partial u _ {1}}{\partial x _ {1}}, \quad \varepsilon_ {2 2} = \frac {\partial u _ {2}}{\partial x _ {2}}, \quad \varepsilon_ {3 3} = \frac {\partial u _ {3}}{\partial x _ {3}} \tag {1}
$$

$$
2 \varepsilon_ {2 3} = \frac {\partial u _ {2}}{\partial x _ {3}} + \frac {\partial u _ {3}}{\partial x _ {2}}, \qquad 2 \varepsilon_ {1 3} = \frac {\partial u _ {1}}{\partial x _ {3}} + \frac {\partial u _ {3}}{\partial x _ {1}}, \qquad 2 \varepsilon_ {1 2} = \frac {\partial u _ {1}}{\partial x _ {2}} + \frac {\partial u _ {2}}{\partial x _ {1}}
$$

The kinetics of the Cauchy continuum model is described using six stresses $\left( \sigma _ { 1 1 } , \sigma _ { 2 2 } , \sigma _ { 3 3 } , \sigma _ { 2 3 } , \sigma _ { 1 3 } , \sigma _ { 1 2 } \right)$ which are functions of $x _ { 1 } , x _ { 2 } , x _ { 3 }$ . These stresses are governed by the following equations of equilibrium: 

$$
\frac {\partial \sigma_ {1 1}}{\partial x _ {1}} + \frac {\partial \sigma_ {1 2}}{\partial x _ {2}} + \frac {\partial \sigma_ {1 3}}{\partial x _ {3}} + f _ {1} = 0
$$

$$
\frac {\partial \sigma_ {1 2}}{\partial x _ {1}} + \frac {\partial \sigma_ {2 2}}{\partial x _ {2}} + \frac {\partial \sigma_ {2 3}}{\partial x _ {3}} + f _ {2} = 0 \tag {2}
$$

$$
\frac {\partial \sigma_ {1 3}}{\partial x _ {1}} + \frac {\partial \sigma_ {2 3}}{\partial x _ {2}} + \frac {\partial \sigma_ {3 3}}{\partial x _ {3}} + f _ {3} = 0
$$

where $f _ { 1 } , f _ { 2 } , f _ { 3 }$ are distributed body forces per unit volume. The constitutive relations of the Cauchy continuum model for the linear elastic behavior are described using the Hooke’s law as 

$$
\left\{ \begin{array}{l} \sigma_ {1 1} \\ \sigma_ {2 2} \\ \sigma_ {3 3} \\ \sigma_ {2 3} \\ \sigma_ {1 3} \\ \sigma_ {1 2} \end{array} \right\} = \left[ \begin{array}{c c c c c c} C _ {1 1} & C _ {1 2} & C _ {1 3} & C _ {1 4} & C _ {1 5} & C _ {1 6} \\ C _ {1 2} & C _ {2 2} & C _ {2 3} & C _ {2 4} & C _ {2 5} & C _ {2 6} \\ C _ {1 3} & C _ {2 3} & C _ {3 3} & C _ {3 4} & C _ {3 5} & C _ {3 6} \\ C _ {1 4} & C _ {2 4} & C _ {3 4} & C _ {4 4} & C _ {4 5} & C _ {4 6} \\ C _ {1 5} & C _ {2 5} & C _ {3 5} & C _ {4 5} & C _ {5 5} & C _ {5 6} \\ C _ {1 6} & C _ {2 6} & C _ {3 6} & C _ {4 6} & C _ {5 6} & C _ {6 6} \end{array} \right] \left\{ \begin{array}{l} \varepsilon_ {1 1} \\ \varepsilon_ {2 2} \\ \varepsilon_ {3 3} \\ 2 \varepsilon_ {2 3} \\ 2 \varepsilon_ {1 3} \\ 2 \varepsilon_ {1 2} \end{array} \right\} \tag {3}
$$

The $6 \times 6$ matrix $C _ { i j }$ is called the stiffness matrix and its inverse is called the compliance matrix. Note that material properties are usually provided in the so-called material coordinate system which implies that we need to write constitutive relations in the material coordinate system first. However, the kinematics and kinetics are usually formulated in the global coordinate system. A proper transformation according to the tensorial transformation laws is needed to transfer the constitutive relations into the global coordinate system. 

For isotropic materials, the constitutive relations can be expressed in terms of the Young’s modulus $E$ and Poisson’s ratio $\nu$ as 

$$
\left\{ \begin{array}{l} \varepsilon_ {1 1} \\ \varepsilon_ {2 2} \\ \varepsilon_ {3 3} \\ 2 \varepsilon_ {2 3} \\ 2 \varepsilon_ {1 3} \\ 2 \varepsilon_ {1 2} \end{array} \right\} = \left[ \begin{array}{c c c c c c} \frac {1}{E} & - \frac {\nu}{E} & - \frac {\nu}{E} & 0 & 0 & 0 \\ - \frac {\nu}{E} & \frac {1}{E} & - \frac {\nu}{E} & 0 & 0 & 0 \\ - \frac {\nu}{E} & - \frac {\nu}{E} & \frac {1}{E} & 0 & 0 & 0 \\ 0 & 0 & 0 & \frac {2 (1 + \nu)}{E} & 0 & 0 \\ 0 & 0 & 0 & 0 & \frac {2 (1 + \nu)}{E} & 0 \\ 0 & 0 & 0 & 0 & 0 & \frac {2 (1 + \nu)}{E} \end{array} \right] \left\{ \begin{array}{l} \sigma_ {1 1} \\ \sigma_ {2 2} \\ \sigma_ {3 3} \\ \sigma_ {2 3} \\ \sigma_ {1 3} \\ \sigma_ {1 2} \end{array} \right\} \tag {4}
$$

which can be inverted to obtain the same expression as Eq. (3) with 

$$
C _ {1 1} = C _ {2 2} = C _ {3 3} = \frac {E (1 - \nu)}{(1 + \nu) (1 - 2 \nu)}
$$

$$
C _ {1 2} = C _ {1 3} = C _ {2 3} = \frac {E \nu}{(1 + \nu) (1 - 2 \nu)}
$$

$$
C _ {4 4} = C _ {5 5} = C _ {6 6} = \frac {E}{2 (1 + \nu)} \tag {5}
$$

and all other terms in the stiffness matrix of Eq. (3) are zero. 

For orthotropic materials, the constitutive relations can be expressed as 

$$
\left\{ \begin{array}{l} \varepsilon_ {1 1} \\ \varepsilon_ {2 2} \\ \varepsilon_ {3 3} \\ 2 \varepsilon_ {2 3} \\ 2 \varepsilon_ {1 3} \\ 2 \varepsilon_ {1 2} \end{array} \right\} = \left[ \begin{array}{c c c c c c} \frac {1}{E _ {1}} & - \frac {\nu_ {2 1}}{E _ {2}} & - \frac {\nu_ {3 1}}{E _ {3}} & 0 & 0 & 0 \\ - \frac {\nu_ {1 2}}{E _ {1}} & \frac {1}{E _ {2}} & - \frac {\nu_ {3 2}}{E _ {3}} & 0 & 0 & 0 \\ - \frac {\nu_ {1 3}}{E _ {1}} & - \frac {\nu_ {2 3}}{E _ {2}} & \frac {1}{E _ {3}} & 0 & 0 & 0 \\ 0 & 0 & 0 & \frac {1}{G _ {2 3}} & 0 & 0 \\ 0 & 0 & 0 & 0 & \frac {1}{G _ {1 3}} & 0 \\ 0 & 0 & 0 & 0 & 0 & \frac {1}{G _ {1 2}} \end{array} \right] \left\{ \begin{array}{l} \sigma_ {1 1} \\ \sigma_ {2 2} \\ \sigma_ {3 3} \\ \sigma_ {2 3} \\ \sigma_ {1 3} \\ \sigma_ {1 2} \end{array} \right\} \tag {6}
$$

where $E _ { 1 } , E _ { 2 } , E _ { 3 }$ are Young’s moduli in three directions, $\mathrm { \Delta } G _ { 1 2 } , G _ { 1 3 } , G _ { 2 3 }$ are shear moduli in three directions, $\nu _ { 1 2 } , \nu _ { 1 3 } , \nu _ { 2 3 }$ and $\nu _ { 2 1 } , \nu _ { 3 1 } , \nu _ { 3 2 }$ are two set of Poisson’s ratios. Usually only $\nu _ { 1 2 } , \nu _ { 1 3 } , \nu _ { 2 3 }$ are given and the other Poisson’s ratios are calculated as 

$$
\nu_ {2 1} = \nu_ {1 2} E _ {2} / E _ {1}, \qquad \nu_ {3 1} = \nu_ {1 3} E _ {3} / E _ {1}, \qquad \nu_ {3 2} = \nu_ {2 3} E _ {3} / E _ {2}
$$

due to the symmetry of the compliance matrix. 

Eq. (6) can be inverted to obtain the same expression as Eq. (3) with 

$$
C _ {1 1} = E _ {1} \left(1 - \nu_ {2 3} \nu_ {3 2}\right) / \Delta , \quad C _ {1 2} = E _ {2} \left(\nu_ {1 2} + \nu_ {1 3} \nu_ {3 2}\right) / \Delta , \quad C _ {1 3} = E _ {3} \left(\nu_ {1 3} + \nu_ {1 2} \nu_ {2 3}\right) / \Delta ,
$$

$$
C _ {2 2} = E _ {2} (1 - \nu_ {1 3} \nu_ {3 1}) / \Delta , \qquad C _ {2 3} = E _ {3} (\nu_ {2 3} + \nu_ {1 3} \nu_ {2 1}) / \Delta , \qquad C _ {3 3} = E _ {3} (1 - \nu_ {1 2} \nu_ {2 1}) / \Delta ,
$$

$$
C _ {4 4} = G _ {2 3}, \quad C _ {5 5} = G _ {1 3}, \quad C _ {6 6} = G _ {1 2}
$$

with 

$$
\Delta = 1 - \nu_ {1 2} \nu_ {2 1} - \nu_ {2 3} \nu_ {3 2} - \nu_ {1 3} \nu_ {3 1} - 2 \nu_ {2 1} \nu_ {1 3} \nu_ {3 2}
$$

and all other terms in Eq. (3) are zero. 

Eqs. (1), (2), and (3) form a system of 15 equations underpinning the Cauchy continuum model to be solved along with appropriate boundary conditions for 15 unknowns (three displacements, six strains, and six stresses). This model has been implemented in many FEA codes which have 3D solid elements. Kinematics and kinetics remain the same no matter whether the structure is made of metals or composites. Only the constitutive relations will be different, see Eq. (3) for general anisotropic materials, Eq. (4) for isotropic materials, and Eq. (6) for orthotropic materials. 

It is worthy to point out that there are two degenerated version of the 3D Cauchy continuum model: plane stress model and plane strain model. Plane stress model assumes that all the outof-plane stresses vanish. For example, if the plane stress model is formulated in the $x _ { 1 } - x _ { 2 }$ plane, we assume $\sigma _ { 1 3 } = \sigma _ { 2 3 } = \sigma _ { 3 3 } = 0$ . Plane strain model assumes that all the out-of-plane strains vanish. For example, if the plane strain model is formulated in the $x _ { 1 } - x _ { 2 }$ plane, we assume $\varepsilon _ { 1 3 } = \varepsilon _ { 2 3 } = \varepsilon _ { 3 3 } = 0$ . The kinematics of the plane stress model and the plane strain model remain the same as 

$$
\varepsilon_ {1 1} = \frac {\partial u _ {1}}{\partial x _ {1}}, \quad \varepsilon_ {2 2} = \frac {\partial u _ {2}}{\partial x _ {2}}, \quad 2 \varepsilon_ {1 2} = \frac {\partial u _ {1}}{\partial x _ {2}} + \frac {\partial u _ {2}}{\partial x _ {1}} \tag {7}
$$

The kinetics of the plane stress model and the plane strain model remain the same as 

$$
\frac {\partial \sigma_ {1 1}}{\partial x _ {1}} + \frac {\partial \sigma_ {1 2}}{\partial x _ {2}} + f _ {1} = 0 \tag {8}
$$

$$
\frac {\partial \sigma_ {1 2}}{\partial x _ {1}} + \frac {\partial \sigma_ {2 2}}{\partial x _ {2}} + f _ {2} = 0
$$

The constitutive relations of the plane strain model are 

$$
\left\{ \begin{array}{l} \sigma_ {1 1} \\ \sigma_ {2 2} \\ \sigma_ {1 2} \end{array} \right\} = \left[ \begin{array}{c c c} C _ {1 1} & C _ {1 2} & C _ {1 6} \\ C _ {1 2} & C _ {2 2} & C _ {2 6} \\ C _ {1 6} & C _ {2 6} & C _ {6 6} \end{array} \right] \left\{ \begin{array}{l} \varepsilon_ {1 1} \\ \varepsilon_ {2 2} \\ 2 \varepsilon_ {1 2} \end{array} \right\} \tag {9}
$$

The constitutive relations of the plane stress model are 

$$
\left\{ \begin{array}{l} \sigma_ {1 1} \\ \sigma_ {2 2} \\ \sigma_ {1 2} \end{array} \right\} = \left[ \begin{array}{c c c} Q _ {1 1} & Q _ {1 2} & Q _ {1 6} \\ Q _ {1 2} & Q _ {2 2} & Q _ {2 6} \\ Q _ {1 6} & Q _ {2 6} & Q _ {6 6} \end{array} \right] \left\{ \begin{array}{l} \varepsilon_ {1 1} \\ \varepsilon_ {2 2} \\ 2 \varepsilon_ {1 2} \end{array} \right\} \tag {10}
$$

where $Q _ { i j }$ are the so-called plane-stress-reduced stiffnesses which are different from $C _ { i j }$ . They are computed by substituting $\sigma _ { 1 3 } = \sigma _ { 2 3 } = \sigma _ { 3 3 } = 0$ into Eq. (3) to obtain $\varepsilon _ { 3 3 } , 2 \varepsilon _ { 2 3 } , 2 \varepsilon _ { 1 3 }$ in terms of $\varepsilon _ { 1 1 } , \varepsilon _ { 2 2 } , 2 \varepsilon _ { 1 2 }$ . Then substituting these relations back into Eq. (3) to obtain the relationship in Eq. (10). For isotropic materials, we have 

$$
Q _ {1 1} = Q _ {2 2} = \frac {E}{1 - \nu^ {2}}, \qquad Q _ {1 2} = \frac {E \nu}{1 - \nu^ {2}}, \qquad Q _ {1 6} = Q _ {2 6} = 0, \qquad Q _ {6 6} = \frac {E}{2 (1 + \nu)}
$$

which are different from $C _ { i j }$ for isotropic materials given in Eq. (5). For anisotropic materials, $Q _ { i j }$ expressions can be found in a typical textbook on mechanics of composite materials. 
