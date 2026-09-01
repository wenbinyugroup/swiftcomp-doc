
# Dehomogenization

For dehomogenization, the user needs to provide additional information obtained from the macroscopic analysis including the macroscopic primary field (such as temperature for heat conduction or displacement for the elastic analysis) and the generalized strain vector according to Eq. (29).
This information are provided in a text file corresponding to the input file name with extension `glb`.

For example if the input file is `test.sc`, one should also prepare a file called `test.sc.glb` for dehomogenization holding the data as described below. 

---

If `analysis` is 0, then the macroscopic displacements, rotations, and mechanical strains are to be provided to compute the local displacement/strain/stress fields.
The data are arranged as: 

```
v_1   v_2   v_3
C_11  C_12  C_13
C_21  C_22  C_23
C_31  C_32  C_33
id_1
sigma_g|epsilon_g
```

:`v_1`, `v_2`, `v_3`:
    Real.
    Macro displacements.

:`C_ij`:
    Real.
    Macro rotations.

    This is defined such that $\mathbf{B}_{i} = C_{ij} \mathbf{b}_{j}$ where $\mathbf{b}_{j}$ is the base vector for undeformed configuration and $\mathbf{B}_{i}$ is the base vector for the deformed configuration.

    For example, for a linear analysis of 3D structures,

    $$
    C_{ij} =
    \begin{bmatrix}
    1 + u_{1,1} & u_{2,1} & u_{3,1} \\
    u_{1,2} & 1 + u_{2,2} & u_{3,2} \\
    u_{1,3} & u_{2,3} & 1 + u_{3,3}
    \end{bmatrix}
    $$

    For linear analysis of plates/shells using the classical plate model (Kirchhoff-Love model), 

    $$
    C_{ij} =
    \begin{bmatrix}
    1 + u_{1,1} & u_{2,1} & u_{3,1} \\
    u_{1,2} & 1 + u_{2,2} & u_{3,2} \\
    -u_{3,1} & -u_{3,2} & 1 + u_{1,1} + u_{2,2}
    \end{bmatrix}
    $$

    For linear analysis of beams using the classical beam model (Euler-Bernoulli model), 

    $$
    C _ {i j} =
    \begin{bmatrix}
    1 & u_{2}^{\prime} & u_{3}^{\prime} \\
    -u_{2}^{\prime} & 1 & \theta_ {1} \\
    -u_{3}^{\prime} & -\theta_{1} & 1
    \end{bmatrix}
    $$

    where $u_{i}$ are the global displacements and $\theta_{1}$ is the twist angle. 

:`id_1`:
    Integer. Either 0 or 1.
    Indicator of using generalized stresses (0) or strains (1).

:`sigma_g`:
    Array of reals.
    Generalized stresses.

    - 3D Cauchy continuum model,

        `sigma_11  sigma_22  sigma_33  sigma_23  sigma_13  sigma_12`

    - Kirchhoff-Love plate/shell model,

        `N_11  N_22  N_12  M_11  M_22  M_12`

    - Reissner-Mindlin plate/shell model,

        `N_11  N_22  N_12  M_11  M_22  M_12  N_13  N_23`

    - Euler-Bernoulli beam model,

        `F_1  M_1  M_2  M_3`

    - Timoshenko beam model,

        `F_1  F_2  F_3  M_1  M_2  M_3` 

:`epsilon_g`:
    Array of reals.
    Generalized strains.

    - 3D Cauchy continuum model,

        `epsilon_11  epsilon_22  epsilon_33  2epsilon_23  2epsilon_13  2epsilon_12`

    - Kirchhoff-Love plate/shell model,

        `epsilon_11  epsilon_22  2epsilon_12  kappa_11  kappa_22  2kappa_12`

    - Reissner-Mindlin plate/shell model,

        `epsilon_11  epsilon_22  2epsilon_12  kappa_11  kappa_22  2kappa_12  gamma_13  gamma_23`

    - Euler-Bernoulli beam model,

        `epsilon_11  kappa_11  kappa_12  kappa_13`

    - Timoshenko beam model,

        `epsilon_11  gamma_12  gamma_13  kappa_11  kappa_12  kappa_13`


If `analysis` is 1, we need to provide an additional data for the macroscopic temperature difference to compute the thermoelastic effects.

```
T_m
```

$T _ { m }$ is the difference between the current macroscopic temperature with respect to the reference temperature $T _ { 1 } .$
If `temp_flag` is 1, $x _ { m }$ is not used.


If `analysis` is 2, we need to provide the following four values, arranged as 

```
T
id_1
-q_i | T_p_i
```

:`T`:
    Real.

:`id_1`:
    Integer. Either 0 or 1.
    Indicator of using heat fluxes (0) or temperature gradient (1).

: `q_i`:
    Array of 3 reals.
    Macroscopic heat fluxes.

:`T_p_i`:
    Array of 3 reals.
    Partial derivatives of the macroscopic temperature.

If `analysis` is 3 or 4, we need to provide the following data for dehomogenization, which are arranged as:

```
v_1   v_2   v_3   phi_star
C_11  C_12  C_13
C_21  C_22  C_23
C_31  C_32  C_33
id_1
sigma_g|epsilon_g
T_m
```

