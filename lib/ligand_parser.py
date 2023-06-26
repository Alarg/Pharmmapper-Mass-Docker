import sys

def parse_pdb(file_path, verbose):
    if verbose:
        print('Parsing PDB file...')
    atoms = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('ATOM'):
                atom = {}
                atom['x'] = float(line[30:38])
                atom['y'] = float(line[38:46])
                atom['z'] = float(line[46:54])
                atoms.append(atom)
    return atoms

def parse_pdbqt(file_path, verbose):
    if verbose:
        print('Parsing PDBQT file...')
    atoms = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('ATOM'):
                atom = {}
                atom['x'] = float(line[30:38])
                atom['y'] = float(line[38:46])
                atom['z'] = float(line[46:54])
                atoms.append(atom)
    return atoms

def parse_mol2(file_path, verbose):
    if verbose:
        print('Parsing MOL2 file...')
    atoms = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('@<TRIPOS>ATOM'):
                for j in range(i + 1, len(lines)):
                    if lines[j].startswith('@<TRIPOS>BOND'):
                        break
                    fields = lines[j].split()
                    atom = {}
                    atom['x'] = float(fields[2])
                    atom['y'] = float(fields[3])
                    atom['z'] = float(fields[4])
                    atoms.append(atom)
                break
    return atoms

def find_min_coords(atoms):
    min_x = min(atoms, key=lambda atom: atom['x'])['x']
    min_y = min(atoms, key=lambda atom: atom['y'])['y']
    min_z = min(atoms, key=lambda atom: atom['z'])['z']
    return min_x, min_y, min_z

def find_max_coords(atoms):
    max_x = max(atoms, key=lambda atom: atom['x'])['x']
    max_y = max(atoms, key=lambda atom: atom['y'])['y']
    max_z = max(atoms, key=lambda atom: atom['z'])['z']
    return max_x, max_y, max_z

def main():
    if len(sys.argv) == 2 or len(sys.argv) == 3 and sys.argv[2] == '-v':
        file_path = sys.argv[1]
        ext = file_path.split('.')[-1].lower()
        verbose = False
        if len(sys.argv) == 3:
            verbose = True

        if ext == 'pdb':
            atoms = parse_pdb(file_path, verbose)
        elif ext == 'pdbqt':
            atoms = parse_pdbqt(file_path, verbose)
        elif ext == 'mol2':
            atoms = parse_mol2(file_path, verbose)
        else:
            print('Invalid file type')
            sys.exit(1)

        min_x, min_y, min_z = find_min_coords(atoms)
        max_x, max_y, max_z = find_max_coords(atoms)

        if verbose:
            print(file_path + ' coordinates:')
            print(f'Minimum X: {min_x:.3f}')
            print(f'Minimum Y: {min_y:.3f}')
            print(f'Minimum Z: {min_z:.3f}')
            print(f'Maximum X: {max_x:.3f}')
            print(f'Maximum Y: {max_y:.3f}')
            print(f'Maximum Z: {max_z:.3f}')

        else:
            print(file_path)
            print(f'{min_x:.3f}')
            print(f'{min_y:.3f}')
            print(f'{min_z:.3f}')
            print(f'{max_x:.3f}')
            print(f'{max_y:.3f}')
            print(f'{max_z:.3f}')

    else:
        print('Usage: python ligand_parser.py file_path [-v]')

if __name__ == '__main__':
    main()
