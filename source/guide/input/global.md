
# 9 SwiftCompTM Inputs for Dehomogenization Run

For dehomogenization, the user needs to provide additional information obtained from the macroscopic analysis including the macroscopic primary field (such as temperature for heat conduction or displacement for the elastic analysis) and the generalized strain vector according to Eq. (29). This information are provided in a text file corresponding to the input file name with extension $g l b$ 

For example if the input file is test.sc, one should also prepare a file called test.sc.glb for dehomogenization holding the data as described below. 

If analysis= 0, then the macroscopic displacements, rotations, and mechanical strains are to be provided to compute the local displacement/strain/stress fields. The data are arranged as: 

$$
\begin{array}{l} \begin{array}{c} C _ {1 1} \end{array} C _ {1 2} \begin{array}{c} C _ {1 3} \end{array} \\ \begin{array}{c} C _ {2 1} \end{array} C _ {2 2} \begin{array}{c} C _ {2 3} \end{array} \\ \begin{array}{c c c} C _ {3 1} & C _ {3 2} & C _ {3 3} \end{array} \\ i d _ {1} \\ \bar {\epsilon} \text {o r} \bar {\sigma} \\ \end{array}
$$

where $v _ { 1 }$ , $v _ { 2 }$ , and $v _ { 3 }$ are the macro displacements, $C _ { i j }$ are macro rotations, and ¯ contains the macro generalized strains. $C _ { i j }$ is defined such that $B _ { i } = C _ { i j } { \pmb { b } } _ { j }$ where $b _ { j }$ is the base vector for undeformed configuration and $\mathbf { \delta } _ { B _ { i } }$ is the base vector for the deformed configuration. For example, for a linear analysis of 3D structures, 

$$
C _ {i j} = \left[ \begin{array}{c c c} 1 + u _ {1, 1} & u _ {2, 1} & u _ {3, 1} \\ u _ {1, 2} & 1 + u _ {2, 2} & u _ {3, 2} \\ u _ {1, 3} & u _ {2, 3} & 1 + u _ {3, 3} \end{array} \right] \tag {38}
$$

For linear analysis of plates/shells using the classical plate model (Kirchhoff-Love model), 

$$
C _ {i j} = \left[ \begin{array}{c c c} 1 + u _ {1, 1} & u _ {2, 1} & u _ {3, 1} \\ u _ {1, 2} & 1 + u _ {2, 2} & u _ {3, 2} \\ - u _ {3, 1} & - u _ {3, 2} & 1 + u _ {1, 1} + u _ {2, 2} \end{array} \right] \tag {39}
$$

For linear analysis of beams using the classical beam model (Euler-Bernoulli model), 

$$
C _ {i j} = \left[ \begin{array}{c c c} 1 & u _ {2} ^ {\prime} & u _ {3} ^ {\prime} \\ - u _ {2} ^ {\prime} & 1 & \theta_ {1} \\ - u _ {3} ^ {\prime} & - \theta_ {1} & 1 \end{array} \right] \tag {40}
$$

where $u _ { i }$ are the global displacements and $\theta _ { 1 }$ is the twist angle. 

