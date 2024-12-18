import os

from Bio import SeqIO


# Set your working directory
print(os.getcwd())
os.chdir('/Users/mahitha/Documents/Projects/crispr-genome-diversity/data/igh/data/amplicon')
print(os.getcwd())

# Read the FASTA file (100bp before and 100bp after the guide RNA + PAM region)
for record in SeqIO.parse("igh_amplicon.fa", "fasta"):
    sequence = record.seq # sequence data
    header = record.id # header data
    print(f"Header: {header}, Sequence: {sequence}")