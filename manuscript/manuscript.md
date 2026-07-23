# Title

A Hierarchical Bayesian Analysis of Memory Load Effects on Visual Working Memory Precision

# Abstract

Visual working memory is limited in both capacity and precision, and computational models increasingly aim to characterize how memory representations vary with increasing load and across individuals. The present study applied hierarchical Bayesian modeling to a publicly available continuous-report visual working-memory dataset to examine the relationship between memory load and precision while comparing alternative statistical representations of performance. Trial-level angular errors from three experiments were analyzed using Bayesian models with von Mises likelihoods. The evaluated models included a null hierarchical model with no memory-load effect, a hierarchical model estimating a population-level effect of set size with participant-specific variation, and a nonlinear hierarchical model allowing independent set-size effects through a sum-to-zero parameterization. Model performance was evaluated using posterior predictive checks, convergence diagnostics, and approximate leave-one-out cross-validation.

Results showed that memory precision decreased systematically as memory load increased and that participants exhibited substantial differences in baseline precision. The nonlinear hierarchical model achieved the strongest predictive performance among the evaluated models, indicating that the relationship between memory load and precision was not fully captured by a simple linear representation. Robustness analyses demonstrated that the primary conclusions remained stable across alternative prior specifications, sampling configurations, and posterior initializations. These findings highlight the value of hierarchical Bayesian approaches for modeling individual variability in visual working-memory performance and demonstrate the utility of reproducible computational workflows for evaluating statistical models using open behavioral datasets.

**Keywords:** Visual working memory, Bayesian modeling, hierarchical models, continuous report, memory precision, computational cognitive science


# Introduction

Visual working memory enables the temporary maintenance and manipulation of visual information to support ongoing perception, reasoning, and goal-directed behavior. Despite its central role in cognition, visual working memory is markedly limited in both capacity and precision. Understanding these limitations has been a major objective of cognitive psychology and cognitive neuroscience for several decades (Luck & Vogel, 1997). A central question concerns whether performance limitations arise from a fixed number of stored representations, a limited resource shared across items, or probabilistic mechanisms determining the fidelity of memory representations.

Early influential accounts proposed that visual working memory consists of a small number of discrete storage slots that maintain representations with relatively fixed precision (Luck & Vogel, 1997; Zhang & Luck, 2008). Under this framework, increasing the number of memorized items mainly reduces the probability that an item is successfully stored, whereas the precision of stored representations remains largely unchanged. Although these models successfully explained many experimental findings, subsequent evidence suggested that memory performance often changes gradually rather than categorically as memory load increases, motivating alternative theoretical accounts.

Resource-based theories instead propose that visual working memory relies on a limited representational resource that is continuously distributed across remembered items (Bays & Husain, 2009). As memory load increases, fewer resources are available for each representation, leading to progressively lower memory precision. Continuous-report paradigms have been especially influential in evaluating these accounts because they provide a sensitive measure of representational fidelity. Rather than requiring binary correct-or-incorrect responses, participants reproduce a remembered stimulus feature, such as a color or orientation, on a continuous response scale. The resulting angular error provides a behavioral measure of representational precision across experimental conditions and has become a standard behavioral measure in computational studies of visual working memory (Bays & Husain, 2009; Zhang & Luck, 2008).

Subsequent theoretical developments have further suggested that memory precision itself varies across trials and items rather than remaining constant. Variable-precision models propose that the representational resources allocated to individual memories fluctuate over time, producing systematic variability in recall precision even under identical experimental conditions (van den Berg et al., 2012). More broadly, contemporary perspectives increasingly characterize visual working memory as a probabilistic representational system in which uncertainty and variability are fundamental properties of memory representations rather than merely sources of measurement error (Ma et al., 2014; Bays, 2022; Bays, 2024).

These theoretical developments have been accompanied by increasing use of computational modeling to evaluate competing explanations of behavioral performance. Bayesian methods are well suited for this purpose because they estimate complete posterior distributions over model parameters while naturally quantifying uncertainty. Hierarchical Bayesian models additionally account for the multilevel structure of behavioral data by simultaneously estimating population-level effects and participant-specific variation through partial pooling. This approach generally produces more stable parameter estimates than fitting separate models to individual participants while preserving meaningful individual differences in cognitive performance. The Bayesian workflow further emphasizes model criticism and predictive evaluation through posterior predictive checks, convergence diagnostics, and out-of-sample model comparison rather than relying solely on statistical significance (Gelman et al., 2020).

