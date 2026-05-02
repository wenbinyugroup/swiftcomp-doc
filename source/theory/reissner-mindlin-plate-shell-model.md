# Reissner-Mindlin Plate/Shell Model

When the thickness of the panel is not very small with respect to the in-plane dimensions, the Kirchhoff-Love model is inadequate and a refined model is needed. The next refinement is the so-called Reissner-Mindlin model due to independent contributions of Reissner and Mindlin to its development. The kinematics of the Reissner-Mindlin model contains five displacement variables including three displacements $( u _ { 1 } , u _ { 2 } , u _ { 3 } )$ and two rotations $( \theta _ { 1 } , \theta _ { 2 } )$ , and eight strain variables including in-plane strains $( \epsilon _ { 1 1 } , \epsilon _ { 2 2 } , \epsilon _ { 1 2 } )$ , curvatures $( \kappa _ { 1 1 } , \kappa _ { 2 2 } , \kappa _ { 1 2 } )$ , and transverse shear strains $( \gamma _ { 1 2 } , \gamma _ { 1 3 } )$ . For a plate, the strain-displacement relations are 

$$
\epsilon_ {1 1} = \frac {\partial u _ {1}}{\partial x _ {1}}, \qquad \epsilon_ {2 2} = \frac {\partial u _ {2}}{\partial x _ {2}}, \qquad 2 \epsilon_ {1 2} = \frac {\partial u _ {1}}{\partial x _ {2}} + \frac {\partial u _ {2}}{\partial x _ {1}}
$$

$$
\kappa_ {1 1} = \frac {\partial \theta_ {2}}{\partial x _ {1}}, \quad \kappa_ {2 2} = - \frac {\partial \theta_ {1}}{\partial x _ {2}}, \quad \kappa_ {1 2} = - \frac {\partial \theta_ {2}}{\partial x _ {2}} - \frac {\partial \theta_ {1}}{\partial x _ {1}} \tag {15}
$$

$$
\gamma_ {1 3} = \frac {\partial u _ {3}}{\partial x _ {1}} + \theta_ {2}, \qquad \gamma_ {2 3} = \frac {\partial u _ {3}}{\partial x _ {2}} - \theta_ {1}
$$

The kinetics of the Reissner-Mindlin model contains eight stress resultants $( N _ { 1 1 } , N _ { 2 2 } , N _ { 1 2 } , M _ { 1 1 }$ , $M _ { 2 2 } , M _ { 1 2 } , N _ { 1 3 } , N _ { 2 3 } )$ with $N _ { 1 1 } , N _ { 2 2 } , N _ { 1 2 }$ denoting in-plane forces, $M _ { 1 1 } , M _ { 2 2 } , M _ { 1 2 }$ denoting moments, and $N _ { 1 3 } , N _ { 2 3 }$ denoting transverse shear forces. These kinetic variables are governed by the following 

five equations of equilibrium: 

$$
\frac {\partial N _ {1 1}}{\partial x _ {1}} + \frac {\partial N _ {1 2}}{\partial x _ {2}} + p _ {1} = 0
$$

$$
\frac {\partial N _ {2 1}}{\partial x _ {1}} + \frac {\partial N _ {2 2}}{\partial x _ {2}} + p _ {2} = 0
$$

$$
\frac {\partial N _ {1 3}}{\partial x _ {1}} + \frac {\partial N _ {2 3}}{\partial x _ {2}} + p _ {3} = 0 \tag {16}
$$

$$
\frac {\partial M _ {1 2}}{\partial x _ {1}} + \frac {\partial M _ {2 2}}{\partial x _ {2}} - q _ {1} - N _ {2 3} = 0
$$

$$
\frac {\partial M _ {1 1}}{\partial x _ {1}} + \frac {\partial M _ {2 1}}{\partial x _ {2}} + q _ {2} - N _ {1 3} = 0
$$

