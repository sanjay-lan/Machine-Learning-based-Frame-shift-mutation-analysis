# Codon Usage Optimization Against Frame-Shift Mutations in Escherichia coli Genome

## Overview

The main focus of this study is, to understand provision of reducing impact of frame shift mutations in genetic code table, which may occur when protein translation starts not at the first nucleotide but at the second (+1 frame shift) or third (−1 frame shift) nucleotide of the codon. Frameshifts would yield non-functional or cytotoxic proteins which may not be useful for the organism. Therefore frame-shifts lead to waste of energy, resources and activity of the biosynthetic machinery. The "ambush" hypothesis (Seligmann and Pollock 2004) suggests that the hidden stop codons and their role in off-frame (incorrect) gene reading suggests that hidden stop codons prevent off-frame gene reading and there is an advantage in using codons that can be part of hidden stop codons. The ambush hypothesis implies that hidden stop codons are sometimes selected and this selection is reflected in sequences.

## Objective

In this project, our main objective is to understand provision in genetic code table for incorporation of stop codon in a frame shifted ORF of a gene and existence of any evolutionary pressure towards codon selection using machine learning approach in Escherichia coli Genome. 

## Libraries, Frameworks and other tools:
- **Data Manipulation, Framing and storing**: `Pandas`, `Numpy`   
- **Mathematical Operations on the dataset**: `Excel`
- **To Implement Machine Learning Alorithms**: `Scikit-learn`
- **Feature Selection**: `Boruta`
- **Logistic Regression Classifier**
- **Gaussian Naive Bayes**
- **Support Vector Classifier**
- **Random Forest Classifier**
- **Adaboost Classifier**
- **Gradient Boosting Classifier**
- **XGB Classifier**
- **Visualization**: `Matplotlib`

## Methodology:

