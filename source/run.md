(sc-run)=
# Execution

Without a graphic user interface, SwiftComp should be executed under command line.
For example in Windows systems, using the system command cmd to bring up the command line window.
Then use the system command `cd` to enter the right folder where the input files are in.

Then type
```
SwiftComp INPUTFILE MACRODIM ANALYSIS [INTEGRATION]
```

## Arguments

**Required**

:INPUTFILE: The name of the input file.

:MACRODIM: Macroscopic model to be constructed. Choose from
    - 1D: Beam model
    - 2D: Plate/shell model
    - 3D: 3D model

:ANALYSIS: The type of analysis to be performed. Choose from
    - H: Homogenization
    - L: Dehomogenization
    - LG: Dehomogenization with local results written in Gmsh format
    - F: Initial failure strength analysis
    - FE: Initial failure envelope
    - FI: Initial failure indexes and strength ratios
    - HA: Homogenization of aperiodic structures
    - LA: Dehomogenization of aperiodic structures
    - LAG: Dehomogenization of aperiodic structures with local results written in Gmsh format

**Optional**

:INTEGRATION: Whether to use reduced integration for certain elements
    - If not provided, full integration will be used
    - R: Reduced integration will be used


## Examples


To construct a 3D model using the input file `test.sc`:
```
SwiftComp test.sc 3D H
```

To calculate local fields:
```
SwiftComp test.sc 3D L
```

```{note}
For a specific input file, dehomogenization and initial failure related analyses (`F`/`FE`/`FI`) can only be carried out after at least one homogenization run and a corresponding file with extension `*.glb` storing extra inputs needed for dehomogenization and initial failure related analyses should also exist in the same folder.
```
