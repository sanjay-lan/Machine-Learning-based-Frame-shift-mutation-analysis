# Finding the distribution of Hidden Stop codons in case of Frame-Shift mutation in *E. coli* Genome dataset downloaded from NCBI database

The main focus of this study is, to understand provision of reducing impact of frame shift mutations in genetic code table, which may occur when protein translation starts not at the first nucleotide but at the second (+1 frame shift) or third (−1 frame shift) nucleotide of the codon. Frameshifts would yield non-functional or cytotoxic proteins which may not be useful for the organism. Therefore frame-shifts lead to waste of energy, resources and activity of the biosynthetic machinery. The "ambush" hypothesis (Seligmann and Pollock 2004) suggests that the hidden stop codons and their role in off-frame (incorrect) gene reading suggests that hidden stop codons prevent off-frame gene reading and there is an advantage in using codons that can be part of hidden stop codons. The ambush hypothesis implies that hidden stop codons are 
sometimes selected and this selection is reflected in sequences.

In this research, we employ E. coli genome downloaded from NCBI database to investigate codon pairs capable of producing hidden stop codons. We focus to determining the count of stop codons produced by codon pairs and their respective amino acid pairs. Also identifying the first occurrence position of hidden stop codons for each codon pair and amino acid pair. So, we have developed algorithms using python programming language to determine those results and create csv files to store them. 

Standard genetic codon table

  ![Screenshot 2025-03-18 114920](https://github.com/user-attachments/assets/17e24bd9-158b-4bab-959e-0c94d798df00)

frameshift mutation example:

  ![Screenshot 2025-03-18 121937](https://github.com/user-attachments/assets/b23749f0-f6d7-43c4-9e87-c77d3be0b80d)


Theoretically, there are 43 and 90 possible amino acid pairs that can produce stop codons in +1 and -1 frame shifted translation scenarios. In our preliminary findings, we observed that out of 43 pairs of amino acid, in 10 cases, codon usage favours producing stop codons for Frame-Shift +1 and out of 90 pairs of amino acid, in 36 cases, codon-usage favours producing stop codons for Frame-Shift -1 of E. coli genome.

  Standard code table with stop codon producing codon pairs in every stop codon producing amino acid pairs for FS +1:

  ![Screenshot 2025-03-18 125228](https://github.com/user-attachments/assets/60ae14ef-539d-4e89-bdf7-7d6fc15d1da2)

  Standard code table with stop codon producing codon pairs in every stop codon producing amino acid pairs for FS -1:

  ![Screenshot 2025-03-18 125251](https://github.com/user-attachments/assets/6ff168c4-e80d-49e2-b330-1fb62a67c7cc)

## Steps Involved:
1. **Dataset Download**
   E coli dataset downloaded from NCBI:  Ecol_K12_MG1655

2. **Identifying the stop codon producing amino acid pairs according to the standard genetic code table**
   1. In the above picture stop codon producing codon pairs in every stop codon producing amino acid pairs for FS +1
   2. In the above picture stop codon producing codon pairs in every stop codon producing amino acid pairs for FS -1
3. **Calculate Expected Stop Codon frequency**
   Expected stop codon frequency = (number of stop codon producing codon pairs in every stop codon producing amino acid pairs) / (number of all the synonymous codon pairs in every stop codon producing amino acid pairs)
   here is the example: TAA,TGA and TAG are universal stop codons.
   ![Screenshot 2025-03-18 133813](https://github.com/user-attachments/assets/0fc7556d-742b-41dd-9d79-07b6bd69858e)

7. **All AA codon Pairs: Calculate the count of all combination of codon pairs that can produce stop codon producing amino acid pairs in Ecoli genome**
9. **Codon pair generating STOP: Calculate the count of stop codons that are actually exists or used in the E. coli Genome**
10. **Observed STOP codon frequency**
    The ratio between Codon pair generating STOP and All AA codon pair.
    Observed STOP codon frequency = (Codon pair generating STOP) / (All AA codon pair)

    Example:
    ![Screenshot 2025-03-18 135124](https://github.com/user-attachments/assets/72fe0e53-7c84-4c32-8780-ad89947fd296)

    
12. **Take out the Codon usage ratio as Obj/Exp**
    Obj/Exp = (Observed STOP codon frequency)/ (Expected Stop Codon frequency)

    Example:
    ![Screenshot 2025-03-18 145036](https://github.com/user-attachments/assets/b74c753c-93a4-49eb-8e48-1b224d554548)


14. **Plotting bar graph to visualize the ratio of codon pair usage**

    1. For Frame-Shift +1:
    ![Screenshot 2025-03-18 145641](https://github.com/user-attachments/assets/960bdc13-901f-458a-8e73-c33c6f671a81)


    2. For Frame-Shift -1:
    ![Screenshot 2025-03-18 145702](https://github.com/user-attachments/assets/00ccd2dd-c95d-43b6-9a94-fffce7c01769)




## Libraries & Frameworks:
- **Data Manipulation, Framing and storing**: `Pandas`, `Numpy`   
- **Mathematical Operations**: `excel` 

## Findings
### For Frame-Shift +1
      

