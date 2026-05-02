(sc-guide)=
# Guide

SwiftComp inputs are in free format which means that the entries in input files can be separated by comma, space, and/or tab, scientific notation such as `1.0E-5` can be used.
Since SwiftComp calculation is carried out using double precision, it can also handle inputs up to 15 significant digits. 

## Input files

Starting from VABS 4.0, the inputs for the VABS are separated into two files: homogenization input file and dehomogenization input file.

:`input_file_name`:
    Homogenization input file.
    VABS homogenization run only requires the homogenization input file with a name of the user's choice.
:`input_file_name.glb`:
    Dehomogenization input file.

Empty lines or comment lines can be used in the input file for readability.
The comment line must start with `!`.
Both input files should be ended with a blank line to avoid any possible incompatibility of different computer operating systems.

The input file can be given any name as long as the total number of the characters of the name including extension is not more than 256.

## Output files

VABS generates a number of output files.

:`input_file_name.ech`:
    Echo file containing all the inputs and error messages.
    For the convenience of the user to identify mistakes in the input file, all the inputs are echoed in the file named `input_file_name.ech`.
:`input_file_name.opt`:
    Output file containing all the outputs.

:`input_file_name.K`:
    VABS homogenization analysis outputs the sectional properties stored in a text file named `input_file_name.K`.

VABS dehomogenization analysis could output 3D displacement/strain/stress, or failure index/strength ratio distributions over the cross-section in different files as explained later.
All these output files are in pure text format and can be opened by any text editor.

:`input_file_name.U`:
    Recovered 3D displacements
:`input_file_name.E`:
    Recovered 3D strains for each Gauss point measured in the beam coordinate system
:`input_file_name.S`:
    Recovered 3D stresses for each Gauss point measured in the beam coordinate system
:`input_file_name.EM`:
    Recovered 3D strains for each Gauss point measured in the material coordinate system
:`input_file_name.SM`:
    Recovered 3D stresses for each Gauss point measured in the material coordinate system
:`input_file_name.EN`:
    Recovered 3D strains for each node measured in the beam coordinate system
:`input_file_name.SN`:
    Recovered 3D stresses for each node measured in the beam coordinate system
:`input_file_name.EMN`:
    Recovered 3D strains for each node measured in the material coordinate system
:`input_file_name.SMN`:
    Recovered 3D stresses for each node measured in the material coordinate system
:`input_file_name.ELE`:
    Average recovered 3D strains and stresses for each element
:`input_file_name.fi`:
    Failure index and strength ratio for each element

```{toctree}
:maxdepth: 2

convention.md
input/index.md
output/index.md
```
