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

import sys, re
from monty.io import zopen

def gulp_average_energy(filen='log', lave=True):
    #filen: Screen output of gulp
    with zopen(filen, "rt") as f:
        contents = f.read()
    energy = Gulp.get_energy(contents)
    if lave :
        contents = open(filen,'r').readlines()
        for line in contents:
            if 'Total number atoms/shells' in line:
                num = int(re.findall('\d+',line)[0])
                break   
    else:
        num = 1
    return energy/num


if __name__ == '__main__':
    Gulp = GulpIO()

    num = int(sys.argv[1])
    if num == 1:
        #write input file of gulp
        Cry_Str = Structure.from_file("POSCAR")
        with open('gulpinput','w') as f:
            f.write(Gulp.keyword_line('opti conj conp nosymmetry qok'))
            f.write(Gulp.keyword_line('switch_min bfgs gnorm 0.5\n'))

            gulpinput = Gulp.structure_lines(structure = Cry_Str,symm_flg=False)
            f.write(gulpinput)

            f.write(Gulp.keyword_line('maxcyc 500'))
            f.write(Gulp.keyword_line('library self_build.lib'))
            f.write(Gulp.keyword_line('dump every gulpopt'))

    if num == 2:
        #output the energy
        energy = gulp_average_energy()
        print energy

    if num == 3:
        #output the relaxed structure
        with zopen('log', "rt") as f:
            contents = f.read()
        Opt_Str = Gulp.get_relaxed_structure(contents)
        Vasp_Str = Poscar(Opt_Str)
        Vasp_Str.write_file('out.vasp')
