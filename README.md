# [Building] Rethinking protein drug design with highly accurate structure prediction of anti-CRISPR proteins

<p align="center">
  <img src="example.png" width=100% height=100%>
</p>


CRISPR-Cas9 gene editing technology has been widely applied to improve the traits of animals and plants, to treat diseases, and to exterminate pests. However, its stability has been pointed out due to the off-target problem of targeting an unintended part. Anti-CRISPR (Acr) is a protein that controls CRISPR and is attracting attention as a countermeasure against the side effects of gene editing technology. 


Structural biology uses advanced equipment such as X-ray crystallography, NMR spectroscopy, and cryo-electron microscopy to characterize the elemental positions of proteins and other important molecules and share the results with wwPDB. Using such advanced equipment can get very accurate values, but on the contrary, it has the disadvantage of having to invest a lot of money and time to obtain a single structure. The Critical Assessment of protein Structure Prediction (CASP) is a competition for predicting 3-D structures from protein sequences. In the recent 14th contest, AlphaFold from Google Deepmind won the protein contest. AlphaFold has achieved highely accurate molecular localization of a variety of proteins in a matter of hours, which would normally take monthes. 

In our study, we use AlphaFold to predict the 3-D structure of Acr, which has recently attracted attention, and perform structural and sequence analysis. 

This github shares the predicted 3-D structure and sequence of anti-CRISPR used in this study and captured images. This is to encourage researchers conducting related research to cross verify the structure predicted by AlphaFold, and to help minimize the resources and time required for related research by preventing repeated predictions of similar sequences. 


All Acr protein sequences were provided by anti-CRISPRdb[] and they are divided into Set A, B and C. Set A includes verified acr from Database and Literature. In other words, Set A is definitely acr and at the same time there is a corresponding 3-D structure. Set B is a set that has been verified in Databse, but does not yet have a corresponding 3-D structure. The final set C is a set containing a protein that has a corresponding 3-D structure but has not yet been identified as an Acr. 




### Our GitHub largely has the following hierarchy structure. 

#### 1. protein_sequences
- The input protein sequence required for prediction using AlphaFold is stored. 

#### 2. pdb_files
- Alphafold_pdbs_from_protein_sequences: The predicted 3-D structure from the protein sequence is saved. 
- Ground_truth_pdb_files: The correct answer corresponding to the predicted 3-D structure is stored. 

#### 3. predict_and_ground_truth_matching.xlsx
- Contains information about which Ground_truth_pdb matches Alphafold_pdbs_from_protein_sequences. 


#### 4. captured_images
- Screenshots are saved for every 3-D structures.
- *Super_imposed: Saved screenshots of (overlapped) predictions and ground truth. 

 

## Additional informations

More structures (Set D): https://github.com/powersimmani/??

## Full prediction result with features

For checking the whole results of AlphaFold, please download the file through the following link, unzip it

## For citation

Readers may use the following information to cite our research and the dataset.

??? Baek, J. Y., de Guzman, M. K., Park, H. M., Park, S., Shin, B., Velickovic, T. C., ... & De Neve, W. (2021). Developing a Segmentation Model for Microscopic Images of Microplastics Isolated from Clams. In Pattern Recognition. ICPR International Workshops and Challenges (pp. 86-97). Springer International Publishing.

**We also glad to get the new idea for this project. Please feel free to contact us using 'issues' or following email address: homin.park@ghent.ac.kr**

!!! This section will be updated when the expansive study is published.


## References
It will be updated soon 
-->
- Tool making: https://stackoverflow.com/questions/35508711/how-to-enable-pan-and-zoom-in-a-qgraphicsview
- MP-VAT: https://mpvat.wordpress.com/
- processing with image thresholding: 
- U-Net: Ronneberger, O., Fischer, P., & Brox, T. (2015, October). U-net: Convolutional networks for biomedical image segmentation. In International Conference on Medical image computing and computer-assisted intervention (pp. 234-241). Springer, Cham.


## Acknowledgement

The research and development activities described in this paper were funded by Ghent University Global Campus (GUGC).

