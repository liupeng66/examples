#!/usr/bin/python2
#Change the format of crystal structure
#python Str_Format.py infile outfile
try:
    from pymatgen.io.vasp.inputs           import Poscar
    from pymatgen                          import Structure
    from pymatgen.command_line.gulp_caller import GulpIO
except:
    print 'You should install pymatgen first.'
    exit(0)

import sys
from monty.io import zopen

def Read_POSCAR( filen ):
    with zopen(filen, "rt") as f:
        contents = f.read()
    Cry_Str = IStructure.from_str(contents, fmt="poscar")
    return Read_POSCAR

if __name__ == '__main__':
    Cry_Str = Structure.from_file("POSCAR")
    #energy  = get_energy_buckingham(Cry_Str)
    #print energy
    Gulp = GulpIO()
    #gulpinput = Gulp.structure_lines(structure = Cry_Str)
    #with open('gulpinput','w') as f:
        #f.write(gulpinput)
    
    #with zopen('./out1', "rt") as f:
        #contents = f.read()

    #energy = Gulp.get_energy(contents)
    #print energy

    with zopen('gulpoutput', "rt") as f:
        contents = f.read()
    Opt_Str = Gulp.get_relaxed_structure(contents)
    Vasp_Str = Poscar(Opt_Str)
    Vasp_Str.write_file('out.vasp')


