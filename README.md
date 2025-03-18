# Finding the distribution of Hidden Stop codons in case of Frame-Shift mutation in *E. coli* Genome dataset downloaded from NCBI database

The main focus of this study is, to understand provision of reducing impact of frame shift mutations in genetic code table, which may occur when protein translation starts not at the first nucleotide but at the second (+1 frame shift) or third (−1 frame shift) nucleotide of the codon. Frameshifts would yield non-functional or cytotoxic proteins which may not be useful for the organism. Therefore frame-shifts lead to waste of energy, resources and activity of the biosynthetic machinery. The "ambush" hypothesis (Seligmann and Pollock 2004) suggests that the hidden stop codons and their role in off-frame (incorrect) gene reading suggests that hidden stop codons prevent off-frame gene reading and there is an advantage in using codons that can be part of hidden stop codons. The ambush hypothesis implies that hidden stop codons are 
sometimes selected and this selection is reflected in sequences.

In this research, we employ E. coli genome downloaded from NCBI database to investigate codon pairs capable of producing hidden stop codons. We focus to determining the count of stop codons produced by codon pairs and their respective amino acid pairs. Also identifying the first occurrence position of hidden stop codons for each codon pair and amino acid pair. So, we have developed algorithms using python programming language to determine those results and create csv files to store them. 

Standard genetic codon table

  ![Screenshot 2025-03-18 114920](https://github.com/user-attachments/assets/17e24bd9-158b-4bab-959e-0c94d798df00)

frameshift mutation example:

  ![Screenshot 2025-03-18 121937](https://github.com/user-attachments/assets/b23749f0-f6d7-43c4-9e87-c77d3be0b80d)


Theoretically, there are 43 and 90 possible amino acid pairs that can produce stop codons in +1 and -1 frame shifted translation scenarios. In our preliminary findings, we observed that out of 43 pairs of amino acid, in 10 cases, codon usage favours producing stop codons for Frame-Shift +1 and out of 90 pairs of amino acid, in 36 cases, codon-usage favours producing stop codons for Frame-Shift -1 of E. coli genome.


## Steps Involved:
1. **Dataset Download**
2. **Data Cleaning**
3. **Identifying the stop codon producing amino acid pairs according to the standard genetic code table**
4. **Calculate the count of combination of codon pairs that can produce stop codons**
5. **Calculate the count of stop codons that are actually exists or used in the E. coli Genome**
6. **Take out the Codon usage ratio=(sum of actually used codons)/(sum of all synonymous codons that can produce stop codons)**
     ![Screenshot 2025-03-18 114323](https://github.com/user-attachments/assets/cc503db8-9f30-49cb-9a07-f794b02e5f14)

7. **Plotting bar graph to visualize the ratio of codon pair usage** 
  

## Libraries & Frameworks:
- **Data Manipulation, Framing and storing**: `Pandas`, `Numpy`   
- **Mathematical Operations**: `excel` 

## Results

