# [Building] Rethinking Protein Drug Design with Highly Accurate Structure Prediction of Anti-CRISPR Proteins

**Contact**: Hyunjin.Shim@ghent.ac.kr

**Contributors**:
 - [Ho-min Park](https://github.com/powersimmani)
 - [Yunseol Park](https://github.com/YunseolPark)
 - [Joris Vankerschaver](https://github.com/jvkersch)
 - [Arnout Van Messem](https://github.com/avmessem)
 - [Wesley De Neve](https://github.com/wmdeneve)
 - [Hyunjin Shim]()

### Introduction

<p align="center">
  <img src="example.png" width=100% height=100%>
  <figcaption align = "center"><b>Fig.1 - Predicted protein structure and the corresponding superimposed image with ground truth for 0272 and 0153 </b></figcaption>
</p>

Anti-CRISPR (Acr) proteins are the defence mechanism of bacteriophages to counter the prokaryotic adaptive immunity, CRISPR-Cas systems. They are natural protein therapeutics that could be used for future drug design. Furthermore, they can be used as a countermeasure against CRISPR-Cas9 gene editing technology, which has off-target problems at the moment.

~~CRISPR-Cas9 gene editing technology has been widely applied to improve the traits of animals and plants, to treat diseases, and to exterminate pests. However, its stability has been pointed out due to the off-target problem of targeting an unintended part. Anti-CRISPR (Acr) is a protein that controls CRISPR and is attracting attention as a countermeasure against the side effects of gene editing technology.~~

Structural and functional analysis of these Acr proteins is essential for them to be used for drug design or in any other capacity. Currently, advanced equipments such as X-ray crystallography, NMR spectroscopy, and cryo-electron microscopy are used to visualize the structure of proteins. These methods are highly accurate, but they can be very time consuming and expensive. To overcome these disadvantages, prediction of protein structures via machine learning has gained a lot of attention as of late. The Critical Assessment of protein Structure Prediction (CASP), for example, is a competition for predicting protein 3-D structures from their sequences. In the 14th CASP contest, AlphaFold from Google Deepmind achieved highely accurate molecular localization of a variety of proteins and won the contest. AlphaFold can predict protein structures in a matter of hours, which would normally take months in a wet lab.

~~Structural biology uses advanced equipment such as X-ray crystallography, NMR spectroscopy, and cryo-electron microscopy to characterize the elemental positions of proteins and other important molecules and share the results with wwPDB. Using such advanced equipment can get very accurate values, but on the contrary, it has the disadvantage of having to invest a lot of money and time to obtain a single structure. The Critical Assessment of protein Structure Prediction (CASP) is a competition for predicting 3-D structures from protein sequences. In the recent 14th contest, AlphaFold from Google Deepmind won the protein contest. AlphaFold has achieved highely accurate molecular localization of a variety of proteins in a matter of hours, which would normally take monthes.~~

In our study, we present a wide variety of protein-manipulating strategies of Acr proteins for future protein drug design as well as a novel family of Acr proteins which are structurally homologous to the recently-discovered mechanism of manipulating host proteins through enzymatic activity, rather than through direct inference. For this, we make use of the aforementioned AlphaFold to predict the 3-D structures of Acr proteins and perform structural and sequence analysis using the results.

~~In our study, we use AlphaFold to predict the 3-D structure of Acr, which has recently attracted attention, and perform structural and sequence analysis.~~

Through this github repository, we share the predicted 3-D structures and sequences of Acr proteins used in our study. We do this for researchers conducting related research, to encourage them to cross-verify the structures predicted by AlphaFold, and to help minimize their time and effort in similar studies. 

~~This github shares the predicted 3-D structure and sequence of anti-CRISPR used in this study and captured images. This is to encourage researchers conducting related research to cross verify the structure predicted by AlphaFold, and to help minimize the resources and time required for related research by preventing repeated predictions of similar sequences.~~

All Acr protein sequences were provided by [anti-CRISPRdb](http://guolab.whu.edu.cn/anti-CRISPRdb/) and they have been divided into three sets: Set A, B and C. Set A contains proteins that have been verified as being Acr proteins via the database and their 3-D structures have been discovered in literature. Set B contains proteins that have been verified as being Acr proteins via the database but their 3-D structures have not been discovered. Lastly, Set C contains proteins that has not been verified yet as being Acr proteins but their 3-D structures have been discovered. 

~~All Acr protein sequences were provided by anti-CRISPRdb[] and they are divided into Set A, B and C. Set A includes verified acr from Database and Literature. In other words, Set A is definitely acr and at the same time there is a corresponding 3-D structure. Set B is a set that has been verified in Databse, but does not yet have a corresponding 3-D structure. The final set C is a set containing a protein that has a corresponding 3-D structure but has not yet been identified as an Acr.~~


### Our GitHub largely has the following structure:

#### 1. [`protein_sequences`](https://github.com/powersimmani/ACR_alphafold/tree/main/protein_sequences)
- The input protein sequences required for prediction via AlphaFold are stored here. 

#### 2. [`pdb_files`](https://github.com/powersimmani/ACR_alphafold/tree/main/pdb_files)
- [`Alphafold_pdbs_from_protein_sequences`](https://github.com/powersimmani/ACR_alphafold/tree/main/pdb_files/Alphafold_pdbs_from_protein_sequences): The predicted 3-D structures from the input protein sequences are saved here. 
- [`Ground_truth_pdb_files`](https://github.com/powersimmani/ACR_alphafold/tree/main/pdb_files/Ground_truth_pdb_files): The ground truth 3-D structures corresponding to the predicted 3-D structures are stored here. 

#### 3. [`predict_and_ground_truth_matching.xlsx`](https://github.com/powersimmani/ACR_alphafold/blob/main/predict_and_ground_truth_matching.xlsx)
- The information about which `Ground_truth_pdb` matches `Alphafold_pdbs_from_protein_sequences` is saved here. 

#### 4. [`captured_images`](https://github.com/powersimmani/ACR_alphafold/tree/main/captured_images)
- Screenshots are saved for every 3-D structure.
- [`Super_imposed`](https://github.com/powersimmani/ACR_alphafold/tree/main/captured_images/Super_imposed): Screenshots of (overlapped) predictions and ground truth is saved here.

 

## Additional information

Additional structures, not used in this study can be found in [Set D](link)

## Full prediction result with features

For the full results from AlphaFold, download the [file](link) and unzip it.

## For citation

Readers may use the following information to cite our research and dataset.

_**<citation to be added here>**_

**Please feel free to contact us using 'issues' or the following email address: Hyunjin.Shim@ghent.ac.kr**

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