Here $i d _ { 1 }$ indicates whether generalized stresses or generalized strains are used for dehomogenization run. If it is equal to 0, generalized stresses are used as inputs; if it is equal to 1, generalized strains are used as inputs. For the 3D Cauchy continuum model ${ \bar { \epsilon } } = \lfloor \epsilon _ { 1 1 } ~ \epsilon _ { 2 2 } ~ \epsilon _ { 3 3 } ~ 2 \epsilon _ { 2 3 } ~ 2 \epsilon _ { 1 3 } ~ 2 \epsilon _ { 1 2 } \rfloor ^ { T }$ , $\bar { \sigma } = \left\lfloor \sigma _ { 1 1 } \sigma _ { 2 2 } \sigma _ { 3 3 } \sigma _ { 2 3 } \sigma _ { 1 3 } \sigma _ { 1 2 } \right\rfloor ^ { 1 }$ . For the Kirchhoff-Love plate/shell model, ${ \bar { \epsilon } } = \lfloor \epsilon _ { 1 1 } ~ \epsilon _ { 2 2 } ~ 2 \epsilon _ { 1 2 } ~ \kappa _ { 1 1 } ~ \kappa _ { 2 2 } ~ 2 \kappa _ { 1 2 } \rfloor ^ { 1 }$ $\begin{array} { l l l l l l l } { \bar { \sigma } ~ = ~ \lfloor N _ { 1 1 } } & { N _ { 2 2 } } & { N _ { 1 2 } } & { M _ { 1 1 } } & { M _ { 2 2 } } & { M _ { 1 2 } } \end{array}$ 2cT . For the Reissner-Mindlin plate/shell model, $\begin{array} { r l } { \overline { { \epsilon } } } & { { } = } \end{array}$ $\left\lfloor \epsilon _ { 1 1 } \quad \epsilon _ { 2 2 } \quad 2 \epsilon _ { 1 2 } \quad \kappa _ { 1 1 } \quad \kappa _ { 2 2 } \quad 2 \kappa _ { 1 2 } \quad \gamma _ { 1 3 } \quad \gamma _ { 2 3 } \right\rfloor ^ { \mathcal { I } }$ , ¯σ = bN11 N22 N12 M11 M22 M12 N13 N23cT . For the Euler-Bernoulli beam model, ${ \bar { \epsilon } } = \left\lfloor \epsilon _ { 1 1 } \quad \kappa _ { 1 1 } \quad \kappa _ { 1 2 } \quad \kappa _ { 1 3 } \right\rfloor ^ { \prime }$ , $\begin{array} { r } { \bar { \boldsymbol { \sigma } } = \lfloor \boldsymbol { F } _ { 1 } \quad M _ { 1 } \quad M _ { 2 } \quad M _ { 3 } \rfloor ^ { \prime } } \end{array}$ . For the Timoshenko beam model, ${ \bar { \epsilon } } = \left\lfloor \epsilon _ { 1 1 } \gamma _ { 1 2 } \gamma _ { 1 3 } \kappa _ { 1 1 } \kappa _ { 1 2 } \kappa _ { 1 3 } \right\rfloor ^ { T }$ , $\bar { \sigma } = \lfloor F _ { 1 } ~ F _ { 2 } ~ F _ { 3 } ~ M _ { 1 } ~ M _ { 2 } ~ M _ { 3 } \rfloor ^ { T } .$ . 

If analysis=1, we need to provide an additional data for the macroscopic temperature difference $T _ { m }$ to compute the thermoelastic effects. $T _ { m }$ is the difference between the current macroscopic temperature with respect to the reference temperature $T _ { 1 } .$ If temp flag=1, $x _ { m }$ is not used. The data are arranged as: 

$$
\begin{array}{c c c} v _ {1} & v _ {2} & v _ {3} \end{array}
$$

$$
\begin{array}{l} \begin{array}{c} C _ {1 1} \end{array} C _ {1 2} \begin{array}{c} C _ {1 3} \end{array} \\ \begin{array}{c} C _ {2 1} \end{array} C _ {2 2} \begin{array}{c} C _ {2 3} \end{array} \\ \begin{array}{c c c} C _ {3 1} & C _ {3 2} & C _ {3 3} \end{array} \\ i d _ {1} \\ \bar {\epsilon} \text {o r} \bar {\sigma} \\ T _ {m} \\ \end{array}
$$

If analysis=2, we need to provide the following four values, arranged as 

$$
\begin{array}{l} \begin{array}{c} T \\ i d _ {1} \end{array} \\ T _ {, 1} \quad T _ {, 2} \quad T _ {, 3} \text {o r} - q _ {1} \quad - q _ {2} \quad - q _ {3} \\ \end{array}
$$

