# hyperspheres
Graphically sampling of hyperspheres

Numerical Methods
Programming Assignment 3

We have discussed approaches to sampling hyperspheres.  The general equation is as follows:

r ← [0,1] ; θ ← [0,2π] ; x = droot(r*cos(θ)) ; y = droot(r*sin(θ))

Where r is the unit radius,  is the angle in radians and d is the dimensionality of the hypersphere.

In addition, we discussed Archimedes’ theorem, that the area of a sphere equals the area of every right circular cylinder circumscribed about the sphere (excluding the bases). The axial projection of any measurable region on a sphere on the right circular cylinder circumscribed about the sphere preserves area.

    • Your first task is to write a professionally documented functioning program that allows the user to input ranges for r and  and produce a two-dimensional image sampling of a circle segment.  By testing a variety of user inputs, provide a summary description of the ways in which the user input affects the graphical output.
    • Your second task is to extend the concept to three dimensions (adding) and again, allow for different values of r, .  Describe in summary what affect different values of the variables has on the output.

=========================================

User input and generated output:

﻿﻿﻿﻿﻿﻿User can set variable:

    ﻿Points
        Defines the number of points to be generated.
    Radius / Roh
        Defines the radius from origin (0,0,0) at which the points will be drawn to﻿﻿.
    Theta
        Defines the circumference to which the points will be confined within
    Phi
        Defines the Phi which defines the Z axis circumference to which the sphere will be confined to

All variables are modifiable to users desire within set optimal parameters. All generated shapes will have within them uniform distribution of points.

Source controlled using GitHub: https://github.com/findhamza/hyperspheres.git

Attached zip file contains:

    Source Code (hypers.py)
    Virtual Python Env. and Config.
    Uniformly distributed disk image (Disk.png)
    Uniformly distributed sphere image (Sphere.png)
