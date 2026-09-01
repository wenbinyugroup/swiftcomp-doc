
# Homogenization

Effective properties computed by SwiftComp are stored in `input_file_name.k`, including effective stiffness matrix corresponding to Eq. (32), effective flexibility matrix (inverse of stiffness matrix), effective thermal coefficients including CTEs, specific heat, pyroelectric coefficients, and pyromagnetic coefficients. 

If the material can be approximated as orthotropic material, engineering constants corresponding to the elastic stiffness matrix is also provided among the outputs. 

Regarding the effective specific heat, there are two contributions $D _ { \theta \theta }$ and $F _ { e f f }$.

**If `temp_flag` is 0**, the effective specific heat can be calculated as 

$$
\bar {c} _ {v} = D _ {\theta \theta} - T F _ {e f f}
$$

with $T$ as the current temperature $T = T _ { 1 } + T _ { m }$ .

**If `temp_flag` is 1**, the effective specific heat can be calculated as 

$$
\bar {c} _ {v} = \frac {D _ {\theta \theta} - T _ {1} F _ {e f f}}{\bar {\theta} ^ {2}}
$$

with $\theta$ as the average temperature of the SG. 

The effective density of the SG is also listed as one output. 

**If `analysis` is 9**, the output will be a $2 4 \times 2 4$ effective element stiffness matrix for a 8-node 3D element.

**If `analysis` is 10**, the output will be a $6 0 \times 6 0$ effective element stiffness matrix for a 20-node 3D element. 

All these output files are in pure text format and can be opened and edited by any text editor. 