where $T _ { , i }$ are the gradients of the macroscopic temperature, and $q _ { i }$ are the macroscopic heat fluxes. If $i d _ { 1 } = 0$ , heat fluxes are used as inputs. If $i d _ { 1 } = 1$ , temperature gradients are used as inputs. 

If analysis= 3 or 4, we need to provide the following data for dehomogenization, which are arranged as: 

$$
\begin{array}{l} \begin{array}{c c c c} v _ {1} & v _ {2} & v _ {3} & \phi^ {*} \end{array} \\ \begin{array}{c} C _ {1 1} \end{array} C _ {1 2} \begin{array}{c} C _ {1 3} \end{array} \\ \begin{array}{c} C _ {2 1} \end{array} C _ {2 2} \begin{array}{c} C _ {2 3} \end{array} \\ \begin{array}{c c c} C _ {3 1} & C _ {3 2} & C _ {3 3} \end{array} \\ i d _ {1} \\ \bar {\epsilon} \text {o r} \bar {\sigma} \\ T _ {m} \\ \end{array}
$$

with $\phi ^ { * }$ as the scaled electric potential, $\epsilon$ as the macro generalized strains, and $\sigma$ as the macro generalized stresses. For 3D structures $\overline { { { \epsilon } } } = \left\lfloor \epsilon _ { 1 1 } \quad \epsilon _ { 2 2 } \quad \epsilon _ { 3 3 } \quad 2 \epsilon _ { 2 3 } \quad 2 \epsilon _ { 1 3 } \quad 2 \epsilon _ { 1 2 } \quad - E _ { 1 } ^ { * } \quad - E _ { 2 } ^ { * } \quad - E _ { 3 } ^ { * } \right\rfloor ^ { T }$ , $\bar { \sigma } \ = \ \lfloor \sigma _ { 1 1 } \quad \sigma _ { 2 2 } \quad \sigma _ { 3 3 } \quad \sigma _ { 2 3 } \quad \sigma _ { 1 3 } \quad \sigma _ { 1 2 } \ D _ { 1 } \quad D _ { 2 } \quad D _ { 3 } \rfloor ^ { T }$ $\sigma _ { 1 2 } \ D _ { 1 } \quad D _ { 2 } \quad D _ { 3 } \rfloor ^ { T }$ . For the Kirchhoff-Love plate/shell model, ${ \overline { { \epsilon } } } = \left\lfloor \epsilon _ { 1 1 } ~ \epsilon _ { 2 2 } ~ 2 \epsilon _ { 1 2 } ~ \kappa _ { 1 1 } ~ \kappa _ { 2 2 } ~ 2 \kappa _ { 1 2 } ~ - E _ { 1 } ^ { * } ~ - E _ { 2 } ^ { * } \right\rfloor ^ { \iota } ,$ $\bar { \sigma } = \lfloor N _ { 1 1 } N _ { 2 2 } N _ { 1 2 } M _ { 1 1 } M _ { 2 2 } M _ { 1 2 } D _ { 1 } D _ { 2 } \rfloor ^ { 7 }$ . For the Reissner-Mindlin plate/shell model, ${ \bar { \varepsilon } } = \left\lfloor \epsilon _ { 1 1 } ~ \epsilon _ { 2 2 } ~ 2 \epsilon _ { 1 2 } ~ \kappa _ { 1 1 } ~ \kappa _ { 2 2 } ~ 2 \kappa _ { 1 2 } ~ \gamma _ { 1 3 } ~ \gamma _ { 2 3 } ~ - E _ { 1 } ^ { * } ~ - E _ { 2 } ^ { * } \right\rfloor ^ { I }$ , $\bar { \sigma } = \lfloor N _ { 1 1 } N _ { 2 2 } N _ { 1 2 } M _ { 1 1 } M _ { 2 2 } M _ { 1 2 } N _ { 1 3 } N _ { 2 3 } D _ { 1 } D _ { 2 } \rfloor ^ { T }$ . For the Euler-Bernoulli beam model, ${ \bar { \epsilon } } = \lfloor \epsilon _ { 1 1 } \kappa _ { 1 1 } \kappa _ { 1 2 } \kappa _ { 1 3 } - E _ { 1 } ^ { * } \rfloor ^ { T }$ , ${ \bar { \sigma } } = \lfloor F _ { 1 } M _ { 1 } M _ { 2 } M _ { 3 } D _ { 1 } \rfloor ^ { T }$ . For the Timoshenko beam model, ${ \bar { \epsilon } } = \left\lfloor \epsilon _ { 1 1 } \gamma _ { 1 2 } \gamma _ { 1 3 } \kappa _ { 1 1 } \kappa _ { 1 2 } \kappa _ { 1 3 } D _ { 1 } \right\rfloor ^ { T }$ , $\bar { \sigma } = \lfloor F _ { 1 } F _ { 2 } F _ { 3 } M _ { 1 } M _ { 2 } M _ { 3 } D _ { 1 } \rfloor ^ { T }$ . Here $\phi _ { , i } ^ { * } = - E _ { i } ^ { * }$ . If temp flag $\mathop { \prime } = \mathop { \prime }$ , $T _ { m }$ is not used. If analysis is 3, the macroscopic temperature difference $T _ { m }$ does not exist. 