Although computational models are frequently used to evaluate theories of visual working memory, it is important to distinguish statistical model parameterizations from cognitive theories. A statistical model provides a quantitative description of observed behavior under a particular set of assumptions, whereas a cognitive theory proposes mechanisms that generate that behavior. Consequently, demonstrating that one statistical model predicts behavioral data better than another does not by itself establish superiority of one cognitive theory over competing theoretical accounts. Instead, statistical models provide a principled framework for quantifying behavioral regularities and evaluating alternative representations of the data.

The increasing availability of openly accessible behavioral datasets has created new opportunities for reproducible computational research. Public datasets enable independent evaluation of modeling approaches using standardized experimental paradigms while promoting transparency and cumulative scientific progress. Continuous-report datasets are particularly valuable because they provide trial-level measurements of memory precision across multiple memory loads, making them well suited for hierarchical Bayesian analyses that simultaneously examine population-level effects and individual differences.

The present study applied hierarchical Bayesian analysis to a publicly available continuous-report dataset originally reported by van den Berg et al. (2012). The primary objective of this study is methodological: to evaluate alternative Bayesian statistical models of memory precision using a publicly available continuous-report dataset. Specifically, the study evaluates a sequence of progressively more flexible hierarchical Bayesian models that differ in how the relationship between memory load and memory precision is parameterized. A null model serves as a baseline by assuming no effect of memory load. A hierarchical linear model estimates a population-level effect of memory load while accounting for participant-specific variability. Finally, a nonlinear hierarchical model allows memory-load effects to vary freely across set sizes without assuming a linear relationship. These models should be interpreted as alternative statistical models of the same behavioral data rather than as competing cognitive theories of visual working memory. Model performance was evaluated using leave-one-out cross-validation together with posterior predictive checks and standard Bayesian convergence diagnostics.

The study addressed three primary research questions. First, does memory precision decrease systematically as memory load increases? Second, to what extent do individuals differ in their baseline levels of memory precision? Third, does increasing statistical flexibility improve predictive performance when modeling continuous-report behavioral data? Based on previous findings from resource-based and variable-precision theories (Bays & Husain, 2009; van den Berg et al., 2012), it was hypothesized that memory precision would decline with increasing set size, substantial individual differences in baseline precision would be observed, and the nonlinear hierarchical model would provide the best predictive performance among the statistical models considered.

# Methods

## Dataset

The dataset analyzed in this study consists of individual trial-level responses from three continuous-report experiments originally reported by van den Berg et al. (2012) and distributed through the BenchmarksWM repository (Dutli et al., 2024). The experiments examined the relationship between memory load and visual working memory precision. They differed in stimulus type and response procedure while sharing a common delayed-estimation paradigm. Experiment 1 employed colored stimuli with a scrolling response method, Experiment 2 used oriented stimuli with a rotational response, and Experiment S3 used colored stimuli with a color-wheel response.

The complete dataset comprised 37,824 trials collected from 13 unique participants across 32 participant–experiment units. Memory load was manipulated by varying set size from one to eight items. On each trial, participants reproduced the remembered feature value of a target stimulus, allowing memory precision to be quantified as angular reproduction error. Because the study analyzed an existing public dataset, no additional ethical approval or participant recruitment was required.

## Measures

The primary descriptive outcome variable was absolute angular error expressed in radians. Absolute angular error was computed as the absolute value of the signed circular deviation between the target feature and the participant’s response, yielding values between 0 and π radians. Absolute angular error was used for descriptive summaries and visualizations because these analyses focused on the magnitude of recall error rather than its direction.

The principal predictor was memory load, defined as set size. Participant identity was included to account for repeated observations and individual differences in baseline memory precision. Experiment identifiers were retained throughout preprocessing and descriptive analyses but were not included as predictors in the primary hierarchical models because the objective was to evaluate the general relationship between memory load and memory precision across the combined dataset.

Pooling the experiments increased statistical efficiency for evaluating the general relationship between memory load and memory precision. Experiment-specific analyses were conducted as robustness checks to assess whether the principal conclusions remained consistent across the individual experiments.

## Data Processing

