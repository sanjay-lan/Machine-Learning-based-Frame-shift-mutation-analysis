import pandas as pd
#TGA

def count_TAA_j_followed_by_k(gene_sequence, j, k):
    first_occ = 0
    codons_rx = ["ttt", "tct", "tat", "tgt", "ctt", "cct", "cat", "agt", "att", "act", "aat", "agt", "gtt", "gct",
                 "gat", "ggt"]
    codons_ry = ["aat", "aac", "aaa", "aag"]

    for i in range(0, len(gene_sequence) - 3, 3):
        codon = gene_sequence[i:i + 3]
        next_codon = gene_sequence[i + 3:i + 6]

        if codon == j and next_codon == k:
            if j in codons_rx and k in codons_ry:
                if first_occ == 0:
                    first_occ = (i // 3) + 1
    return first_occ

def count_TAG_j_followed_by_k(gene_sequence, j, k):
    first_occ = 0
    codons_rx = ["ttt", "tct", "tat", "tgt", "ctt", "cct", "cat", "agt", "att", "act", "aat", "agt", "gtt", "gct",
                 "gat", "ggt"]
    codons_ry = ["agt", "agc", "aga", "agg"]

    for i in range(0, len(gene_sequence) - 3, 3):
        codon = gene_sequence[i:i + 3]
        next_codon = gene_sequence[i + 3:i + 6]

        if codon == j and next_codon == k:
            if j in codons_rx and k in codons_ry:
                if first_occ == 0:
                    first_occ = (i // 3) + 1

    return first_occ


def count_TGA_j_followed_by_k(gene_sequence, j, k):
    first_occ = 0

    codons_rx = ["ttt", "tct", "tat", "tgt", "ctt", "cct", "cat", "agt", "att", "act", "aat", "agt", "gtt", "gct",
                 "gat", "ggt"]
    codons_ry = ["gat", "gac", "gaa", "gag"]

    for i in range(0, len(gene_sequence) - 3, 3):
        codon = gene_sequence[i:i + 3]
        next_codon = gene_sequence[i + 3:i + 6]

        if codon == j and next_codon == k:
            if j in codons_rx and k in codons_ry:
                if first_occ == 0:
                    first_occ = (i // 3) + 1

    return first_occ

def amino_acids(j,k):
    a = ""
    b = ""
    phe = ["ttt", "ttc"]
    leu = ["tta", "ttg", "ctt", "ctc", "cta", "ctg"]
    ile = ["att", "atc", "ata"]
    val = ["gtt", "gtc", "gta", "gtg"]
    ser = ["tct", "tcc", "tca", "tcg", "agt", "agc"]
    arg = ["cgt", "cgc", "cga", "cgg", "aga", "agg"]
    pro = ["cct", "ccc", "cca", "ccg"]
    thr = ["act", "acc", "aca", "acg"]
    ala = ["gct", "gcc", "gca", "gcg"]
    tyr = ["tat", "tac"]
    his = ["cat", "cac"]
    asn = ["aat", "aac"]
    lys = ["aaa", "aag"]
    asp = ["gat", "gac"]
    glu = ["gaa", "gag"]
    cys = ["tgt", "tgc"]
    gly = ["ggt", "ggc", "gga", "ggg"]

    for p in range(1):
        if j in phe:
            a = " Phe"
        elif j in leu:
            a = " Leu"
        elif j in ile:
            a = " Ile"
        elif j in val:
            a = " Val"
        elif j in ser:
            a = " Ser"
        elif j in pro:
            a = " Pro"
        elif j in thr:
            a = " Thr"
        elif j in ala:
            a = " Ala"
        elif j in tyr:
            a = " Tyr"
        elif j in his:
            a = " His"
        elif j in asn:
            a = " Asn"
        elif j in asp:
            a = " Asp"
        elif j in cys:
            a = " Cys"
        elif j in arg:
            a = " Arg"
        elif j in gly:
            a = " Gly"

    for q in range(1):
        if k in asn:
            b = " Asn"
        elif k in lys:
            b = " Lys"
        elif k in asp:
            b = " Asp"
        elif k in glu:
            b = " Glu"
        elif k in ser:
            b = " Ser"
        elif k in arg:
            b = " Arg"

    return a, b

def read_genes_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    genes = []
    current_gene_name = None
    current_gene_sequence = ""
    for line in lines:
        if line.startswith('>:|'):
            if current_gene_name and current_gene_sequence:
                genes.append((current_gene_name, current_gene_sequence))
            current_gene_name = line.strip()
            current_gene_sequence = ""
        else:
            current_gene_sequence += line.strip()

    if current_gene_name and current_gene_sequence:
        genes.append((current_gene_name, current_gene_sequence))

    return genes

file_path = 'gene.ena'
genes = read_genes_from_file(file_path)
gene_names = []
df = pd.DataFrame(columns=['gene_name', 'Codon', 'AA', 'First_occ'])
data = []

for gene_info, gene_sequence in genes:
    gene_name = gene_info.split(':')[1]
    gene_names.append(gene_name)
    codons_x = ["ttt", "ttc", "tta", "ttg", "ctt", "ctc", "cta", "ctg", "att", "atc", "ata", "gtt", "gtc", "gta", "gtg",
                "tct", "tcc",
                "tca", "tcg", "agt", "agc", "cct", "ccc", "cca", "ccg", "act", "acc", "aca", "acg", "gct", "gcc", "gca",
                "gcg", "tat", "tac", "cat", "cac", "aat", "aac", "gat", "gac", "tgt", "tgc", "cgt", "cgc", "cga", "cgg",
                "aga", "agg", "ggt", "ggc", "gga", "ggg"]
    codons_y = ["aat", "aac", "aaa", "aag"]

    for j in codons_x:
        for k in codons_y:
            first_occ = count_TAA_j_followed_by_k(gene_sequence, j, k)
            a, b = amino_acids(j, k)
            data.append([gene_name, j+' '+k, a+' '+b, first_occ])
df1 = pd.DataFrame(data, columns=['gene_name', 'Codon', 'AA', 'First_occ'])
df = df._append(df1, ignore_index=True)

data = []
for gene_info, gene_sequence in genes:
    gene_name = gene_info.split(':')[1]
    gene_names.append(gene_name)
    codons_x = ["ttt", "ttc", "tta", "ttg", "ctt", "ctc", "cta", "ctg", "att", "atc", "ata", "gtt", "gtc", "gta", "gtg",
                "tct", "tcc",
                "tca", "tcg", "agt", "agc", "cct", "ccc", "cca", "ccg", "act", "acc", "aca", "acg", "gct", "gcc", "gca",
                "gcg", "tat", "tac", "cat", "cac", "aat", "aac", "gat", "gac", "tgt", "tgc", "cgt", "cgc", "cga", "cgg",
                "aga", "agg", "ggt", "ggc", "gga", "ggg"]
    codons_y = ["tct", "tcc", "tca", "tcg", "agt", "agc", "cgt", "cgc", "cga", "cgg", "aga", "agg"]

    for j in codons_x:
        for k in codons_y:
            first_occ = count_TAG_j_followed_by_k(gene_sequence, j, k)
            a, b = amino_acids(j, k)
            data.append([gene_name, j+' '+k, a+' '+b, first_occ])
df2 = pd.DataFrame(data, columns=['gene_name', 'Codon', 'AA', 'First_occ'])
df = df._append(df2, ignore_index=True)

data = []
for gene_info, gene_sequence in genes:
    gene_name = gene_info.split(':')[1]
    gene_names.append(gene_name)
    codons_x = ["ttt", "ttc", "tta", "ttg", "ctt", "ctc", "cta", "ctg", "att", "atc", "ata", "gtt", "gtc", "gta", "gtg",
                "tct", "tcc",
                "tca", "tcg", "agt", "agc", "cct", "ccc", "cca", "ccg", "act", "acc", "aca", "acg", "gct", "gcc", "gca",
                "gcg", "tat", "tac", "cat", "cac", "aat", "aac", "gat", "gac", "tgt", "tgc", "cgt", "cgc", "cga", "cgg",
                "aga", "agg", "ggt", "ggc", "gga", "ggg"]
    codons_y = ["gat", "gac", "gaa", "gag"]

    for j in codons_x:
        for k in codons_y:
            first_occ = count_TGA_j_followed_by_k(gene_sequence, j, k)
            a, b = amino_acids(j, k)
            data.append([gene_name, j+' '+k, a+' '+b, first_occ])
df3 = pd.DataFrame(data, columns=['gene_name', 'Codon', 'AA', 'First_occ'])
df = df._append(df3, ignore_index=True)
df = df.groupby(['gene_name', 'Codon', 'AA']).agg({'First_occ': 'max'}).reset_index()
df = df.pivot(index='gene_name', columns=['Codon', 'AA'], values='First_occ').fillna(0)
df = df.fillna(0)
print(df)
df.to_csv('FS-1(First_occ).csv')
