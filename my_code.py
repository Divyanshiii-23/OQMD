from pymatgen.ext.matproj import MPRester
from pymatgen.io.vasp import Poscar

API_KEY = "RSCMCp6x85fzs5d6WE462HG6SI2KiuKn"
mpr = MPRester(API_KEY)

formula = "Al2O3"
try:
    results = mpr.materials.summary.search(formula=formula)
    if results:
        for result in results:
            material_id = result.material_id
            print(f"Fetching structure for {result.formula_pretty} (ID: {material_id})")
            
            structure = mpr.get_structure_by_material_id(material_id)
            poscar = Poscar(structure)
            filename = f"POSCAR_{material_id}"
            poscar.write_file(filename)
            print(f"Saved POSCAR as {filename}")
    else:
        print(f"No materials found for formula: {formula}")
except Exception as e:
    print(f"Error fetching data: {e}")
nano POSCAR_mp-1244940