:`phi_star`:
    Real.
    Scaled electric potential.

:`sigma_g`:
    Array of reals.
    Generalized stresses.

    - 3D Cauchy continuum model,

        `sigma_11  sigma_22  sigma_33  sigma_23  sigma_13  sigma_12  D_1  D_2  D_3`

    - Kirchhoff-Love plate/shell model,

        `N_11  N_22  N_12  M_11  M_22  M_12  D_1  D_2`

    - Reissner-Mindlin plate/shell model,

        `N_11  N_22  N_12  M_11  M_22  M_12  N_13  N_23  D_1  D_2`

    - Euler-Bernoulli beam model,

        `F_1  M_1  M_2  M_3  D_1`

    - Timoshenko beam model,

        `F_1  F_2  F_3  M_1  M_2  M_3  D_1` 

:`epsilon_g`:
    Array of reals.
    Generalized strains.

    - 3D Cauchy continuum model,

        `epsilon_11  epsilon_22  epsilon_33  2epsilon_23  2epsilon_13  2epsilon_12  -E_1_star  -E_2_star  -E_3_star`

    - Kirchhoff-Love plate/shell model,

        `epsilon_11  epsilon_22  2epsilon_12  kappa_11  kappa_22  2kappa_12  -E_1_star  -E_2_star`

    - Reissner-Mindlin plate/shell model,

        `epsilon_11  epsilon_22  2epsilon_12  kappa_11  kappa_22  2kappa_12  gamma_13  gamma_23  -E_1_star  -E_2_star`

    - Euler-Bernoulli beam model,

        `epsilon_11  kappa_11  kappa_12  kappa_13  -E_1_star`

    - Timoshenko beam model,

        `epsilon_11  gamma_12  gamma_13  kappa_11  kappa_12  kappa_13  -E_1_star`

Here $\phi_{,i}^*=-E_i^*$.
If `temp_flag` is 1, `T_m` is not used.
If `analysis` is 3, the macroscopic temperature difference `T_m` does not exist. 

If `analysis` is 5 or 6, we need to provide the following data which are arranged as: 

```
v_1   v_2   v_3   phi_star  psi_star
C_11  C_12  C_13
C_21  C_22  C_23
C_31  C_32  C_33
id_1
sigma_g|epsilon_g
T_m
```

:`psi_star`:
    Real.
    Scaled magnetic potential.

:`sigma_g`:
    Array of reals.
    Generalized stresses.

    - 3D Cauchy continuum model,

        `sigma_11  sigma_22  sigma_33  sigma_23  sigma_13  sigma_12  D_1  D_2  D_3  B_1  B_2  B_3`

    - Kirchhoff-Love plate/shell model,

        `N_11  N_22  N_12  M_11  M_22  M_12  D_1  D_2  B_1  B_2`

    - Reissner-Mindlin plate/shell model,

        `N_11  N_22  N_12  M_11  M_22  M_12  N_13  N_23  D_1  D_2  B_1  B_2`

    - Euler-Bernoulli beam model,

        `F_1  M_1  M_2  M_3  D_1  B_1`

    - Timoshenko beam model,

        `F_1  F_2  F_3  M_1  M_2  M_3  D_1  B_1` 

:`epsilon_g`:
    Array of reals.
    Generalized strains.

    - 3D Cauchy continuum model,

        `epsilon_11  epsilon_22  epsilon_33  2epsilon_23  2epsilon_13  2epsilon_12  -E_1_star  -E_2_star  -E_3_star  -H_1_star  -H_2_star  -H_3_star`

    - Kirchhoff-Love plate/shell model,

        `epsilon_11  epsilon_22  2epsilon_12  kappa_11  kappa_22  2kappa_12  -E_1_star  -E_2_star  -H_1_star  -H_2_star`

    - Reissner-Mindlin plate/shell model,

        `epsilon_11  epsilon_22  2epsilon_12  kappa_11  kappa_22  2kappa_12  gamma_13  gamma_23  -E_1_star  -E_2_star  -H_1_star  -H_2_star`

    - Euler-Bernoulli beam model,

        `epsilon_11  kappa_11  kappa_12  kappa_13  -E_1_star  -H_1_star`

    - Timoshenko beam model,

        `epsilon_11  gamma_12  gamma_13  kappa_11  kappa_12  kappa_13  -E_1_star  -H_1_star`

Here $\psi_{,i}^{*} = -H_i^{*}$.
If `temp_flag` is 1, `T_m` is not used.
If `analysis` is 5, the macroscopic temperature difference `T_m` does not exist. 

If `analysis` is 9 or 10, we need to the following data which are arranged as: 

```
ubar_11  ubar_12  ubar_13
ubar_21  ubar_22  ubar_23
...
ubar_n1  ubar_n2  ubar_n3
```

:`ubar_i1`, `ubar_i2`, `ubar_i3`:
    Real.
    Displacements of node `i` along $y_1$, $y_2$, and $y_3$, respectively.

    It is noted that such displacements are not those measured in the global coordinate system of the macroscopic analysis, but those measured in the elemental coordinate system of the macroscopic analysis. 