The constitutive relations of the Reissner-Mindlin model can be expressed using the following matrix equation: 

$$
\left\{ \begin{array}{l} N _ {1 1} \\ N _ {2 2} \\ N _ {1 2} \\ M _ {1 1} \\ M _ {2 2} \\ M _ {1 2} \\ N _ {1 3} \\ N _ {2 3} \end{array} \right\} = \left[ \begin{array}{c c c c c c c c} A _ {1 1} & A _ {1 2} & A _ {1 6} & B _ {1 1} & B _ {1 2} & B _ {1 6} & Y _ {1 1} & Y _ {1 2} \\ A _ {1 2} & A _ {2 2} & A _ {2 6} & B _ {1 2} & B _ {2 2} & B _ {2 6} & Y _ {2 1} & Y _ {2 2} \\ A _ {1 6} & A _ {2 6} & A _ {6 6} & B _ {1 6} & B _ {2 6} & B _ {6 6} & Y _ {3 1} & Y _ {3 2} \\ B _ {1 1} & B _ {1 2} & B _ {1 6} & D _ {1 1} & D _ {1 2} & D _ {1 6} & Y _ {4 1} & Y _ {4 2} \\ B _ {1 2} & B _ {2 2} & B _ {2 6} & D _ {1 2} & D _ {2 2} & D _ {2 6} & Y _ {5 1} & Y _ {5 2} \\ B _ {1 6} & B _ {2 6} & B _ {6 6} & D _ {1 6} & D _ {2 6} & D _ {6 6} & Y _ {6 1} & Y _ {6 2} \\ Y _ {1 1} & Y _ {2 1} & Y _ {3 1} & Y _ {4 1} & Y _ {5 1} & Y _ {6 1} & C _ {1 1} & C _ {1 2} \\ Y _ {1 2} & Y _ {2 2} & Y _ {3 2} & Y _ {4 2} & Y _ {5 2} & Y _ {6 2} & C _ {1 2} & C _ {2 2} \end{array} \right] \left\{ \begin{array}{l} \epsilon_ {1 1} \\ \epsilon_ {2 2} \\ 2 \epsilon_ {1 2} \\ \kappa_ {1 1} \\ \kappa_ {2 2} \\ 2 \kappa_ {1 2} \\ \gamma_ {1 3} \\ \gamma_ {2 3} \end{array} \right\} \tag {17}
$$

This $8 \times 8$ matrix is called the plate stiffness matrix and its inverse is called the plate compliance matrix for the Reissner-Mindlin model. $G _ { i j } ( i = 1 , 2 ; j = 1 , 2$ ) denote the transverse shear stiffness terms and $Y _ { i j }$ $i = 1 , \ldots , 6 ; j = 1 , 2$ ) denote the coupling stiffness terms relating the classical plate deformation modes and transverse shear deformation modes. It is noted that $A , B , D$ matrices could be different from those in Eq. (13) due to possible nonzero $Y _ { i j }$ ( $i = 1 , \ldots , 6 ; j = 1 , 2$ ). 

Eqs. (15), (16), and (17) form a system of 21 equations underpinning the Reissner-Mindlin model to be solved along with appropriate boundary conditions for 21 unknowns (five displacement variables, eight strain variables, and eight stress resultants). Kinematics and kinetics remain the same no matter whether the structure is made of metals or composites and these equations have been implemented in many FEA codes which have plate/shell elements. Only difference is that the plate/shell stiffness matrix in Eq. (17) could be fully populated if the plate/shell is made of composites. 

Although the Reissner-Mindlin model was originally developed based on a set of ad hoc assumptions, such assumptions are not used in MSG to derive this model. Thus, the Reissner-Mindlin model here only refers to the model which has 21 field variables of $x _ { 1 } , x _ { 2 }$ governed by the 21 equations in Eqs. (15), (16) and (17). The deformation and stress state of the structure are not assumed a priori but determined by MSG. 
