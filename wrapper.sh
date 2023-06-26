#!/bin/bash

# check for input argument
if [ -z "$1" ]
then
    echo "Usage: $0 [input_site]"
    exit 1
fi

# download html file using the first python script
python ./lib/site_parser.py $1 -v

cd ./.temp

# loop through each file and generate a configuration file
for f in ligand_*.mol2; do
    b=${f#"ligand_"}
    b=${b%".mol2"}
    echo Processing ligand $b
    ../lib/generate_config.sh ligand_$b.mol2 conf_$b.txt
done

cd ./..

# convert all .pdb files to .pdbqt using ADFR -- prepare_receptor
./lib/convert_prot.sh

# if output directory doesn't exist, create it
if [ ! -d "output_ligand" ]; then
    mkdir "output_ligand"
fi

# dock all ligands present in master folder with all the proteins
echo Docking initialized
for fi in lig_*.pdbqt; do
    ./lib/dock.sh $fi
done
echo Docking finished
