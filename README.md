# A Hierarchical Bayesian Analysis of Memory Load Effects on Visual Working Memory Precision

## Overview

This project investigates how memory load influences visual working memory precision using trial-level data from a continuous-report task. The analysis examines whether increasing set size is associated with reduced memory precision and whether individual differences in precision can be captured using hierarchical Bayesian models.

The project applies Bayesian modeling to a publicly available visual working memory dataset originally reported by van den Berg et al. (2012). Three progressively flexible Bayesian models are evaluated: a null model, a hierarchical model with participant-level variability, and a nonlinear hierarchical model with set-size-specific effects.

The models are evaluated as alternative statistical descriptions of behavioral performance rather than competing cognitive theories of visual working memory. Model performance is compared using posterior predictive checks and out-of-sample predictive evaluation.

The results show that memory load is associated with systematic changes in precision and that the nonlinear hierarchical model provides the best predictive performance among the tested model formulations. Robustness analyses indicate that the main conclusions remain stable across alternative priors, sampling configurations, initialization settings, and experiment-specific analyses.

## Research Question

How does memory load affect visual working memory precision, and can hierarchical Bayesian models adequately characterize individual differences and set-size effects in continuous-report performance?

## Hypotheses

H1: Memory precision will decrease as memory load increases.

H2: Participants will show meaningful individual differences in baseline visual working memory precision.

H3: A more flexible hierarchical Bayesian model will provide better predictive performance than simpler alternative formulations.

## Dataset

### Dataset Source

The dataset analyzed in this project is the Visual Working Memory Continuous Report Dataset from van den Berg et al. (2012).

Original citation:

van den Berg, R., Shin, H., Chou, W. C., George, R., Ma, W. J., & Jehee, J. F. M. (2012). Variability in encoding precision accounts for visual short-term memory limitations. *Proceedings of the National Academy of Sciences, 109*(22), 8780–8785.

The dataset is publicly available through the BenchmarksWM R package:

https://github.com/joschadutli/BenchmarksWM

The original dataset identifier is:

`vandenberg12`

The dataset contains trial-level continuous-report responses from three experiments investigating visual working memory precision.

Experiments include:

* Exp1: Color memory with scrolling response
* Exp2: Orientation memory with rotation response
* ExpS3: Color memory with color wheel response

The repository uses the original dataset without modifying the experimental structure. All preprocessing steps are documented in the analysis workflow.

## Methods Summary

### Experimental Paradigm

The project analyzes continuous-report visual working memory tasks in which participants remember visual features under different memory loads and reproduce the target feature after a delay.

Memory performance is quantified using circular error, calculated as the angular difference between the target stimulus and participant response.

### Data Processing

Preprocessing includes:

* Validation of dataset structure
* Checking missing values and duplicated records
* Circular error transformations
* Participant and experiment indexing
* Generation of analysis-ready datasets

All preprocessing and analysis steps are implemented in Python.

### Bayesian Modeling

The analysis uses hierarchical Bayesian models with a von Mises likelihood for circular error distributions.

Three models are evaluated:

1. **Null model**

   A baseline model estimating participant-level precision without a memory-load effect.

2. **Hierarchical model**

   A model estimating:

   * Population-level precision
   * Memory-load effects
   * Participant-level variation through partial pooling

3. **Nonlinear hierarchical model**

   A more flexible model allowing memory-load effects to vary across set sizes using a sum-to-zero parameterization.

Models are fitted using Hamiltonian Monte Carlo sampling with the No-U-Turn Sampler (NUTS) implemented in PyMC.

Model evaluation includes:

* Posterior predictive checks
* Convergence diagnostics
* Effective sample size
* Rank plots
* Leave-one-out cross-validation

Robustness analyses examine:

* Prior sensitivity
* Sampling sensitivity
* Posterior stability
* Experiment-specific effects

## Results Summary

The analysis demonstrates a systematic relationship between memory load and visual working memory precision.

The hierarchical Bayesian models identified substantial individual differences in baseline precision across participants.

Model comparison using leave-one-out cross-validation favored the nonlinear hierarchical model over simpler alternatives, indicating that a more flexible set-size representation provided better predictive performance within the tested model family.

Posterior predictive checks showed that the selected model reproduced important characteristics of the observed error distributions.

Robustness analyses showed highly similar parameter estimates across alternative priors, sampling configurations, random seeds, and experiment-specific analyses.

## Reproducibility

This project is fully reproducible using a Python scientific computing environment.

The complete workflow includes:

1. Data preparation
2. Exploratory analysis
3. Bayesian model fitting
4. Posterior analysis
5. Model comparison
6. Figure and table generation

Detailed computational environment information, including software versions and dependencies, is provided in the repository environment files.

To reproduce the analysis:

1. Clone this repository.
2. Install the required Python environment.
3. Download and place the dataset in the appropriate data directory.
4. Execute the analysis notebooks in the documented order.

All generated figures, tables, and supplementary outputs can be reproduced from the analysis pipeline.

## Repository Structure

│

├── data/

│   ├── processed/

│   └── raw/

│

├── manuscript/

│   ├── manuscript.md

│   └── references.bib

│

├── notebooks/

│   ├── 01-data-inspection.ipynb

│   ├── 02-analysis.ipynb

│   └── 03-modeling.ipynb

│

├── results/

│   ├── figures/

│   └── tables/

│

├── src/

│   ├── __init__.py

│   ├── circular_statistics.py

│   ├── data_processing.py

│   ├── models.py

│   └── visualization.py

│

├── .gitignore

├── CITATION.cff

├── environment.yml

├── LICENSE

└── README.md

## Citation

If you use this repository, please cite the associated preprint:

[Preprint citation will be added after publication.]

The original dataset should also be cited:

van den Berg, R., Shin, H., Chou, W. C., George, R., Ma, W. J., & Jehee, J. F. M. (2012). Variability in encoding precision accounts for visual short-term memory limitations. *Proceedings of the National Academy of Sciences, 109*(22), 8780–8785.

## License

This repository contains original analysis code and materials developed for this project.

The original dataset is distributed according to the license specified by the BenchmarksWM repository.

Code and manuscript materials are released under the repository license specified below.