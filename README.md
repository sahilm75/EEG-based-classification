# Re-thinking EEG 

This repository aims to implement the ideas represented in the paper Re-thinking EEG-based non-invasive brain interfaces: modeling and analysis.

## Requirements
jupyter-notebook >= 6.0
python       >=  3.3
numpy        >=  1.20
scipy        >=  1.3
scikit-learn >=  1.0

## Setup
In order to view some of the EEG plots, you will need mne. The remaining packages used are fairly common. (See Requirements above)
 bash
pip3 install mne


## Running Instructions
Make sure you're in the directory containing the Readme.
Run
 bash
jupyter-notebook Democode.ipynb


All of the data required is already loaded in this directory. (Data taken from [here](http://bbci.de/competition/iii/)).

You should be able to step through the functions one by one in the python notebook. 

Since, estimation of *A, takes a long time, a previously estimated **A* has been cached in the file AdataL.npz in this directory. The lines for estimation of A have thus been commented out (Cell 20)

Citations:

@article{Gupta2018DealingWU,
 title={Dealing with Unknown Unknowns:Identification and 
 Selection of Minimal Sensing for Fractional Dynamics 
 with Unknown Inputs},
 author={Gaurav Gupta and S{\'e}rgio Pequito 
 and Paul Bogdan},
 journal={2018 Annual American Control Conference (ACC)},
 year={2018},
 pages={2814-2820}
}
