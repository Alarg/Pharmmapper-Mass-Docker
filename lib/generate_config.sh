#!/bin/bash

# Run the Python script and capture its output
# ./generate_config.sh input.mol2 config.txt
output=$(python ../lib/ligand_parser.py "$1")

# Extract the minimum and maximum coordinates from the output
min_x=$(echo "$output" | awk 'NR==2')
min_y=$(echo "$output" | awk 'NR==3')
min_z=$(echo "$output" | awk 'NR==4')
max_x=$(echo "$output" | awk 'NR==5')
max_y=$(echo "$output" | awk 'NR==6')
max_z=$(echo "$output" | awk 'NR==7')
add='30'

# Set the Vina configuration file parameters based on the coordinates
center_x=$(echo "scale=3; ($min_x + $max_x) / 2" | bc)
center_y=$(echo "scale=3; ($min_y + $max_y) / 2" | bc)
center_z=$(echo "scale=3; ($min_z + $max_z) / 2" | bc)
size_x=$(echo "scale=3; sqrt(($max_x - $min_x)^2) + $add" | bc)
size_y=$(echo "scale=3; sqrt(($max_y - $min_y)^2) + $add" | bc)
size_z=$(echo "scale=3; sqrt(($max_z - $min_z)^2) + $add" | bc)

# Isolate filename marker
pdb_id=${1#"ligand_"}
pdb_id=${pdb_id%".mol2"}

# Generate the Vina configuration file
echo Generating $2
cat << EOF > ./$2
receptor = ./.temp/$pdb_id.pdbqt
exhaustiveness = 8
center_x = $center_x
center_y = $center_y
center_z = $center_z
size_x = $size_x
size_y = $size_y
size_z = $size_z
EOF
