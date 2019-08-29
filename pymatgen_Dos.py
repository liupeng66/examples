from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp.outputs import Vasprun, Procar
from pymatgen.core.ion import Ion

v = Vasprun('vasprun.xml')
cdos = v.complete_dos
#el = cdos.Structure.composition
eles = cdos.structure.composition.elements

for ele in eles:
    plotter = DosPlotter()
    ele_or_dos = cdos.get_element_spd_dos(ele)
    plotter.add_dos_dict(ele_or_dos)
    plotter.show(xlim=[-8, 8], ylim=[0, 1000])

exit(0)
print cdos.Structure
#print el.elements
#exit(0)

#orbital_dos = cdos.get_spd_dos()
#plotter = DosPlotter()
#plotter.add_dos_dict(orbital_dos)
#plotter.show(xlim=[-8, 8], ylim=[0, 1000])







#ele_or_dos = cdos.get_element_spd_dos('Ni')
#plotter = DosPlotter()
#plotter.add_dos_dict(ele_or_dos)
#plotter.show(xlim=[-8, 8], ylim=[0, 1000])