If analysis $= 5$ or 6, we need to provide the following data which are arranged as: 

$$
\begin{array}{l} \begin{array}{c c c c c} v _ {1} & v _ {2} & v _ {3} & \phi^ {*} & \psi^ {*} \end{array} \\ \begin{array}{c} C _ {1 1} \end{array} C _ {1 2} \begin{array}{c} C _ {1 3} \end{array} \\ \begin{array}{c} C _ {2 1} \end{array} C _ {2 2} \begin{array}{c} C _ {2 3} \end{array} \\ \begin{array}{c c c} C _ {3 1} & C _ {3 2} & C _ {3 3} \end{array} \\ i d _ {1} \\ \bar {\epsilon} \text {o r} \bar {\sigma} \\ T _ {m} \\ \end{array}
$$

with $\psi ^ { * }$ as the scaled magnetic potential, $\epsilon$ as the macro generalized strains, and $\sigma$ as the macro generalized stresses. For 3D structures ¯ = b11 22 33 223 213 212 − E∗1 − E∗2 − E∗3 − 

$\begin{array} { r l r l } { H _ { 1 } ^ { * } } & { { } - H _ { 2 } ^ { * } } & { { } - H _ { 3 } ^ { * } \rfloor ^ { T } } \end{array}$ , ${ \bar { \sigma } } = \left. \sigma _ { 1 1 } \quad \sigma _ { 2 2 } \quad \sigma _ { 3 3 } \quad \sigma _ { 2 3 } \quad \sigma _ { 1 3 } \quad \sigma _ { 1 2 } \ D _ { 1 } \quad D _ { 2 } \quad D _ { 3 } \quad B _ { 1 } \quad B _ { 2 } \quad B _ { 3 } \right. ^ { \iota } . \ \mathrm { F o r } \quad$ $D _ { 2 }$ the Kirchhoff-Love plate/shell model, $\bar { \epsilon } = \left\lfloor \epsilon _ { 1 1 } ~ \epsilon _ { 2 2 } ~ 2 \epsilon _ { 1 2 } ~ \kappa _ { 1 1 } ~ \kappa _ { 2 2 } ~ 2 \kappa _ { 1 2 } ~ - E _ { 1 } ^ { * } ~ - E _ { 2 } ^ { * } ~ - H _ { 1 } ^ { * } ~ - H _ { 2 } ^ { * } \right\rfloor ^ { - }$ T , ${ \bar { \sigma } } = [ N _ { 1 1 } N _ { 2 2 } N _ { 1 2 } M _ { 1 1 } M _ { 2 2 } M _ { 1 2 } D _ { 1 } D _ { 2 } B _ { 1 } B _ { 2 } ] ^ { T } . \mathrm { F o r ~ t h e ~ R e ~ }$ eissner-Mindlin plate/shell model, $\xi = \frac { \ d \xi } { \ d t _ { 1 } } \quad \epsilon _ { 2 2 } \quad 2 \epsilon _ { 1 2 } \quad \kappa _ { 1 1 } \quad \kappa _ { 2 2 } \quad 2 \kappa _ { 1 2 } \quad \gamma _ { 1 3 } \quad \gamma _ { 2 3 } \quad - \ E _ { 1 } ^ { * } \quad - \ E _ { 2 } ^ { * } \quad - \ H _ { 1 } ^ { * } \quad - \ H _ { 2 } ^ { * } \mid ^ { I } .$ $\bar { \sigma } =$ $\ \underline { { { \vert } } } N _ { 1 1 } ~ N _ { 2 2 } ~ N _ { 1 2 } ~ M _ { 1 1 } ~ M _ { 2 2 } ~ M _ { 1 2 } ~ N _ { 1 3 } ~ N _ { 2 3 } ~ D _ { 1 } ~ D _ { 2 } ~ B _ { 1 } ~ B _ { 2 } \vert ^ { T }$ . For the Euler-Bernoulli beam model, ${ \bar { \epsilon } } = \left\lfloor \epsilon _ { 1 1 } ~ \kappa _ { 1 1 } ~ \kappa _ { 1 2 } ~ \kappa _ { 1 3 } ~ - E _ { 1 } ^ { * } ~ - H _ { 1 } ^ { * } \right\rfloor ^ { \prime }$ , $\bar { \sigma } = \lfloor F _ { 1 } M _ { 1 } M _ { 2 } M _ { 3 } D _ { 1 } B _ { 1 } \rfloor ^ { T }$ . For the Timoshenko beam model, $\bar { \epsilon } = \left\lfloor \epsilon _ { 1 1 } \gamma _ { 1 2 } \gamma _ { 1 3 } \kappa _ { 1 1 } \kappa _ { 1 2 } \kappa _ { 1 3 } - E _ { 1 } ^ { * } - H _ { 1 } ^ { * } \right\rfloor ^ { T }$ , ${ \bar { \sigma } } = \lfloor F _ { 1 } F _ { 2 } F _ { 3 } M _ { 1 } M _ { 2 } M _ { 3 } D _ { 1 } B _ { 1 } \rfloor ^ { T }$ . Here $\psi _ { , i } ^ { * } = - H _ { i } ^ { * }$ . If temp flag=1, $T _ { m }$ is not used. If analysis is 5, the macroscopic temperature difference $T _ { m }$ does not exist. 