![Screenshot 2025-03-18 201743](https://github.com/user-attachments/assets/d38c8f69-7a3f-4b4d-b74e-f0ebaf4b2fde)


## Explaination

In this research, we employ E. coli genome downloaded from NCBI database to investigate codon pairs capable of producing hidden stop codons. We focus to determining the count of stop codons produced by codon pairs and their respective amino acid pairs. Also identifying the first occurrence position of hidden stop codons for each codon pair and amino acid pair. So, we have developed algorithms using python programming language to determine those results and create csv files to store them. Further we implement machine learning algorithms on the newly created dataset to classify Essential and Non-Essential genes and High Expressive and Low Expressive genes in the genome. 

**Standard genetic codon table:**

  ![Screenshot 2025-03-18 114920](https://github.com/user-attachments/assets/17e24bd9-158b-4bab-959e-0c94d798df00)

**frameshift mutation example:**

  ![Screenshot 2025-03-18 121937](https://github.com/user-attachments/assets/b23749f0-f6d7-43c4-9e87-c77d3be0b80d)


Theoretically, there are 43 and 90 possible amino acid pairs that can produce stop codons in +1 and -1 frame shifted translation scenarios. In our preliminary findings, we observed that out of 43 pairs of amino acid, in 10 cases, codon usage favours producing stop codons for Frame-Shift +1 and out of 90 pairs of amino acid, in 36 cases, codon-usage favours producing stop codons for Frame-Shift -1 of E. coli genome.

  Standard code table with stop codon producing codon pairs in every stop codon producing amino acid pairs for FS +1:

  ![Screenshot 2025-03-18 125228](https://github.com/user-attachments/assets/60ae14ef-539d-4e89-bdf7-7d6fc15d1da2)

  Standard code table with stop codon producing codon pairs in every stop codon producing amino acid pairs for FS -1:

  ![Screenshot 2025-03-18 125251](https://github.com/user-attachments/assets/6ff168c4-e80d-49e2-b330-1fb62a67c7cc)

## Steps Involved in dataset creation and pre-processing:
1. **Dataset Download**
   E coli dataset downloaded from NCBI:  Ecol_K12_MG1655

2. **Identifying the stop codon producing amino acid pairs according to the standard genetic code table**
   1. In the above picture stop codon producing codon pairs in every stop codon producing amino acid pairs for FS +1
   2. In the above picture stop codon producing codon pairs in every stop codon producing amino acid pairs for FS -1
3. **Calculate Expected Stop Codon frequency**
   Expected stop codon frequency = (number of stop codon producing codon pairs in every stop codon producing amino acid pairs) / (number of all the synonymous codon pairs in every stop codon producing amino acid pairs).
   
   **TAA,TGA and TAG are universal stop codons.**
    Example:
   
    ![Screenshot 2025-03-18 133813](https://github.com/user-attachments/assets/0fc7556d-742b-41dd-9d79-07b6bd69858e)

4. **All AA codon Pairs: Calculate the count of all combination of codon pairs that can produce stop codon producing amino acid pairs in Ecoli genome**
5. **Codon pair generating STOP: Calculate the count of stop codons that are actually exists or used in the E. coli Genome**
6. **Observed STOP codon frequency**
    The ratio between Codon pair generating STOP and All AA codon pair.
    Observed STOP codon frequency = (Codon pair generating STOP) / (All AA codon pair)

    Example:

    ![Screenshot 2025-03-18 135124](https://github.com/user-attachments/assets/72fe0e53-7c84-4c32-8780-ad89947fd296)

    
7. **Take out the Codon usage ratio as Obj/Exp**
    Obj/Exp = (Observed STOP codon frequency)/ (Expected Stop Codon frequency)

    Example:

   ![Screenshot 2025-03-18 145036](https://github.com/user-attachments/assets/b74c753c-93a4-49eb-8e48-1b224d554548)


8. **Plotting bar graph to visualize the ratio of codon pair usage**

    1. For Frame-Shift +1:
    
    ![Screenshot 2025-03-18 145641](https://github.com/user-attachments/assets/960bdc13-901f-458a-8e73-c33c6f671a81)

    2. For Frame-Shift -1:
    
    ![Screenshot 2025-03-18 145702](https://github.com/user-attachments/assets/00ccd2dd-c95d-43b6-9a94-fffce7c01769)


## Steps Involved in classification:

After getting the preliminary result, we implemented machine learning algorithms to classify different labels using newly created dataset. 

1. **Type Classification**

There are two types of genes in the dataset, essential genes and non-essential genes. We used binary classification approach to classify gene type. We have implemented the model for both FS+1 and FS-1 datasets.

   1. For Frame-shift +1:
      
      After classification we calculate accuracy, true positive rate and false positive rate and then we plot the roc curves with AUC score for various classifiers. We also calculated the Accuracy, Precision, Recall and F1 Score to evaluate model performance.

      ![image](https://github.com/user-attachments/assets/7862b2de-5ce5-4bfe-b8c9-6f41fbb5ba9a)

      ![image](https://github.com/user-attachments/assets/7911fd3c-2e04-4c66-8db8-029a0a9bfe04)

      The curves are generating more than average result, it suggests that the gene type depends on features that contain hidden stop codon producing codon usage ratio for each amino acid pairs. 

      From this analysis we can say that codon usage is not random in genes. Some codons are selected in essential genes to avoid Frame-shift +1 mutation. 

      For better understanding and validation, we have used boruta feature selection and calculate feature importance score and ranking and arrange them in ascending order. From there we pick up 10 best features and 10 worst features and implement the classification model to them.

      a. For 10 best features:

      ![image](https://github.com/user-attachments/assets/1fd12931-32db-423b-810a-b06c7c452792)

      ![image](https://github.com/user-attachments/assets/2569e879-042b-45a4-bd8e-6c4a8dbc38fe)

      b. For 10 worst Features:

      ![image](https://github.com/user-attachments/assets/5ee54448-f827-4c18-bf24-455ed33ddb01)
   
      ![image](https://github.com/user-attachments/assets/37a1bcba-87b4-4673-b308-fb9f8fe67ef2)


      We can observe a significant difference about 15% between best feature’s AUC percentage and worst feature’s AUC percentage in Figure and classification performance is also better in essential genes as shown in Tables. From this we can say that all the stop codon producing amino acid pairs are not utilized equally only a few hidden stop-codon producing amino acid pairs are selected for the gene sequence latter on which can produce stop codon in frame-shift +1 mutation scenario.
 
   2. For Frame-Shift -1:

   As similler to fs+1 we implement the classification model for fs-1 dataset and calculate true positive rate and false positive rate then plot roc curve with AUC percentage.

   ![image](https://github.com/user-attachments/assets/5404e3ea-e28e-41ab-8595-33776566ae75)

     
   ![image](https://github.com/user-attachments/assets/8a13839f-5df1-4b58-a610-2939fb49eb3e)

   The curves are generating AUC near 75%, it suggests that the gene type can be classified by features, which contains hidden stop codon producing codon usage ratio as feature values in case of Frame-shift -1. We can say gene type depends on codon usage in case of Frame-shift -1. And also, our previous results shows that hidden stop codon producing codon pairs are used more than other synonymous codons in case of frame-shift -1.  

   From this analysis we can say that codon usage is not random in genes. Some codons are selected in essential genes to avoid Frame-shift -1 mutation. 

   For better understanding and validation, we use feature selection and calculate feature importance score and ranking and arrange them in ascending order. From there we pick up 20 best features and 20 worst features and implement the classification model to them.

   a. For 20 best features:

   ![image](https://github.com/user-attachments/assets/3ac72978-f595-4f2b-8cd1-f94ea940f86c)

   ![image](https://github.com/user-attachments/assets/e566e110-7347-435e-8948-668abe3ca74e)


   b. For 20 worst features:

   ![image](https://github.com/user-attachments/assets/d25e21df-bd60-4993-9dac-1933cce86fa6)

   ![image](https://github.com/user-attachments/assets/32ed8f8e-22c4-4e74-9a48-af1e7cc09b52)

   We can observe a significant difference about 20% between best feature’s AUC percentage and worst feature’s AUC percentage in Figure of best feature & worst feature and classification performance is also better in essential genes as shown in Tables. From this we can say that all the stop codon producing amino acid pairs are not utilized equally only a few hidden stop-codon producing amino acid pairs are selected for the gene sequence latter on which can produce stop codon in frame-shift -1 mutation scenario.

   
2. **Gene Expression Classification using CAI values**

Gene expression or CAI values are in quantitative. So, we categorise gene expression in two classes 0 to 0.3 as class 0 or low expressive class and 0.6 to 1 as class 1 or high expressive class. We discarded the medium range genes of range 0.3 to 0.6 for better identification of high expression gens and low expression genes. We implemented binary classification model to classify both the datasets. 

   1. For Frame Shoft +1:

      We implement binary classification model for FS +1 dataset and calculate accuracy, true positive rate and false positive rate and then we plot the ROC curves with AUC percentage for different classifiers.

        ![image](https://github.com/user-attachments/assets/c5cfe601-acf8-4607-89ff-02b3887bfd60)

        ![image](https://github.com/user-attachments/assets/dad3926b-6031-4f60-9dff-0767aa0ae358)

        The ROC curves are generating AUC near 90%, it suggests that the gene expression can be classified by features, which contains hidden stop codon producing codon usage ratio as feature values in case of Frame-shift +1. We can say that codon usage in a gene depends on gene expression to avoid Frame-shift +1. And also, our previous results shows that hidden stop codon producing codon pairs are used more than other synonymous codons in case of frame-shift +1. The table suggests the classifiers are correctly predicting the highly expression genes and low expression genes. 

       From this analysis we can say that codon usage is not random in genes. Codons are selected in highly expressive genes to avoid Frame-shift +1 mutation. 

       For better understanding and validation, we use feature selection and calculate feature importance score and ranking and arrange them in ascending order. From there we pick up 10 best features and 10 worst features and implement the classification model to them. 

        a. For best 10 features:

         ![image](https://github.com/user-attachments/assets/a832d6c4-cc4e-4513-a0a3-41d8727cb36c)
       
         ![image](https://github.com/user-attachments/assets/ff456fd7-e703-447a-8db3-fcfdb3570a14)

        b. For worst 10 features:

         ![image](https://github.com/user-attachments/assets/9c6ca7ab-b64b-476d-bdcb-e1869eeb0e6f)

         ![image](https://github.com/user-attachments/assets/9e68d608-5c4f-4a2d-b12d-4292d7411f04)

        We can observe a significant difference about 25% between best feature’s AUC percentage and worst feature’s AUC percentage in Figure best & worst feature and classification performance is also better in high expression genes as shown in Tables. From this we can say that all the hidden stop codon producing amino acid pairs are not utilized equally only a few hidden stop-codon producing amino acid pairs are selected for the gene sequence latter on which can produce stop codon in frame-shift +1 mutation scenario. 
         
   2. For Frame Shift -1:

       We implement binary classification model for FS -1 dataset and calculate accuracy, true positive rate and false positive rate and then we plot the ROC curves with AUC percentage for different classifiers.
       
       ![image](https://github.com/user-attachments/assets/b0a93c73-f755-4ec3-ac58-d7e7a22cb033)

       ![image](https://github.com/user-attachments/assets/db526df9-8f51-4bee-85d0-99bbbfecc872)

      As we can see in the figure, the most of the classifiers are generating ROC curves with AUC more than 90%, it suggests that the gene expression can be classified by features, which contains hidden stop codon producing codon usage ratio as feature values in case of Frame-shift -1. We can say that codon usage in a gene depends on gene expression to avoid Frame-shift -1. And also, our previous result shows that hidden stop codon producing codon pairs are used more than other synonymous codons in case of frame-shift -1. The table suggests the classifiers are correctly predicting the highly expression genes and low expression genes. 

      From this analysis we can say that codon usage is not random in genes. Codons are selected in highly expressive genes to avoid Frame-shift -1 mutation. 

      For better understanding and validation, we use feature selection and calculate feature importance score and ranking and arrange them in ascending order. From there we pick up 20 best features and 20 worst features and implement the classification model to them.
   
      a. For best 20 features:

      ![image](https://github.com/user-attachments/assets/66146ab8-9b11-4727-9b81-1a373ea70f43)

      ![image](https://github.com/user-attachments/assets/e9f68f44-5137-49a0-80a4-65df7476f3ef)


      b. For worst 20 features:

      ![image](https://github.com/user-attachments/assets/c572a303-452e-46fa-beda-5ba4fb19cacf)

   
      ![image](https://github.com/user-attachments/assets/73b63302-138c-4b81-a338-9fbd798c981a)

      We can observe a significant difference about 40% between best feature’s AUC percentage and worst feature’s AUC percentage in Figure best & worst feature and classification performance is also better in high expression genes as shown in Tables. From this we can say that all the hidden stop codon producing amino acid pairs are not utilized equally only a few hidden stop-codon producing amino acid pairs are selected for the gene sequence latter on which can produce stop codon in frame-shift -1 mutation scenario. 

## Conclusion
Theoretically, there are 1.5 x 1084 possible ways of generating a codon table with 64 codons. But out of all nature has adopted the most unique and precise one to encode amino acids. There are various mechanisms through which nature reduces the effect of mutations inside an organism. In this project, we try to understand provision of reducing impact of frame shift mutations in E. coli genome. Our classification result suggests that the codon usage in essential/high-expression genes are different from non-essential/low-expression genes with regard to generation of hidden stop codons. Our result strongly supports the “Ambush hypothesis” that says the hidden stop codons are not random they are selected sometimes. On the basis of our work, we can say codon selection depends on Gene Type (Essential/Non-essential) and Gene Expression level.
      

