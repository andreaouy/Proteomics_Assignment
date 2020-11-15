# -*- coding: utf-8 -*-
“””bioinfoProteomicsHW4.ipynb
# Loading CPTAC Data in google colab using a Python package developed in the Payne lab at BYU.
"""
#install and import cptac and other python packages (just pandas in this case)
!pip install -q cptac  
import cptac 
import pandas as pd

#download endometrial data and creates a new endometrial class
cptac.download(dataset="Endometrial")
en = cptac.Endometrial()

#obtain proteomic data (enProt) and patient information (enInfo)
enProt = en.get_proteomics()
enInfo = en.get_clinical()

#i used google colab to do this, so need to mount my drive to be able to export the data
from google.colab import drive
drive.mount('drive') 

#save proteome and clinical information tables to export and work on locally/in another language
enProt.to_csv("enProt.csv")
!cp enProt.csv "drive/My Drive"
enInfo.to_csv("enInfo.csv")
!cp enInfo.csv "drive/My Drive"