If analysis $= 9$ or 10, we need to the following data which are arranged as: 

$$
\begin{array}{l} \bar {u} _ {1 1}, \bar {u} _ {1 2}, \bar {u} _ {1 3} \\ \bar {u} _ {2 1}, \bar {u} _ {2 2}, \bar {u} _ {2 3} \\ \begin{array}{c c c} \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \end{array} \\ \bar {u} _ {n 1}, \bar {u} _ {n 2}, \bar {u} _ {n 3} \\ \end{array}
$$

with $u _ { i 1 } , u _ { i 2 } , u _ { i 3 }$ as the displacements of node $i$ along $y _ { 1 } , y _ { 2 } , y _ { 3 }$ directions respectively. It is noted that such displacements are not those measured in the global coordinate system of the macroscopic analysis, but those measured in the elemental coordinate system of the macroscopic analysis. 



# 10 SwiftCompTM Inputs for Failure Analysis

A corresponding homogenization analysis must be run before carrying out any failure analysis. 

For failure analysis (including initial failure strength, initial failure index/strength ratio, and initial failure envelope), the *.glb file will be used to store the data needed for failure analysis instead. First, additional material properties are needed for each material at each given temperature including a failure criterion and corresponding strength constants. Three lines will be inserted and the inputs needed for failure analyses should be arranged as: 

f ailure criterion num of constants 

$l _ { c }$ 

