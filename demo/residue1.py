from mcircuit import *
import sympy as sym

s = sym.var('s')
z = 1.0*(3.81078125e-19*s**6 + 2.68632879045996e-11*s**4 + 0.00063122335439346*s**2 + 4944.08235441037)/(1.63120026676829e-25*s**7 + 2.57963974895563e-19*s**6 + 7.96785370953058e-17*s**5 + 1.23772016720644e-10*s**4 + 3.47431772456453e-9*s**3 + 0.00538940056086208*s**2 + 0.0397609461185644*s + 61645.6417839253)

pprint(poles(z))
pprint(zeros(z))
pprint(residues(z, s))


