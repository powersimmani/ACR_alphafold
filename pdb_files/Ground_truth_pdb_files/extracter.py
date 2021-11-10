import os
from Bio import PDB
import sys, code, os
from Bio.PDB import PDBParser, PDBIO


items = os.listdir("./")

for item in items:
    if ".ent" not in item:
        continue

    io = PDBIO()
    pdb = PDBParser().get_structure(item[3:7].upper(), item)

    for chain in pdb.get_chains():
        io.set_structure(chain)
        io.save("./extracted/" + pdb.get_id() + "_" + chain.get_id() + ".pdb")
        code.interact(local=dict(globals(), **locals()))