const1 const2 const3 . . . 

f ailure criterion is an integer identifier for the failure criterion. num of constants indicates the number of strength constants needed for the corresponding failure criterion. $l _ { c }$ is a real number indicating the characteristic length used in the nonlocal approach for initial failure analysis. If $l _ { c }$ is equal to zero, the local approach based on element averaged values will be used. $c o n s t _ { 1 } , c o n s t _ { 2 } , c o n s t _ { 3 } \ldots$ are the corresponding strength constants. It is noted that this block of data should be corresponding to the material block in the main input file. In other words, for each material with mat id, we need to provide such information for each temperature. 

f ailure criterion can be equal to 1, 2, 3, 4, 5, and another number greater than 10. For isotropic material, 1 is the max principal stress criterion, 2 is the max principal strain criterion, 3 is the max shear stress criterion (also commonly called the Tresca criterion), 4 is the max shear strain criterion, and 5 is the Mises criterion. For anisotropic materials, 1 is the max stress criterion for anisotropic materials, 2 is the max strain criterion for anisotropic materials, 3 is the Tsai-Hill criterion, 4 is the Tsai-Wu criterion and 5 is the Hashin criterion. 11 or a larger integer indicates 

a user-defined failure criterion. If f ailure criterion is equal to 1, 2, 3, 4, 5, num of constants is not used. If it is a user-defined failure criterion, then num of constants will be used to input the right number of strength constants. It is assumed that the number of strength constants will not be greater than 9 for a material. If the material is isotropic, the failure criterion and corresponding strength constants are defined as follows. 

• If f ailure criterion is 1, the max principal stress criterion is used and two strength constants are needed: one for tensile strength (X) and one for compressive strength ( $X ^ { \prime }$ ), arranged as $X , X ^ { \prime }$ . 

• If f ailure criterion is 2, the max principal strain criterion is used and two strength constants are needed: one for tensile strength ( $X _ { \epsilon }$ ) and one for compressive strength ( $X _ { \epsilon } ^ { \prime }$ ), arranged as $X _ { \epsilon } , X _ { \epsilon } ^ { \prime }$ . 

• If f ailure criterion is 3, the max shear stress criterion (aka the Tresca criterion) is used and one shear strength constant ( $S$ ) is needed. 

• If f ailure criterion is 4, the max shear strain criterion is used and one shear strength constant ( $S _ { \epsilon }$ ) is needed. 

• If f ailure criterion is 5, the Mises criterion is used and one strength constant ( $X$ ) is needed. 

If the material is not isotropic (transversely isotropic, orthotropic, or general anisotropic), the failure criterion and corresponding strength constants are defined as follows. 

• If f ailure criterion is 1, the max stress criterion is used and nine strength constants are needed: three for tensile strengths $( X , Y , Z )$ in three directions, three for compressive strengths $( X ^ { \prime } , Y ^ { \prime } , Z ^ { \prime } )$ in three directions, and three for shear strengths $( R , T , S )$ in three principal planes, arranged as $X , Y , Z , X ^ { \prime } , Y ^ { \prime } , Z ^ { \prime } , R , T , S$ . 

• If f ailure criterion is 2, the max strain criterion is used and nine strength constants are needed: three for tensile strengths $( X _ { \epsilon } , Y _ { \epsilon } , Z _ { \epsilon } )$ in three directions, three for compressive strengths $( X _ { \epsilon } ^ { \prime } , Y _ { \epsilon } ^ { \prime } , Z _ { \epsilon } ^ { \prime } )$ in three directions, and three for shear strengths $( R _ { \epsilon } , T _ { \epsilon } , S _ { \epsilon } )$ in three principal planes, arranged as $X _ { \epsilon } , Y _ { \epsilon } , Z _ { \epsilon } , X _ { \epsilon } ^ { \prime } , Y _ { \epsilon } ^ { \prime } , Z _ { \epsilon } ^ { \prime } , R _ { \epsilon } , T _ { \epsilon } , S _ { \epsilon }$ . 

