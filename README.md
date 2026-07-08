\# Stroop Interference: A Behavioral and Computational Analysis



\## Overview



This project investigates cognitive interference in the Stroop task using trial-level behavioral data from 81 participants. The analysis examines how congruent, neutral, and incongruent conditions affect reaction time and accuracy, with particular focus on the Stroop effect defined as the reaction time difference between incongruent and congruent trials.



The results show a strong interference effect, with slower responses in incongruent trials and faster responses in congruent trials. The project also includes participant-level analyses, robustness checks, and a simple computational model that reproduces the main behavioral pattern.



\## Research Question



How does cognitive interference influence reaction time and accuracy during Stroop task performance, and to what extent can a simple computational model reproduce the observed interference pattern?



\# Hypotheses

H1: Participants will show longer reaction times in incongruent trials than in congruent trials.

H2: Participants will show lower accuracy in incongruent trials than in congruent trials.





\## Dataset Source



The dataset used in this project is publicly available through the Open Science Framework and contains behavioral recordings from a Stroop task experiment. It includes trial-level reaction time and accuracy data collected across congruent, neutral, and incongruent conditions.



The data can be accessed at: OSF project page



This repository uses the openly shared dataset without modification of its original experimental structure, aside from preprocessing steps described in the Methods section.



\## Methods Summary



This project analyzes behavioral data from a Stroop task experiment to study cognitive interference within responses. The dataset contains reaction time and accuracy measurements collected in congruent, incongruent, and neutral conditions.



Data preprocessing included removing probe trials, excluding nan values or extreme reaction times, and resolving participant-session identifiers. After preprocessing, participant-level summary measures were computed for each condition.



The primary analysis examined the Stroop effect, defined as the difference in mean reaction time between incongruent and congruent trials. Descriptive statistics, paired-samples comparisons, effect size estimation, and confidence intervals were used to quantify interference effects. Additional robustness analyses and nonparametric tests were conducted to verify the stability of the findings. A simple computational simulation was also added to evaluate whether a baseline-plus-interference model could reproduce the observed behavioral patterns.



\## Key Results



The analysis included data from 81 participants who did the Stroop task in congruent, neutral, and incongruent conditions.



Reaction times followed the expected Stroop pattern. The fastest responses were in the congruent condition, and the slowest ones in the incongruent condition. It showed a clear cognitive interference.



The average Stroop effect was 0.106 seconds. It showed a significant increase in response time when the stimulus's meaning conflicted with the required response.



Paired-samples t-test showed a significant interference effect with t(80) = 17.77 and p = 1.67 × 10⁻²⁹.



The effect size was large (dz = 1.97). It showed a strong and reliable interference across participants.



Accuracy remained high across conditions, providing little evidence of a balance between response speed and accuracy.



Robustness checks supported the validity of the statistical analyses, with no substantial deviations from normality detected.



A simple additive model of interference reproduces the observed condition-level reaction time structure. It suggested that an additive interference mechanism can account for the main behavioral effects observed in the dataset.



\## Figure Preview



Figure 1 — Mean RT by Condition

Mean reaction times for congruent, incongruent, and neutral trials.



Figure 2 — RT Distribution by Condition

Participant-level reaction time distributions across experimental conditions.



Figure 3 — Stroop Effect Distribution

Distribution of participant-specific Stroop interference effects (incongruent − congruent RT).



Figure 4 — Baseline RT vs. Stroop Effect

Relationship between baseline processing speed and interference magnitude.



Figure 5 — Model vs. Data Comparison

Comparison of observed and simulated reaction time distributions.



\## Reproducibility



This project is fully reproducible under a standard Python scientific computing environment. The analysis pipeline is implemented through three Jupyter notebooks, each executed sequentially from top to bottom: an exploratory analysis notebook, a statistical analysis notebook, and a computational modeling notebook. Each notebook runs in a few seconds and produces both intermediate and final outputs.



All raw data must be manually placed in the data/raw/ directory prior to execution. The notebooks read directly from this location using local file paths. No external API calls or automatic downloads are required.



The workflow is deterministic. All statistical procedures and the simulation model use fixed computational procedures, ensuring identical outputs across runs. Each notebook generates and saves both figures and CSV output files, which are stored within the repository structure for downstream analysis and visualization.



\## Repository Structure



stroop-interference/

│

├── data/

│   ├── metadata/

│   ├── processed/

│   ├── raw/

│

│

├── figures/

│   ├──

│   ├── baseline-vs-effect.pdf

│   ├── baseline-vs-effect.png

│   ├── distribution-stroop-effects.pdf

│   ├── distribution-stroop-effects.png

│   ├── model-vs-data.pdf

│   ├── model-vs-data.png

│   ├── rt-by-condition.pdf

│   ├── rt-by-condition.png

│

├── manuscript/

│   ├── paper-draft.md

│

│

├── notebooks/

│   ├── 01-exploration.ipynb

│   ├── 02-analysis.ipynb

│   ├── 03-modeling.ipynb

│

│

├── results/

│   ├── assumption-checks.json

│   ├── descriptives.csv

│   ├── inferential-results.csv

│   ├── participant-qc.csv

│   ├── simulated-data.csv

│   ├── stroop-summary.json

│   ├── subject-level-stroop-effects.csv

│

│

├── .gitignore

├── README.md

└── requirements.txt

