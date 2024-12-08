def create_codon_dict(file_path):
    with open(file_path, 'r') as file:
        rows = file.readlines()
    
    codon_dict = {}
    for row in rows:
        row = row.strip().split('\t')
        if len(row) >= 3:
            codon = row[0]
            amino_acid = row[2]
            codon_dict[codon] = amino_acid
    
    return codon_dict  
