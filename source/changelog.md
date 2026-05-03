# What's New


## Version 2.1

SwiftComp 2.1 perform constitutive modeling (homogenization and dehomogenization) of a block of 3D elements to be a 3D 8-node or 20-node element. 


## Version 2.0

SwiftComp 2.0 implements thermoviscoelastic analysis capabilities, temperature change within the SG, and wedge element. Also a few minor bugs were fixed. 


## Version 1.5

SwiftComp 1.5 implements a more efficient and robust way for predicting failure envelopes and also a few minor bugs were fixed. 



## Version 1.4

SwiftComp 1.4 implements homogenization, dehomogenization, initial failure analysis according to the Timoshenko beam model. 


## Version 1.3

SwiftComp 1.3 implements the capability to predict initial failure strengths according to a given failure criterion, failure envelopes for giving two load directions, and failure indexes and strength ratios for materials and structures subject to an arbitrary loading. 


## Version 1.2

SwiftComp 1.2 implements the capability to deal with aperiodic, or partially periodic SGs, or periodic SGs without periodic nodes on the boundary surfaces. 

## Version 1.1

The pointwise anisotropic heterogeneity is enabled in SwiftComp 1.1. The SG can contain phases with general anisotropic materials with material properties given in material coordinates which could be different from the local coordinate system and defined for each element. First, an elemental coordinate system is defined by three points for each element, then the material coordinate system can be defined as a simple rotation around one of the axis of the elemental coordinate element. The first capability (orientation described using an elemental coordinate system) is found applications in woven components and short fiber reinforced composites. The second capability (orientation described using a rotation angle) is found applications in composite laminates. 


## Version 1.0

Starting SwiftComp 1.0, two versions of SwiftComp are available: SwiftComp Standard and SwiftComp Professional.
In SwiftComp Professional, a direct sparse solver is used to deal with big models which could have as many as millions of degrees of freedom.
A parallel edition is also available for SwiftComp Professional.
For a problem that SwiftComp Professional runs more than a few minutes, it is better to use the parallel edition as it can exploit multiple cores which are readily available on most computers nowadays.
In the standard version, Prof. Sloan’s method $^ { 5 }$ is used to provide the renumbering of the finite element mesh, standard skyline storage is used along with a regular direct linear solver.
To simplify the maintenance of the code, the later official released versions use the parallel version with a direct sparse solver.

## Alpha Version

The alpha version of SwiftComp can perform the constitutive modeling corresponding to the classical structural models including the Euler-Bernoulli beam model, Kirchhoff-Love plate/shell model, and 3D Cauchy continuum model.

