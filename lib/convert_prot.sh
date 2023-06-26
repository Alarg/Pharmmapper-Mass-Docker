#! /bin/bash

# ./convert_prot.sh

for f in ./.temp/*.pdb; do
    b=${f%".pdb"}
    echo Converting protein $f to $b.pdbqt
    PATH=$ADFRDIR/bin/:$ADFRDIR/lib:$PATH LD_LIBRARY_PATH=$ADFRDIR/lib:$LD_LIBRARY_PATH REDUCE_HET_DICT=$ADFRDIR/bin/reduce_wwPDB_het_dict.txt reduce -FLIP $f > ${b}H.pdb
    PATH=$ADFRDIR/bin/:$ADFRDIR/lib:$PATH LD_LIBRARY_PATH=$ADFRDIR/lib:$LD_LIBRARY_PATH prepare_receptor -r ${b}H.pdb -o $b.pdbqt
done
