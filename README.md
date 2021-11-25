# [Building] Rethinking Protein Drug Design with Highly Accurate Structure Prediction of Anti-CRISPR Proteins

<p align="center">
  <img src="example.png" width=100% height=100%>
  <figcaption align = "center"><b>Fig.1 - Predicted protein structure and the corresponding superimposed image with ground truth for 0272 and 0153 </b></figcaption>
</p>

Anti-CRISPR (Acr) proteins are the defence mechanism of bacteriophages to counter the prokaryotic adaptive immunity, CRISPR-Cas systems ([Jansen et al. 2002][2]; [Mojica et al. 2005][4]). They are natural protein therapeutics that could be used for future drug design.

Structural and functional analysis of these Acr proteins is essential for them to be used for drug design or in any other capacity. Currently, advanced equipments such as X-ray crystallography, NMR spectroscopy, and cryo-electron microscopy are used to visualize the structure of proteins. These methods are highly accurate, but they can be very time consuming and expensive. To overcome these disadvantages, prediction of protein structures via machine learning has gained a lot of attention as of late. The Critical Assessment of protein Structure Prediction (CASP), for example, is a competition for predicting protein 3-D structures from their sequences. In the 14th CASP contest, AlphaFold ([Jumper et al. 2021][3]; [Callaway 2020][1]) from Google Deepmind achieved highely accurate molecular localization of a variety of proteins and won the contest. AlphaFold can predict protein structures in a matter of hours, which would normally take months in a wet lab.

In our study, we present a wide variety of protein-manipulating strategies of Acr proteins for future protein drug design as well as a novel family of Acr proteins which are structurally homologous to the recently-discovered mechanism of manipulating host proteins through enzymatic activity, rather than through direct inference. For this, we make use of the aforementioned AlphaFold to predict the 3-D structures of Acr proteins and perform structural and sequence analysis using the results.

Through this github repository, we share the predicted 3-D structures and sequences of Acr proteins used in our study. We do this for researchers conducting related research, to encourage them to cross-verify the structures predicted by AlphaFold, and to help minimize their time and effort in similar studies. 

All Acr protein sequences were provided by [anti-CRISPRdb](http://guolab.whu.edu.cn/anti-CRISPRdb/) and they have been divided into three sets: Set A, B and C. Set A contains proteins that have been verified as being Acr proteins via the database and their 3-D structures have been discovered in literature. Set B contains proteins that have been verified as being Acr proteins via the database but their 3-D structures have not been discovered. Lastly, Set C contains proteins that has not been verified yet as being Acr proteins but their 3-D structures have been discovered. 

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

_**citation to be added here**_

**Please feel free to contact us using 'issues' or the following email address: Hyunjin.Shim@ghent.ac.kr**

**Contributors**:
 - [Ho-min Park](https://github.com/powersimmani)
 - [Yunseol Park](https://github.com/YunseolPark)
 - [Joris Vankerschaver](https://github.com/jvkersch)
 - [Arnout Van Messem](https://github.com/avmessem)
 - [Wesley De Neve](https://github.com/wmdeneve)
 - [Hyunjin Shim]()

!!! This section will be updated when the expansive study is published.


## References
[‘It Will Change Everything’: DeepMind’s AI Makes Gigantic Leap in Solving Protein Structures.” Nature 588 (7837): 203–4.][1]

[Jansen, Ruud, Jan D. A. van Embden, Wim Gaastra, and Leo M. Schouls. 2002. “Identification of Genes That Are Associated with DNA Repeats in Prokaryotes.” Molecular Microbiology 43 (6): 1565–75.][2]

[Jumper, John, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, et al. 2021. “Highly Accurate Protein Structure Prediction with AlphaFold.” Nature 596 (7873): 583–89.][3]

[Mojica, Francisco J. M., César Díez-Villaseñor, Jesús García-Martínez, and Elena Soria. 2005. “Intervening Sequences of Regularly Spaced Prokaryotic Repeats Derive from Foreign Genetic Elements.” Journal of Molecular Evolution 60 (2): 174–82.][4]

[1]: https://link.springer.com/article/10.1007%2Fs00239-004-0046-3 "Callaway, Ewen. 2020. “‘It Will Change Everything’: DeepMind’s AI Makes Gigantic Leap in Solving Protein Structures.” Nature 588 (7837): 203–4."
[2]: https://onlinelibrary.wiley.com/doi/full/10.1046/j.1365-2958.2002.02839.x?sid=nlm%3Apubmed  "Jansen, Ruud, Jan D. A. van Embden, Wim Gaastra, and Leo M. Schouls. 2002. “Identification of Genes That Are Associated with DNA Repeats in Prokaryotes.” Molecular Microbiology 43 (6): 1565–75."
[3]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8371605/ "Jumper, John, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, et al. 2021. “Highly Accurate Protein Structure Prediction with AlphaFold.” Nature 596 (7873): 583–89."
[4]: https://link.springer.com/article/10.1007%2Fs00239-004-0046-3 "Mojica, Francisco J. M., César Díez-Villaseñor, Jesús García-Martínez, and Elena Soria. 2005. “Intervening Sequences of Regularly Spaced Prokaryotic Repeats Derive from Foreign Genetic Elements.” Journal of Molecular Evolution 60 (2): 174–82."



## Acknowledgement

The research and development activities described in this paper were funded by Ghent University Global Campus (GUGC).

