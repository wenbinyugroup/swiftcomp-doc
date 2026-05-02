# Euler-Bernoulli Beam Model

The kinematics of the Euler-Bernoulli beam model contains four displacement variables $u _ { 1 } , u _ { 2 } , u _ { 3 } , \theta _ { 1 }$ with $u _ { 1 } , u _ { 2 } , u _ { 3 }$ describing displacements in three directions and $\theta _ { 1 }$ describing the twist angle, and four strain variables including axial strain $\gamma _ { 1 1 }$ , twist rate $\kappa _ { 1 1 }$ , and curvatures $\kappa _ { 1 2 } , \kappa _ { 1 3 }$ around $x _ { 2 }$ and $x _ { 3 }$ , respectively. The strain-displacement relations are 

$$
\gamma_ {1 1} = \frac {\mathrm {d} u _ {1}}{\mathrm {d} x _ {1}}, \quad \kappa_ {1 1} = \frac {\mathrm {d} \theta_ {1}}{\mathrm {d} x _ {1}}, \quad \kappa_ {1 2} = - \frac {\mathrm {d} ^ {2} u _ {3}}{\mathrm {d} x _ {1} ^ {2}}, \quad \kappa_ {1 3} = \frac {\mathrm {d} ^ {2} u _ {2}}{\mathrm {d} x _ {1} ^ {2}} \tag {18}
$$

The kinetics of the Euler-Bernoulli beam model contains four stress resultants $\left( F _ { 1 } , M _ { 1 } , M _ { 2 } , M _ { 3 } \right)$ with $F _ { 1 }$ denoting axial force and $M _ { 1 } , M _ { 2 } , M _ { 3 }$ denoting moments about three directions. These kinetic variables are governed by the following four equations of equilibrium: 

$$
\frac {\mathrm {d} F _ {1}}{\mathrm {d} x _ {1}} + p _ {1} = 0
$$

$$
\frac {\mathrm {d} M _ {1}}{\mathrm {d} x _ {1}} + q _ {1} = 0
$$

$$
\frac {d ^ {2} M _ {2}}{\mathrm {d} x _ {1} ^ {2}} + p _ {3} + \frac {\mathrm {d} q _ {2}}{\mathrm {d} x _ {1}} = 0 \tag {19}
$$

$$
\frac {d ^ {2} M _ {3}}{\mathrm {d} x _ {1} ^ {2}} - p _ {2} + \frac {\mathrm {d} q _ {3}}{\mathrm {d} x _ {1}} = 0
$$

where $p _ { 1 } , p _ { 2 } , p _ { 3 }$ are equivalent forces and $q _ { 1 } , q _ { 2 } , q _ { 3 }$ are equivalent moments in three directions, distributed along the reference line. 

The constitutive relations of the Euler-Bernoulli beam model can be expressed using the following matrix equation: 

$$
\left\{ \begin{array}{l} F _ {1} \\ M _ {1} \\ M _ {2} \\ M _ {3} \end{array} \right\} = \left[ \begin{array}{c c c c} C _ {1 1} ^ {b} & C _ {1 2} ^ {b} & C _ {1 3} ^ {b} & C _ {1 4} ^ {b} \\ C _ {1 2} ^ {b} & C _ {2 2} ^ {b} & C _ {2 3} ^ {b} & C _ {2 4} ^ {b} \\ C _ {1 3} ^ {b} & C _ {2 3} ^ {b} & C _ {3 3} ^ {b} & C _ {3 4} ^ {b} \\ C _ {1 4} ^ {b} & C _ {2 4} ^ {b} & C _ {3 4} ^ {b} & C _ {4 4} ^ {b} \end{array} \right] \left\{ \begin{array}{l} \gamma_ {1 1} \\ \kappa_ {1 1} \\ \kappa_ {1 2} \\ \kappa_ {1 3} \end{array} \right\} \tag {20}
$$

This $4 \times 4$ matrix is commonly called the beam stiffness matrix and its inverse is called the beam compliance matrix for the Euler-Bernoulli model. If a beam is made of a single isotropic material, and the origin of the cross-sectional coordinates $x _ { 2 } , x _ { 3 }$ is chosen to be at the tension center of the cross-section and $x _ { 2 } , x _ { 3 }$ are chosen to align with the principal bending directions of the beam, the constitutive relations can be written as 

$$
\left\{ \begin{array}{l} F _ {1} \\ M _ {1} \\ M _ {2} \\ M _ {3} \end{array} \right\} = \left[ \begin{array}{c c c c} E A & 0 & 0 & 0 \\ 0 & G J & 0 & 0 \\ 0 & 0 & E I _ {2} & 0 \\ 0 & 0 & 0 & E I _ {3} \end{array} \right] \left\{ \begin{array}{l} \gamma_ {1 1} \\ \kappa_ {1 1} \\ \kappa_ {1 2} \\ \kappa_ {1 3} \end{array} \right\} \tag {21}
$$

Clearly the beam stiffness matrix becomes a diagonal matrix for this particular case and the diagonal terms are the well known engineering constants including extension stiffness $E A$ , torsional 

stiffness $G J$ , and bending stiffnesses $E I _ { 2 }$ and $E I _ { 3 }$ for bending about $x _ { 2 }$ and $x _ { 3 }$ respectively. 

Eqs. (18), (19), and (20) form a system of 12 equations underpinning the Euler-Bernoulli model to be solved along with appropriate boundary conditions for 12 unknowns (four displacement variables, four strain variables, and four stress resultants). Kinematics and kinetics remain the same no matter whether the structure is made of metals or composites and these equations have been implemented in many FEA codes which have beam elements. Only difference is that the beam stiffness matrix in Eq. (20) could be fully populated if the beam is made of composites. It is noted that many beam problems, particularly those with a uniform cross-section, can be solved analytical using what we have learned in undergraduate mechanics of materials. 

Although the Euler-Bernoulli model was originally developed based on a set of ad hoc assumptions including the cross-section being rigid in plane, perpendicular to the reference line, and uniaxial stress assumption. However, such assumptions are not used in MSG to derive this model. Thus, the Euler-Bernoulli model here only refers to the model which has 12 field variables of $x _ { 1 }$ governed by the 12 equations in Eqs. (18), (19) and (20). In other words, according to the MSGbased Euler-Bernoulli model, the cross-section could be deformed, not necessarily perpendicular to the reference line, and all six stress components could exist. Actually, the slender structure which is modeled using an MSG-based beam model may not even have clearly defined cross-sections. As long as an SG for the slender structure can be defined, an MSG-based beam model can be constructed for the structural analysis. 