• If f ailure criterion is 3, the Tsai-Hill criterion is used and six strength constants are needed: three for normal strengths $( X , Y , Z )$ in three directions and three for shear strengths $( R , S , T )$ in three principal planes, arranged as $X , Y , Z , R , T , S$ . 

• If f ailure criterion is 4, the Tsai-Wu criterion is used and nine strength constants are needed: three for tensile strengths $( X , Y , Z )$ , three for compressive strengths $( X ^ { \prime } , Y ^ { \prime } , Z ^ { \prime } )$ in three directions, and three for shear strengths $( R , T , S )$ in three principal planes, arranged as $X , Y , Z , X ^ { \prime } , Y ^ { \prime } , Z ^ { \prime } , R , T , S$ . 

• If f ailure criterion is 5, the Hashin criterion is used and six strength constants are needed: two for tensile strengths $( X , Y )$ , two for compressive strengths $( X ^ { \prime } , Y ^ { \prime } )$ in two directions, and two for shear strengths $( R , S )$ in two principal planes, arranged as $X , Y , X ^ { \prime } , Y ^ { \prime } , R , S$ . 

It is noted that for failure analysis, general anisotropic materials are also approximated using orthotropic materials due to limited number of strength constants. In SwiftComp $^ \mathrm { { 4 M } }$ , both the tensile strengths and compressive strengths are expressed using positive numbers. In other words, in the uniaxial compressive test along $y _ { 1 }$ direction, $\sigma _ { 1 1 } = - X ^ { \prime }$ when material fails. 

After the material block for strength parameters, we need to provide the following line in the *.glb file containing one integer if analysis is not equal to 9 or 10. 

$i d _ { 1 }$ 

Here $i d _ { 1 }$ indicates whether the strength is expressed in terms of generalized stresses or generalized strains. If it is equal to 0, the strength is expressed in terms of generalized stresses; if it is equal to 1, it is expressed in terms of generalized strains. 

For failure envelope analysis, we need to provide the following line in the *.glb file containing two integers if analysis is not equal to 9 or 10. 

istr1 istr2 

Here $\boldsymbol { i s t r } _ { 1 }$ and $\boldsymbol { i s t r } _ { 2 }$ indicate the two load directions that one would like to predict a failure envelope for. The values could be 1, 2, 3, 4,. . . , corresponding to the arrangement of the generalized stresses (if $i d _ { 1 } = 0$ ) or generalized strains (if $i d _ { 1 } = 1$ ). For example for the 3D model, the stress/strain are arranged in the order of 11, 22, 33, 23, 13, 12. If we want to draw a $\sigma _ { 2 2 }$ — $\sigma _ { 1 3 }$ failure envelope, we will have $i s t r _ { 1 } = 2 , i s t r _ { 2 } = 5$ . 

For failure index analysis, this above line is not necessary. Instead we need to provide the following line in the *.glb file containing $n$ real numbers with $n$ equal to the total number of generalized stresses or generalized strains. 

$s t r _ { 1 } s t r _ { 2 } s t r _ { 3 } \ldots s t r _ { n }$ 

Here $s t r _ { 1 } , s t r _ { 2 } , \ldots , s t r _ { n }$ indicate the given loads used to compute the strength ratio and the failure index. These values can be given in terms of generalized stresses or generalized strains depending on whether the required strength outputs are in generalized stresses ( $i d _ { 1 } = 0$ ) or generalized strains ( $i d _ { 1 } = 1$ ). If analysis is equal to 9 or 10, corresponding nodal displacements should be provided as the inputs instead as those described at the end of the previous section. 

Both input files, input file name and input file name.glb, should be ended with a blank line to avoid any possible incompatibility of different computer operating systems. The input file can be given any name as long as the total number of the characters of the name including extension is not more than 256. For the convenience of the user to identify mistakes in the input file, all the inputs are echoed in a file named input file name.ech. Error messages are also written at the end of input file name.ech and on the output screen. 
