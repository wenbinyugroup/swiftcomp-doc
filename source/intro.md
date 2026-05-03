# Introduction

SwiftComp represents a general-purpose approach for computing effective properties (aka constitutive modeling) of composite materials and structures.
Here composite materials and structures refer to those materials and structures featuring anisotropy and heterogeneity, not just the traditional fiber reinforced polymers or unidirectional laminates.
SwiftComp can be used independently for virtual testing composite materials and structures or as a plugin to power conventional finite element analysis (FEA) codes with efficient high-fidelity multiscale modeling for such materials and structures.
SwiftComp implements Mechanics of Structure Genome (MSG), a unique multiscale modeling approach based on the concept of Structure Gene (SG), to capture both anisotropy and heterogeneity of composites at the microscopic scale or other scales of user’s interest.
MSG unifies micromechanics and structural mechanics to provide a single theory to model all types of composite materials and structures.
SwiftComp enables engineers to analyze composite materials and structures similarly to metals, capturing details as needed and affordable. 

To facilitate the use of SwiftComp, several graphic user interfaces have been developed including Gmsh4SC, TexGen4SC, Abaqus-SwiftComp GUI, Ansys-SwiftComp GUI, and Nastran-SwiftComp GUI.
Instructions for using SwiftComp through these GUIs are given in user manuals accompanying the corresponding GUIs.
This manual will provide an introduction to MSG, the history and functionalities of SwiftComp, conventions, inputs, outputs, maintenance, and tech support for more advanced SwiftComp users. 


## History

SwiftComp is a culmination of prior work on composite structures and materials implemented in three different codes including VABS, VAPAS, and VAMUCH developed by Prof. Wenbin Yu and his coworkers.
The VABS code was developed for composite beam modeling during Prof. Yu’s PhD study at Georgia Tech under the supervision of Prof. Dewey Hodges.
VABS was later significantly enhanced at Utah State through its affiliation with Georgia Tech’s rotorcraft center and commercialized by Utah State through AnalySwift LLC.
The VAPAS code was developed to model composite laminated plates and shells at Georgia Tech and VAPAS was also later enhanced at Utah State.
VAMUCH, also called SwiftComp Micromechanics, is a general-purpose micromechanics code for homogenization and dehomogenization of periodic, heterogeneous materials developed at Utah State.
In year 2012, Prof. Yu introduced the representative structural element (RSE) concept to unify structural mechanics and micromechanics for multiscale constitutive modeling of composites [1].
RSE concept was later renamed as SG to emphasize its role in filling the gap between materials genome and structural analysis [2].
The founding paper of MSG was published in year 2016 [3] featuring a general geometrical nonlinear formulation, which was simplified to linear problems later in [4].
To implement MSG, we started the development of SwiftComp in April 2014 at Purdue University.
SwiftComp is a single code which can reproduce all of the functionalities in VABS, VAPAS, and VAMUCH, as well as many other capabilities not found in any of these three codes.
SwiftComp can reproduce VABS for composite beams made of uniform cross-sections (see the right figure of Figure 4), VAPAS for composite laminated plates and shells (see the right figure of Figure 5), and VAMUCH for 3D periodic heterogeneous materials (see Figure 3).
However, currently not all VABS capabilities are available in SwiftComp and VABS is still maintained as a separate code for cross-sectional analysis of composite beams while VAPAS and VAMUCH are superseded by SwiftComp.
SwiftComp has many more functionalities not available in the previous three codes such as slender structures with spanwise heterogeneities, plates and shells with in-plane heterogeneity, partially periodic structures and materials, aperiodic structures and materials, etc. 


## Functionalities

Fundamentally speaking, SwiftComp takes the geometry and material characteristics of an SG described using a finite element mesh as the input and computes the effective properties for the macroscopic analysis.
This process is commonly called homogenization.
SwiftComp can also compute the local fields within the SG based on global behavior obtained from the macroscopic analysis.
This process is commonly called dehomogenization, constantly neglected in some multiscale modeling approaches.
Note that SwiftComp is not limited to structural modeling, it can be used to perform multiphysics homogenization and dehomogenization of materials and structures responsive to thermal, mechanical, electric, and magnetic fields. 

Currently, we only provide executables for computers with Windows or Linux OS.
The Gmsh-based GUI, TexGen-bsed GUI, and interfaces with other commercial FEA software packages such as Ansys, Abaqus, Nastran can also be freely downloaded from cdmHUB.org.
Ansys-SwiftComp GUI can be found at https://cdmhub.org/resources/1136.
Abaqus-SwiftComp GUI can be found at https://cdmhub.org/resources/1134.
Nastran-SwiftComp GUI can be found at https://cdmhub.org/resources/1752.