All preprocessing and validation procedures were implemented in Python using a fully reproducible analysis pipeline. The raw dataset was first validated to ensure consistency of variable names, data types, and expected value ranges. Additional quality-control procedures verified the absence of missing observations, duplicated records, and duplicate participant–trial identifiers.

Participant identifiers were encoded numerically for Bayesian modeling, and observations were organized according to experiment, participant, and trial identifiers to ensure consistent ordering throughout subsequent analyses. Circular error measurements supplied by the original dataset were used directly without additional transformation. No observations or participants were excluded because all records passed all validation checks.

## Statistical Analysis

Descriptive analyses summarized the distribution of memory errors across participants, experiments, and memory loads. Summary statistics included means, medians, standard deviations, and trial counts. Because memory errors are circular measurements, circular descriptive statistics, including the circular mean, circular variance, and circular standard deviation, were additionally computed to characterize the overall distribution of response errors.

Behavioral performance across memory loads was summarized by calculating mean error at each set size. Participant-level summaries were generated to quantify individual variability in baseline memory precision. These descriptive analyses served both as an overview of the dataset and as a basis for evaluating the adequacy of the Bayesian models.

## Bayesian Models

The primary analyses employed hierarchical Bayesian modeling to estimate the relationship between memory load and memory precision while accounting for repeated observations within participants. All models used the von Mises distribution as the likelihood because angular errors constitute circular data. Although descriptive analyses used absolute angular error, the Bayesian models were fitted to the signed circular error using a von Mises likelihood.

The models estimated the logarithm of the von Mises concentration parameter, which was exponentiated to obtain κ. Larger values of κ correspond to greater memory precision. Consequently, model-based inferences about precision are expressed in terms of κ rather than the observed error itself. Model parameters were estimated using Markov chain Monte Carlo sampling implemented in PyMC.

Three models of increasing statistical flexibility were evaluated. These models were selected to examine how progressively richer representations of the relationship between memory load and memory precision influence predictive performance. The comparison was methodological rather than theoretical; the models represent alternative statistical descriptions of the observed behavioral data and should not be interpreted as competing cognitive theories of visual working memory.

### Null Model

The null model served as a baseline by assuming that memory precision remained constant across memory loads. Participant-specific intercepts were modeled hierarchically to capture individual differences in baseline precision, while no effect of set size was included. Consequently, any variation in performance across memory loads was left unexplained by the model.

### Hierarchical Linear Model

The hierarchical model extended the baseline model by introducing a population-level effect of memory load. Set size was mean-centered before analysis to improve parameter interpretability and sampling efficiency. Population-level parameters estimated the average baseline precision and the average linear effect of memory load, while participant-specific intercepts accounted for individual differences through partial pooling.

The concentration parameter of the von Mises distribution was modeled on the logarithmic scale, ensuring positive precision estimates while allowing memory precision to vary systematically with memory load. Participant-specific intercepts were modeled using a hierarchical normal distribution, allowing individual differences in baseline precision to be estimated while sharing information across participants. Weakly informative normal priors were assigned to the population intercept and memory-load coefficient, and a half-normal prior was used for the between-participant standard deviation.

### Nonlinear Hierarchical Model

The nonlinear model relaxed the assumption of a linear relationship between memory load and memory precision by estimating a separate effect for each set size. Rather than imposing a predetermined functional form, each memory load was allowed to contribute a separate effect to the expected precision.

Participant effects were parameterized using a noncentered hierarchical formulation to improve sampling efficiency and reduce posterior correlations. Specifically, participant-specific baseline precision parameters were modeled as deviations from the population-level intercept scaled by the between-participant variability.

Set-size effects were represented through unconstrained parameters that were transformed using a sum-to-zero constraint. This parameterization ensured that the population intercept represented the overall average level of precision while allowing each set size to deviate from that average without introducing parameter redundancy. The resulting model provides a flexible statistical description of nonlinear changes in memory precision while maintaining parameter identifiability.

## Model Fitting

Posterior distributions were estimated using the No-U-Turn Sampler (NUTS). Sampling was performed using the NumPyro backend within PyMC to improve computational efficiency. All models were fitted using four independent Markov chains with 1,000 tuning iterations.

