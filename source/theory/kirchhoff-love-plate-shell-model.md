# Kirchhoff-Love Plate/Shell Model

Kirchhoff originally developed the classical plate model for flat panels based on a set of ad hoc assumptions including the transverse normal line being rigid in the thickness direction, perpendicular to the reference surface, and plane stress assumption. Love later extended the same set of assumptions to curved panels to develop the classical shell model. Since both models are based on the same set of assumptions and assume the same model form, we call them collectively as the 

Kirchhoff-Love model. Here, we use the plate model for illustrative purpose. The kinematics of the Kirchhoff-Love model contains three displacements $( u _ { 1 } , u _ { 2 } , u _ { 3 } )$ and six strain variables including in-plane strains $( \epsilon _ { 1 1 } , \epsilon _ { 2 2 } , \epsilon _ { 1 2 } )$ and curvatures $\left( \kappa _ { 1 1 } , \kappa _ { 2 2 } , \kappa _ { 1 2 } \right)$ . For a plate, the strain-displacement relations are given as 

$$
\epsilon_ {1 1} = \frac {\partial u _ {1}}{\partial x _ {1}}, \quad \epsilon_ {2 2} = \frac {\partial u _ {2}}{\partial x _ {2}}, \quad 2 \epsilon_ {1 2} = \frac {\partial u _ {1}}{\partial x _ {2}} + \frac {\partial u _ {2}}{\partial x _ {1}} \tag {11}
$$

$$
\kappa_ {1 1} = - \frac {\partial^ {2} u _ {3}}{\partial x _ {1} ^ {2}}, \qquad \kappa_ {2 2} = - \frac {\partial^ {2} u _ {3}}{\partial x _ {2} ^ {2}}, \qquad \kappa_ {1 2} = - \frac {\partial^ {2} u _ {3}}{\partial x _ {1} \partial x _ {2}}
$$

The kinetics of the Kirchhoff-Love model contains six stress resultants $( N _ { 1 1 } , N _ { 2 2 } , N _ { 1 2 } , M _ { 1 1 } , M _ { 2 2 } , M _ { 1 2 } )$ with $N _ { 1 1 } , N _ { 2 2 } , N _ { 1 2 }$ denoting in-plane forces and $M _ { 1 1 } , M _ { 2 2 } , M _ { 1 2 }$ denoting moments. These kinetic variables are governed by the following three equations of equilibrium 

$$
\frac {\partial N _ {1 1}}{\partial x _ {1}} + \frac {\partial N _ {1 2}}{\partial x _ {2}} + p _ {1} = 0
$$

$$
\frac {\partial N _ {2 1}}{\partial x _ {1}} + \frac {\partial N _ {2 2}}{\partial x _ {2}} + p _ {2} = 0 \tag {12}
$$

$$
\frac {\partial^ {2} M _ {1 1}}{\partial x _ {1} ^ {2}} + \frac {\partial^ {2} M _ {2 2}}{\partial x _ {2} ^ {2}} + 2 \frac {\partial^ {2} M _ {1 2}}{\partial x _ {1} \partial x _ {2}} + \frac {\partial q _ {2}}{\partial x _ {1}} - \frac {\partial q _ {1}}{\partial x _ {2}} + p _ {3} = 0
$$

where $p _ { 1 } , p _ { 2 } , p _ { 3 }$ are equivalent forces and $q 1 , q 2$ are equivalent moments, distributed over the reference surface. 

The constitutive relations of the Kirchhoff-Love model can be expressed using the following matrix equation. 

$$
\left\{ \begin{array}{l} N _ {1 1} \\ N _ {2 2} \\ N _ {1 2} \\ M _ {1 1} \\ M _ {2 2} \\ M _ {1 2} \end{array} \right\} = \left[ \begin{array}{c c c c c c} A _ {1 1} & A _ {1 2} & A _ {1 6} & B _ {1 1} & B _ {1 2} & B _ {1 6} \\ A _ {1 2} & A _ {2 2} & A _ {2 6} & B _ {1 2} & B _ {2 2} & B _ {2 6} \\ A _ {1 6} & A _ {2 6} & A _ {6 6} & B _ {1 6} & B _ {2 6} & B _ {6 6} \\ B _ {1 1} & B _ {1 2} & B _ {1 6} & D _ {1 1} & D _ {1 2} & D _ {1 6} \\ B _ {1 2} & B _ {2 2} & B _ {2 6} & D _ {1 2} & D _ {2 2} & D _ {2 6} \\ B _ {1 6} & B _ {2 6} & B _ {6 6} & D _ {1 6} & D _ {2 6} & D _ {6 6} \end{array} \right] \left\{ \begin{array}{c} \epsilon_ {1 1} \\ \epsilon_ {2 2} \\ 2 \epsilon_ {1 2} \\ \kappa_ {1 1} \\ \kappa_ {2 2} \\ 2 \kappa_ {1 2} \end{array} \right\} \tag {13}
$$

This $6 \times 6$ matrix is commonly called the plate stiffness matrix and its inverse is called the plate compliance matrix for the Kirchhoff-Love model. If a plate is made of a single isotropic material, and the origin of $x _ { 3 }$ is located at the center of the thickness, the constitutive relations can be written as 

$$
\left\{ \begin{array}{l} N _ {1 1} \\ N _ {2 2} \\ N _ {1 2} \end{array} \right\} = \frac {E h}{1 - \nu^ {2}} \left[ \begin{array}{c c c} 1 & \nu & 0 \\ \nu & 1 & 0 \\ 0 & 0 & \frac {1 - \nu}{2} \end{array} \right] \left\{ \begin{array}{l} \epsilon_ {1 1} \\ \epsilon_ {2 2} \\ 2 \epsilon_ {1 2} \end{array} \right\}, \quad \left\{ \begin{array}{l} M _ {1 1} \\ M _ {2 2} \\ M _ {1 2} \end{array} \right\} = \frac {E h ^ {3}}{1 2 (1 - \nu^ {2})} \left[ \begin{array}{c c c} 1 & \nu & 0 \\ \nu & 1 & 0 \\ 0 & 0 & \frac {1 - \nu}{2} \end{array} \right] \left\{ \begin{array}{l} \kappa_ {1 1} \\ \kappa_ {2 2} \\ 2 \kappa_ {1 2} \end{array} \right\} \tag {14}
$$

Clearly extension and bending are decoupled for this particular case. 

Eqs. (11), (12), and (13) form a system of 15 equations underpinning the Kirchhoff-Love model to be solved along with appropriate boundary conditions for 15 unknowns (three displacements, 

six strain variables, and six stress resultants). Kinematics and kinetics remain the same no matter whether the structure is made of metals or composites and these equations have been implemented in many FEA codes which have plate/shell elements. Only difference is that the plate/shell stiffness matrix in Eq. (13) could be fully populated if the plate/shell is made of composites. 

Although the Kirchhoff-Love model was originally developed based on a set of ad hoc assumptions as aforementioned, such assumptions are not used in MSG to derive this model. Also, although we used the familiar terms of $A , B , D$ matrices describing the plate stiffness matrix as those used in the classical lamination theory (CLT), none of the assumptions associated with CLT is necessary for MSG to derive the Kirchhoff-Love model. Thus, the Kirchhoff-Love model here only refers to the model which has 15 field variables of $x _ { 1 } , x _ { 2 }$ governed by the 15 equations in Eqs. (11), (12) and (13). In other words, according to the MSG-based Kirchhoff-Love model, the transverse normal line could be deformed, not necessarily perpendicular to the reference surface, and all six stress components including both in-plane stresses and transverse stresses could exist. 
