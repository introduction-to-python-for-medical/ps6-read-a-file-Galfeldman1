def create_codon_dict(file_path):
    pass # Replace the pass with your code
    path="data/codons.txt"
file = open(path)
rows = file.readlines()
file.close()
mydict={}
for row in rows:
  row=row.strip().split('\t')
  codon=row[0]
  amino_acid=row[2]
  mydict[codon]=amino_acid
 
print(mydict)