The null and hierarchical models were sampled for 1,000 posterior draws per chain, whereas the nonlinear model was sampled for 2,000 posterior draws per chain with the same number of tuning iterations. A target acceptance probability of 0.95 and adaptive diagonal initialization were specified to improve sampling stability. Independent random seeds were used for robustness analyses to evaluate posterior stability across repeated model fits.

## Model Evaluation

Model convergence was evaluated using the potential scale reduction statistic (R-hat), effective sample size (ESS), trace plots, and rank plots. Posterior predictive checks were used to assess the ability of each model to reproduce the principal characteristics of the observed behavioral data, including overall error distributions, memory-load effects, and participant-level variability.

Predictive performance was compared using approximate leave-one-out cross-validation (LOO). Differences in expected log predictive density were used to evaluate relative predictive accuracy across models. Pareto-k diagnostics were also examined to identify influential observations and verify the reliability of the LOO estimates.

## Robustness Analyses

Several robustness analyses were conducted to evaluate the stability of the Bayesian inferences. Prior sensitivity analyses assessed whether posterior estimates remained consistent under alternative prior specifications. Sampling sensitivity analyses examined the effects of different sampling configurations, including longer tuning periods and higher target acceptance probabilities. Posterior stability was evaluated by fitting the primary hierarchical model using multiple random seeds and comparing the resulting posterior estimates.

Experiment-specific robustness analyses were additionally performed by fitting the hierarchical model separately within each experiment to determine whether the estimated memory-load effect remained consistent across datasets. Together, these analyses provided complementary evidence regarding the robustness of the estimated effects and the stability of the computational workflow.

# Results

## Dataset Overview

The final dataset comprised 37,824 trial-level observations obtained from three previously published continuous-report experiments involving 13 unique participants (32 participant–experiment units). All preprocessing and validation procedures were completed successfully, and no additional exclusions were required. Memory load ranged from one to eight items, with observations collected across all set sizes, providing balanced coverage across the experimental conditions.

## Behavioral Results

Descriptive analyses showed that memory error increased as memory load increased. The distribution of angular error was concentrated near zero for smaller set sizes but became progressively broader at larger set sizes. The relationship between set size and mean angular error demonstrated a consistent increase in response error with increasing memory load, corresponding to a decrease in memory precision.

Participant-level summaries also revealed substantial variability in baseline precision across individuals. Although participants differed in their overall levels of precision, the pattern of increasing error with increasing set size was consistently observed across the combined dataset.

## Hierarchical Bayesian Models

Three Bayesian models were fitted to the continuous-report data: a null model assuming constant memory precision across memory loads, a hierarchical linear model estimating a population-level effect of set size while accounting for participant-specific variability, and a nonlinear hierarchical model allowing independent effects for each set size.

Posterior estimates from the hierarchical model indicated a clear negative association between memory load and memory precision. The population intercept was estimated as α = 0.827 (95% HDI [0.619, 1.017]), the population effect of set size as β = -0.336 (95% HDI [-0.343, -0.329]), and the between-participant standard deviation as σα = 0.368 (95% HDI [0.236, 0.529]). The 95% HDI for β was entirely below zero, indicating strong posterior support for a negative association between memory load and the von Mises concentration parameter. Posterior summaries for the population parameters are reported in the corresponding model summary table.

The nonlinear model estimated separate effects for each set size using a sum-to-zero parameterization. Posterior estimates for the set-size effects varied systematically across set sizes, with the estimated deviations ranging from 1.364 (95% HDI [1.327, 1.398]) for set size 1 to -0.933 (95% HDI [-0.975, -0.891]) for set size 8.

These results indicate that memory precision decreased systematically across increasing memory loads and that the relationship between set size and precision was not fully captured by a single linear effect.

## Individual Differences

Participant-level posterior means and 95% HDIs demonstrated substantial variability in baseline memory precision. Baseline precision estimates ranged considerably across participants, indicating meaningful individual differences in visual working memory precision after accounting for the effect of memory load.

The hierarchical model accounted for this variability through partial pooling, allowing participant-specific estimates while borrowing information from the full sample. Participant-level posterior predictive checks further demonstrated that the hierarchical model reproduced individual differences in observed error patterns, indicating that the model captured both population-level effects and variability across participants.

## Model Evaluation

Posterior predictive checks indicated good agreement between the fitted models and the observed data. The posterior predictive distributions reproduced the overall distribution of response errors as well as the observed relationship between memory load and mean error across set sizes, suggesting that the hierarchical model adequately captured the principal characteristics of the behavioral data.

