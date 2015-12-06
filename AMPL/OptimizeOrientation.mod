#PARAMETERS AND SETS
set FACETS = 1..12; #the set of triangular facets the shape has
param area{FACETS}; # each facet has an assigned area
param normalX{FACETS}; # the x component of the facet's normal
param normalY{FACETS}; # the y component of the facet's normal
param normalZ{FACETS}; # the z component of the facet's normal

param coneOfShameWindow;

#Decision Variables
var cX>=-1, <=1; #cone of shame X component
var cY >=-1, <=1; #cone of shame Y component
var cZ>=-1, <=1; # cone of shame Z component
var inCone{FACETS} binary; # 1 if facet is in cone of shame, 0 otherwise

var X_helper{FACETS} binary; #1 if x component of facet normal is within x range
var X_up{FACETS} binary; # 1 if x comp is below upper range
var X_down{FACETS} binary; #1 if x comp is above lower range

var Y_helper{FACETS} binary; #1 if y component of facet normal is within y range
var Y_up{FACETS} binary; 
var Y_down{FACETS} binary;

var Z_helper{FACETS} binary; #1 if z component of facet normal is within z range
var Z_up{FACETS} binary; 
var Z_down{FACETS} binary;

#doesn't support material not only have to do with area, but also the height off the base of the model?
#also, I think with the way it is now, it will say that you need support material for the bottom of the part that is actually touching the printer surface
minimize totalsupportArea: sum{f in FACETS}(area[f]*inCone[f]);

#subject to checkX_up {f in FACETS}: #check if normalX[f] is below upper range of cX, if yes, set X_up[f] = 1
#subject to checkX_down {f in FACETS}:#check if normalX[f] is above lower range of cX, if yes, set X_down[f] = 1
subject to withinX {f in FACETS}: X_up[f] + X_down[f] <= 1+X_helper[f];

#subject to checkY_up {f in FACETS}: #check if normalY[f] is below upper range of cY, if yes, set Y_up[f] = 1
#subject to checkY_down {f in FACETS}:#check if normalY[f] is above lower range of cY, if yes, set Y_down[f] = 1
subject to withinY{f in FACETS}: Y_up[f]+Y_down[f] <= 1+ Y_helper[f];

#subject to checkZ_up {f in FACETS}: #check if normalZ[f] is below upper range of cZ, if yes, set Z_up[f] = 1
#subject to checkZ_down {f in FACETS}:#check if normalZ[f] is above lower range of cZ, if yes, set Z_down[f] = 1
subject to withinZ{f in FACETS}: Z_up[f]+Z_down[f] <= 1+ Z_helper[f];

#if below upper range and above lower range, set inCone[f] = 1
subject to setInCone {f in FACETS}:X_helper[f]+Y_helper[f]+Z_helper[f]<=2+inCone[f];