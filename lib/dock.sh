#! /bin/bash

# ./dock.sh input_ligand.pdbqt

for f in ./.temp/conf_*.txt; do
    b=${f#"./.temp/conf_"}
    b=${b%".txt"}
    echo Processing ligand $1 for protein $b
    name=${1%".pdbqt"}
    ./lib/vina --config ./.temp/conf_$b.txt --ligand $1 --out ./output_ligand/${name}_$b.pdbqt --log ./output_ligand/${name}_$b.txt
done