All Bayesian models converged successfully. All monitored parameters achieved R-hat ≤ 1.01, indicating successful convergence across Markov chains. For the nonlinear model, the minimum bulk ESS exceeded 954 and the minimum tail ESS exceeded 1,236, indicating adequate posterior exploration. Trace plots and rank plots likewise showed good chain mixing and no evidence of sampling pathologies.

## Model Comparison

Leave-one-out cross-validation favored the nonlinear model over both simpler alternatives. The nonlinear model achieved the highest expected log predictive density (ELPD_LOO = -42,771.49), followed by the hierarchical model (ELPD_LOO = -42,938.84; ΔELPD = 167.35) and the null model (ELPD_LOO = -47,830.95; ΔELPD = 5,059.47).

Stacking weights likewise favored the nonlinear model (0.871), whereas the hierarchical (0.070) and null (0.059) models received substantially less support. Pareto-k diagnostics indicated reliable leave-one-out estimates for all models, with maximum Pareto-k values below 0.30 and no observations exceeding the conventional thresholds of 0.7 or 1.0.

Posterior estimates from the nonlinear model indicated systematic changes in precision across memory loads. Because these parameters were estimated under a sum-to-zero constraint, they represent relative deviations from the population mean rather than absolute precision levels.

Together, the model comparison results indicate that a nonlinear representation of memory-load effects provided superior predictive performance compared with a linear effect of set size or a model without memory-load effects.

# Acknowledgements

This study used publicly available data from the BenchmarksWM repository. I thank the original contributors for making the dataset accessible and supporting open research practices. I also acknowledge the open-source scientific computing community and the Python ecosystem, including the tools that enabled data processing, statistical analysis, visualization, and reproducible computational modeling.

# Data and Code Availability

The dataset analyzed in this study is publicly available through the BenchmarksWM repository. All analysis scripts, processed data files, generated figures, supplementary materials, manuscript source files, and computational environment details are available in the project repository:

https://github.com/erfanjaripour/hierarchical-bayesian-working-memory

The repository also includes software versions, computational environment specifications, and reproducibility materials required to reproduce the analyses. The computational workflow was developed to support transparent and reproducible research.

# References

Bays, P. M., Catalao, R. F. G., & Husain, M. (2009). The precision of visual working memory is set by allocation of a shared resource. *Journal of Vision, 9*(10), 7–11. https://doi.org/10.1167/9.10.7

Bays, P. M., Ma, W. J., & Schneegans, S. (2022). Representation and computation in working memory. *Nature Reviews Neuroscience, 23*, 385–401. https://doi.org/10.1038/s41583-022-00573-0

Bays, P. M., Schneegans, S., Ma, W. J., & Brady, T. F. (2024). Theories of visual working memory: The state of the art. *Nature Human Behaviour, 8*, 1–17. https://doi.org/10.1038/s41562-024-01802-9

Dutli, J. (2024). *BenchmarksWM: Benchmark datasets for short-term and working memory models* [GitHub repository; R package]. https://github.com/joschadutli/BenchmarksWM

Gelman, A., Vehtari, A., Simpson, D., Margossian, C. C., Carpenter, B., Yao, Y., Kennedy, L., Gabry, J., Bürkner, P.-C., & Modrák, M. (2020). Bayesian workflow. *arXiv*. https://doi.org/10.48550/arXiv.2011.01808

Luck, S. J., & Vogel, E. K. (1997). The capacity of visual working memory for features and conjunctions. *Nature, 390*, 279–281. https://doi.org/10.1038/36846

Ma, W. J., Husain, M., & Bays, P. M. (2014). Changing concepts of working memory. *Nature Neuroscience, 17*, 347–356. https://doi.org/10.1038/nn.3655

van den Berg, R., Shin, H., Chou, W.-C., George, R., Ma, W. J., & Wiesman, A. (2012). Variability in encoding precision accounts for visual short-term memory limitations. *Proceedings of the National Academy of Sciences, 109*(22), 8780–8785. https://doi.org/10.1073/pnas.0908002107

Zhang, W., & Luck, S. J. (2008). Discrete fixed-resolution representations in visual working memory. *Nature, 453*, 233–235. https://doi.org/10.1038/nature06860