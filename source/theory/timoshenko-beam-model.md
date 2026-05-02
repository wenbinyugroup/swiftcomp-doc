# Timoshenko Beam Model

The kinematics of the Timoshenko beam model contains six displacement variables $( u _ { 1 } , u _ { 2 } , u _ { 3 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 3 } )$ with $u _ { 1 } , u _ { 2 } , u _ { 3 }$ describing displacements in three directions and $\theta _ { 1 } , \theta _ { 2 } , \theta _ { 3 }$ describing rotations about three directions and six strain variables including axial strain $\gamma _ { 1 1 }$ , transverse shear strains $\left( \gamma _ { 1 2 } , \gamma _ { 1 3 } \right)$ , twist rate $\kappa _ { 1 1 }$ , and curvatures $\left( \kappa _ { 1 2 } , \kappa _ { 1 3 } \right)$ . The strain-displacement relations are 

$$
\gamma_ {1 1} = \frac {\mathrm {d} u _ {1}}{\mathrm {d} x _ {1}}, \qquad \gamma_ {1 2} = - \theta_ {3} + \frac {\mathrm {d} u _ {2}}{\mathrm {d} x _ {1}}, \qquad \gamma_ {1 3} = \theta_ {2} + \frac {\mathrm {d} u _ {3}}{\mathrm {d} x _ {1}}
$$

$$
\kappa_ {1 1} = \frac {\mathrm {d} \theta_ {1}}{\mathrm {d} x _ {1}}, \quad \kappa_ {1 2} = \frac {\mathrm {d} \theta_ {2}}{\mathrm {d} x _ {1}}, \quad \kappa_ {1 3} = \frac {\mathrm {d} \theta_ {3}}{\mathrm {d} x _ {1}} \tag {22}
$$

The kinetics of the Timoshenko beam model contains six stress resultants $( F _ { 1 } , F _ { 2 } , F _ { 3 } , M _ { 1 } , M _ { 2 } , M _ { 3 } )$ with $F _ { 1 }$ denoting axial force, $F _ { 2 }$ and $F _ { 3 }$ denoting transverse shear forces, and $M _ { 1 } , M _ { 2 } , M _ { 3 }$ denoting bending moments about three directions. These kinetic variables are functions of $x _ { 1 }$ only and they 

are governed by the following six equations of equilibrium: 

$$
\frac {\mathrm {d} F _ {1}}{\mathrm {d} x _ {1}} + p _ {1} = 0
$$

$$
\frac {\mathrm {d} F _ {2}}{\mathrm {d} x _ {1}} + p _ {2} = 0
$$

$$
\frac {\mathrm {d} F _ {3}}{\mathrm {d} x _ {1}} + p _ {3} = 0
$$

$$
\frac {\mathrm {d} M _ {1}}{\mathrm {d} x _ {1}} + q _ {1} = 0 \tag {23}
$$

$$
\frac {d M _ {2}}{\mathrm {d} x _ {1}} - F _ {3} + q _ {2} = 0
$$

$$
\frac {d M _ {3}}{\mathrm {d} x _ {1}} + F _ {2} + q _ {3} = 0
$$

The constitutive relations of the Timoshenko beam model can be expressed using the following matrix equation: 

$$
\left\{ \begin{array}{l} F _ {1} \\ F _ {2} \\ F _ {3} \\ M _ {1} \\ M _ {2} \\ M _ {3} \end{array} \right\} = \left[ \begin{array}{c c c c c c} C _ {1 1} ^ {b} & C _ {1 2} ^ {b} & C _ {1 3} ^ {b} & C _ {1 4} ^ {b} & C _ {1 5} ^ {b} & C _ {1 6} ^ {b} \\ C _ {1 2} ^ {b} & C _ {2 2} ^ {b} & C _ {2 3} ^ {b} & C _ {2 4} ^ {b} & C _ {2 5} ^ {b} & C _ {2 6} ^ {b} \\ C _ {1 3} ^ {b} & C _ {2 3} ^ {b} & C _ {3 3} ^ {b} & C _ {3 4} ^ {b} & C _ {3 5} ^ {b} & C _ {3 6} ^ {b} \\ C _ {1 4} ^ {b} & C _ {2 4} ^ {b} & C _ {3 4} ^ {b} & C _ {4 4} ^ {b} & C _ {4 5} ^ {b} & C _ {4 6} ^ {b} \\ C _ {1 5} ^ {b} & C _ {2 5} ^ {b} & C _ {3 5} ^ {b} & C _ {4 5} ^ {b} & C _ {5 5} ^ {b} & C _ {5 6} ^ {b} \\ C _ {1 6} ^ {b} & C _ {2 6} ^ {b} & C _ {3 6} ^ {b} & C _ {4 6} ^ {b} & C _ {5 6} ^ {b} & C _ {6 6} ^ {b} \end{array} \right] \left\{ \begin{array}{l} \gamma_ {1 1} \\ \gamma_ {1 2} \\ \gamma_ {1 3} \\ \kappa_ {1 1} \\ \kappa_ {1 2} \\ \kappa_ {1 3} \end{array} \right\} \tag {24}
$$

This $6 \times 6$ matrix is called the beam stiffness matrix and its inverse is called the beam compliance matrix for the Timoshenko model. It is noted that $C _ { i j } ^ { b }$ $i = 1 , 2 , 3 , 4 ; j = 1 , 2 , 3 , 4$ ) in this stiffness matrix could be different from those in Eq. (20). 

Eqs. (22), (23), and (24) form a system of 18 equations to be solved along with appropriate boundary conditions for 18 unknowns (six displacement variables, six strain variables, and six stress resultants). Kinematics and kinetics remain the same no matter whether the structure is made of metals or composites and these equations have been implemented in many FEA codes which have beam elements. Only difference is that the beam stiffness matrix in Eq. (24) could be fully populated if the beam is made of composites. 

It is noted that although the Timoshenko model was originally developed based on a set of ad hoc assumptions including the cross-section being rigid in plane, remaining plane during deformation, and uniaxial stress assumption. However, such assumptions are not used in MSG to derive this model. Thus, the Timoshenko model here only refers to the model which has 18 field variables of $x _ { 1 }$ governed by the 18 equations in Eqs. (22), (23) and (24). 
