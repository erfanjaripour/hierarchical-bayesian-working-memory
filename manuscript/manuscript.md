# Title

A Hierarchical Bayesian Analysis of Memory Load Effects on Visual Working Memory Precision

# Abstract

Visual working memory is limited in both capacity and precision, but the mechanisms underlying these limitations remain actively debated. Computational models have increasingly shifted from discrete capacity accounts toward probabilistic frameworks that characterize memory precision and individual variability. The present study applied hierarchical Bayesian modeling to a publicly available continuous-report visual working-memory dataset to evaluate how memory precision changes with increasing memory load and to compare alternative computational explanations of performance. Trial-level angular errors from three experiments were analyzed using Bayesian models with von Mises likelihoods, including a null model, a hierarchical model estimating population-level and participant-specific effects, and a nonlinear model allowing memory-load effects to vary across set sizes. Model adequacy was assessed using posterior predictive checks, convergence diagnostics, and predictive model comparison using leave-one-out cross-validation. Results showed that memory precision decreased systematically with increasing memory load and that participants differed substantially in baseline precision. The nonlinear model provided a better predictive account of the observed data than simpler alternatives, suggesting that the relationship between memory load and precision was not fully captured by a simple linear representation. Sensitivity analyses demonstrated that the primary conclusions were robust across alternative prior specifications, sampling configurations, and random initializations. These findings demonstrate the utility of hierarchical Bayesian approaches for modeling variability in visual working-memory performance and highlight the value of reproducible computational workflows for evaluating cognitive models using open behavioral datasets.

Keywords: Visual working memory; Memory load; Precision; Continuous report task; Hierarchical Bayesian modeling; Computational cognitive modeling

# Introduction

Visual working memory (VWM) enables the temporary maintenance and manipulation of visual information to support ongoing perception, reasoning, and goal-directed behavior. Despite its central role in cognition, VWM is markedly limited in both capacity and precision. Explaining the nature of these limitations has been a major objective of cognitive psychology and cognitive neuroscience for several decades (Luck \& Vogel, 1997). A central question concerns whether performance limitations arise from a fixed number of stored representations, a limited resource distributed across items, or probabilistic mechanisms governing the fidelity of memory representations.

Early influential accounts proposed that visual working memory consists of a small number of discrete storage slots that maintain representations with relatively fixed precision (Luck \& Vogel, 1997; Zhang \& Luck, 2008). Under this framework, increasing the number of memorized items primarily reduces the probability that an item is successfully stored, whereas the precision of stored representations remains largely unchanged. Although these models successfully explained many experimental findings, subsequent evidence suggested that memory performance often changes gradually rather than categorically as memory load increases, motivating alternative theoretical accounts.

Resource-based theories instead propose that visual working memory relies on a limited representational resource that is continuously distributed across remembered items (Bays et al., 2009). As memory load increases, fewer resources are available for each representation, leading to progressively lower memory precision. Continuous-report paradigms have been particularly influential in evaluating these accounts because they provide a sensitive measure of representational fidelity. Rather than requiring binary correct-or-incorrect responses, participants reproduce a remembered stimulus feature, such as a color or orientation, on a continuous response scale. The resulting angular error provides a behavioral measure of representational precision across experimental conditions and has become a standard behavioral measure in computational studies of visual working memory (Bays et al., 2009; Zhang \& Luck, 2008).

Subsequent theoretical developments have further suggested that memory precision itself varies across trials and items rather than remaining constant. Variable-precision models propose that the representational resources allocated to individual memories fluctuate over time, producing systematic variability in recall precision even under identical experimental conditions (van den Berg et al., 2012). More broadly, contemporary perspectives increasingly characterize visual working memory as a probabilistic representational system in which uncertainty and variability are fundamental properties of memory representations rather than merely sources of measurement error (Ma et al., 2014; Bays et al., 2022; Bays et al., 2024).

These theoretical advances have been accompanied by increasing use of computational modeling to evaluate competing explanations of behavioral performance. Bayesian methods are particularly well-suited for this purpose because they estimate complete posterior distributions over model parameters while naturally quantifying uncertainty. Hierarchical Bayesian models additionally account for the multilevel structure of behavioral data by jointly estimating population-level effects and participant-specific variation through partial pooling. This approach generally yields more stable parameter estimates than fitting separate models to individual participants while preserving meaningful individual differences in cognitive performance. The Bayesian workflow further emphasizes model criticism and predictive evaluation through posterior predictive checks, convergence diagnostics, and out-of-sample model comparison rather than relying solely on statistical significance (Oberauer et al., 2018).

Although computational models are frequently used to evaluate theories of visual working memory, it is important to distinguish statistical model parameterizations from cognitive theories. A statistical model provides a quantitative description of observed behavior under a particular set of assumptions, whereas a cognitive theory proposes mechanisms that generate that behavior. Consequently, demonstrating that one statistical model predicts behavioral data better than another does not by itself establish the superiority of one cognitive theory over competing theoretical accounts. Instead, statistical models provide a principled framework for quantifying behavioral regularities and evaluating alternative representations of the data.

The increasing availability of openly accessible behavioral datasets has created new opportunities for reproducible computational research. Public datasets enable independent evaluation of modeling approaches using standardized experimental paradigms while promoting transparency and cumulative scientific progress. Continuous-report datasets are particularly valuable because they provide trial-level measurements of memory precision across multiple memory loads, making them well suited for hierarchical Bayesian analyses that simultaneously examine population-level effects and individual differences.

The present study applies hierarchical Bayesian analysis to a publicly available continuous-report dataset originally reported by van den Berg et al. (2012). The primary objective is methodological: to evaluate alternative Bayesian statistical parameterizations of memory precision using a publicly available continuous-report dataset. Specifically, the study evaluates a sequence of progressively more flexible hierarchical Bayesian models that differ in how the relationship between memory load and memory precision is parameterized. A null model serves as a baseline by assuming no effect of memory load. A hierarchical linear model estimates a population-level effect of memory load while accounting for participant-specific variability. Finally, a nonlinear hierarchical model allows memory-load effects to vary freely across set sizes without imposing a linear relationship. These models should be interpreted as alternative statistical parameterizations of the same behavioral data rather than as competing cognitive theories of visual working memory. Model performance was evaluated using leave-one-out cross-validation together with posterior predictive checks and standard Bayesian convergence diagnostics.

The study addressed three primary research questions. First, does memory precision decrease systematically as memory load increases? Second, to what extent do individuals differ in their baseline levels of memory precision? Third, does increasing statistical flexibility improve predictive performance when modeling continuous-report behavioral data? Based on previous findings from resource-based and variable-precision theories (Bays et al., 2009; van den Berg et al., 2012), it was hypothesized that memory precision would decline with increasing set size, substantial individual differences in baseline precision would be observed, and the nonlinear hierarchical model would provide the best predictive performance among the statistical models considered.

# Methods

## Dataset

The dataset contains individual trial-level responses from three continuous-report experiments originally reported by van den Berg et al. (2012) and made publicly available through the BenchmarksWM repository (Oberauer et al., 2018). The dataset contains individual trial-level responses from three continuous-report experiments examining the relationship between memory load and visual working memory precision. The experiments differed in stimulus type and response procedure while sharing a common delayed-estimation paradigm. Experiment 1 employed colored stimuli with a scrolling response method, Experiment 2 used oriented stimuli with a rotational response, and Experiment S3 used colored stimuli with a color-wheel response.

The complete dataset comprised 37,824 trials collected from 13 unique participants across 32 participant–experiment units. Memory load was manipulated by varying set size from one to eight items. On each trial, participants reproduced the remembered feature value of a target stimulus, allowing memory precision to be quantified as angular reproduction error. Because the study analyzed an existing public dataset, no additional ethical approval or participant recruitment was required.

## Measures

The primary outcome variable was absolute angular error expressed in radians. Error represented the circular distance between the target feature and the participant's response, with values ranging from 0 (perfect recall) to π radians (maximum error). Absolute error was selected because the present analyses focused on memory precision rather than directional response bias.

The principal predictor was memory load, operationalized as set size. Participant identity was included to account for repeated observations and individual differences in baseline memory precision. Experiment identifiers were retained throughout preprocessing and descriptive analyses but were not incorporated as predictors in the primary hierarchical models because the objective was to evaluate the general relationship between memory load and memory precision across the combined dataset.

Pooling the experiments increased statistical efficiency for evaluating the general relationship between memory load and memory precision. Experiment-specific analyses were conducted as robustness checks to assess whether the principal conclusions remained consistent across the individual experiments.

## Data Processing

All preprocessing and validation procedures were implemented in Python using a fully reproducible analysis pipeline. The raw dataset was first validated to ensure consistency of variable names, data types, and expected value ranges. Additional quality-control procedures verified the absence of missing observations, duplicated records, and duplicate participant–trial identifiers.

Categorical variables were converted to categorical data types, and observations were sorted by experiment, participant, and trial to ensure consistent ordering throughout subsequent analyses. Circular error measurements supplied by the original dataset were used directly without additional transformation. No observations or participants were excluded because all records satisfied the predefined validation criteria.

## Statistical Analysis

Descriptive analyses summarized the distribution of memory errors across participants, experiments, and memory loads. Summary statistics included means, medians, standard deviations, and trial counts. Because memory errors are circular measurements, circular descriptive statistics, including the circular mean, circular variance, and circular standard deviation, were additionally computed to characterize the overall distribution of response errors.

Behavioral performance across memory loads was summarized by calculating mean error at each set size. Participant-level summaries were generated to quantify individual variability in baseline memory precision. These descriptive analyses served both as an overview of the dataset and as a basis for evaluating the adequacy of the Bayesian models.

## Bayesian Models

The primary analyses employed hierarchical Bayesian modeling to estimate the relationship between memory load and memory precision while accounting for repeated observations within participants. All models used the von Mises distribution as the likelihood because angular errors constitute circular data. Although the observed outcome was absolute angular error, the models estimated the von Mises concentration parameter (κ), with larger values of κ corresponding to greater memory precision. Consequently, model-based inferences about precision are expressed in terms of κ rather than the observed error itself. Model parameters were estimated using Markov chain Monte Carlo sampling implemented in PyMC.

Three models of increasing statistical flexibility were evaluated. These models were selected to examine how progressively richer parameterizations of the relationship between memory load and memory precision influence predictive performance. The comparison was methodological rather than theoretical; the models represent alternative statistical descriptions of the observed behavioral data and should not be interpreted as competing cognitive theories of visual working memory.

### Null model

The null model served as a baseline by assuming that memory precision remained constant across memory loads. Participant-specific intercepts were modeled hierarchically to capture individual differences in baseline precision, while no effect of set size was included. Consequently, any variation in performance across memory loads was treated as unexplained by the model.

### Hierarchical linear model

The hierarchical model extended the baseline model by introducing a population-level effect of memory load. Set size was mean-centered before analysis to improve parameter interpretability and sampling efficiency. Population-level parameters estimated the average baseline precision and the average linear effect of memory load, while participant-specific intercepts accounted for individual differences through partial pooling.

The concentration parameter of the von Mises distribution was modeled on the logarithmic scale, ensuring positive precision estimates while allowing memory precision to vary systematically with memory load. Weakly informative normal priors were assigned to the population intercept and memory-load coefficient, and a half-normal prior was used for the between-participant standard deviation.

### Nonlinear hierarchical model

The nonlinear model relaxed the assumption of a linear relationship between memory load and memory precision by estimating an independent effect for each set size. Rather than imposing a predetermined functional form, each memory load was allowed to contribute a separate effect to the expected precision.

Participant effects were parameterized using a non-centered hierarchical formulation to improve sampling efficiency and reduce posterior correlations. Set-size effects were represented through unconstrained parameters that were transformed using a sum-to-zero constraint. This parameterization ensured that the population intercept represented the overall average level of precision while allowing each set size to deviate from that average without introducing parameter redundancy. The resulting model provides a flexible statistical description of nonlinear changes in memory precision while maintaining parameter identifiability.

## Model Fitting

Posterior distributions were estimated using the No-U-Turn Sampler (NUTS). Sampling was performed using the NumPyro backend within PyMC to improve computational efficiency. Each model was fitted with four independent Markov chains using 2,000 tuning iterations followed by 2,000 posterior sampling iterations per chain. A target acceptance probability of 0.95 was specified to improve sampling stability. Independent random seeds were used for robustness analyses to evaluate posterior stability across repeated model fits.

## Model Evaluation

Model convergence was evaluated using the potential scale reduction statistic (R̂), effective sample size (ESS), trace plots, and rank plots. Posterior predictive checks were used to assess the ability of each model to reproduce the principal characteristics of the observed behavioral data.

Predictive performance was compared using approximate leave-one-out cross-validation (LOO). Differences in expected log predictive density were used to evaluate relative predictive accuracy across models, while Pareto-\*k\* diagnostics were examined to identify influential observations and verify the reliability of the LOO estimates.

## Robustness Analyses

Several robustness analyses were conducted to evaluate the stability of the Bayesian inferences. Prior sensitivity analyses assessed whether posterior estimates remained consistent under alternative prior specifications. Sampling sensitivity analyses examined the effects of different sampling configurations, including longer tuning periods and higher target acceptance probabilities. Posterior stability was evaluated by fitting the primary hierarchical model using multiple random seeds and comparing the resulting posterior estimates.

Participant influence analyses were additionally performed to determine whether the principal findings were disproportionately affected by individual participants. Together, these analyses provided complementary evidence regarding the robustness of the estimated effects and the stability of the computational workflow.

# Results

## Dataset Overview

The final dataset comprised 37,824 trial-level observations obtained from three previously published continuous-report experiments involving 13 unique participants (32 participant–experiment units). All preprocessing and validation procedures were completed successfully, and no additional exclusions were required. Memory load ranged from one to eight items, providing observations across the full range of experimental conditions. Figure 1 shows the distribution of trials across set sizes, indicating that all memory-load conditions were well represented in the final dataset.

## Behavioral Results

Descriptive analyses showed that memory error increased as memory load increased. The distribution of angular error was concentrated near zero for smaller set sizes but became progressively broader at larger set sizes. Figure 2 illustrates the relationship between set size and mean angular error, demonstrating a monotonic increase in response error with increasing memory load, corresponding to a decrease in memory precision.

Participant-level summaries also revealed substantial variability in baseline precision across individuals. Although participants differed in their overall levels of precision, the pattern of increasing error with increasing set size was consistently observed across all three experiments.

## Hierarchical Bayesian Models

Three Bayesian models were fitted to the continuous-report data: a null model assuming constant memory precision across memory loads, a hierarchical linear model estimating a population-level effect of set size while accounting for participant-specific variability, and a nonlinear hierarchical model allowing independent effects for each set size.

Posterior estimates from the hierarchical model indicated a clear negative association between memory load and memory precision. The population intercept was estimated as α=0.827 (95% HDI \[0.619, 1.017]), the population effect of set size as β=−0.336 (95% HDI \[-0.343, -0.329]), and the between-participant standard deviation as σ α =0.368 (95% HDI \[0.236, 0.529]). The 95% HDI for β was entirely below zero, indicating strong posterior support for a negative association between memory load and the von Mises concentration parameter. Posterior summaries for the population parameters are reported in Table 1, and their posterior distributions are shown in Figure 3.

The nonlinear model estimated separate effects for each set size using a sum-to-zero parameterization. Posterior estimates for the set-size effects varied systematically across set sizes, with the estimated deviations ranging from 1.364 (95% HDI \[1.327, 1.398]) for set size 1 to −0.933 (95% HDI \[−0.975, −0.891]) for set size 8. These results indicate that the relationship between memory load and memory precision varied systematically across set sizes rather than being fully captured by a single linear effect.

## Individual Differences

Participant-level posterior means and 95% HDIs are presented in Figure 4. Baseline precision estimates ranged substantially across participants, indicating meaningful individual differences in visual working memory precision after accounting for the population-level effect of memory load. The hierarchical model accommodated this variability through partial pooling, allowing participant-specific estimates while borrowing information from the full sample.

## Model Adequacy

Visual posterior predictive checks indicated good agreement between the fitted models and the observed data. The posterior predictive distributions reproduced the overall distribution of response errors as well as the observed relationship between memory load and mean error across set sizes (Figure 5), suggesting that the models adequately captured the principal characteristics of the behavioral data.

All Bayesian models demonstrated satisfactory convergence. All monitored parameters achieved R^≤1.01, indicating successful convergence across Markov chains. For the nonlinear model, the minimum bulk effective sample size exceeded 979 and the minimum tail effective sample size exceeded 1,236, providing evidence of adequate posterior exploration. Trace plots and rank plots likewise showed good chain mixing and no evidence of sampling pathologies.

## Model Comparison

Leave-one-out cross-validation favored the nonlinear model over both simpler alternatives (Table 3). The nonlinear model achieved the highest expected log predictive density (ELPD<sub>LOO</sub> = −42,771.49), followed by the hierarchical model (ELPD<sub>LOO</sub> = −42,938.84; ΔELPD = 167.35) and the null model (ELPD<sub>LOO</sub> = −47,830.95; ΔELPD = 5,059.47). Stacking weights likewise favored the nonlinear model (0.871), whereas the hierarchical (0.070) and null (0.059) models received substantially less support. Pareto-k diagnostics indicated reliable leave-one-out estimates for all models, with maximum Pareto-k values below 0.30 and no observations exceeding the conventional thresholds of 0.7 or 1.0.

Posterior estimates from the nonlinear model indicated that the set-size effects varied systematically across memory loads, consistent with a non-constant relationship between memory load and memory precision. Because these parameters were estimated under a sum-to-zero constraint, they represent relative deviations from the population mean rather than absolute levels of precision.

## Robustness Analyses

Sensitivity analyses demonstrated that the principal conclusions were stable across alternative modeling specifications. Varying the prior distributions produced only negligible changes in the posterior estimates. Across primary, weak, and strong prior specifications, the estimated population effect of set size remained essentially unchanged (β=−0.336; all 95% HDIs excluded zero).

Similarly, repeated analyses using different random seeds yielded highly consistent posterior summaries, and alternative sampling configurations, including longer tuning periods and higher target acceptance rates, produced highly similar parameter estimates. Separate analyses conducted within each experiment also consistently identified a negative effect of memory load, with posterior mean estimates ranging from −0.287 to −0.377.

Participant influence analyses indicated that no individual participant disproportionately affected the overall conclusions. Detailed robustness analyses, including prior sensitivity, sampling sensitivity, posterior stability, and participant influence diagnostics, are provided in the Supplementary Material. Collectively, these analyses indicate that the reported findings were robust to reasonable modeling choices and computational settings.

# Discussion

The present study applied hierarchical Bayesian modeling to a publicly available continuous-report dataset to examine the relationship between memory load and visual working memory precision. Across descriptive analyses and Bayesian modeling, mean response error increased systematically with set size, corresponding to a decrease in estimated memory precision. Substantial individual differences in baseline precision were also observed, and the nonlinear hierarchical model achieved the best predictive performance among the candidate models. Because the primary objective of this study was methodological rather than theoretical, these findings should be interpreted as evidence regarding the predictive adequacy of alternative statistical parameterizations rather than as direct support for a particular cognitive theory of visual working memory.

The observed increase in response error, corresponding to lower estimated memory precision, with increasing memory load is consistent with a large body of previous research employing continuous-report paradigms (Bays et al., 2009; van den Berg et al., 2012). As the number of items held in memory increased, behavioral responses became progressively less precise, replicating one of the most robust empirical findings in the visual working memory literature. Although the present analyses were not designed to distinguish among competing theoretical accounts, the results are consistent with the well-established empirical observation that memory precision decreases as memory load increases.

The nonlinear hierarchical model consistently outperformed both the null model and the hierarchical linear model in predictive performance. Importantly, this result should not be interpreted as evidence for a new cognitive theory or as a direct comparison among existing theoretical models such as resource, slot, or variable-precision accounts. Rather, the nonlinear model represents a more flexible statistical parameterization that allows the relationship between memory load and precision to depart from strict linearity. Its superior predictive performance suggests that changes in memory precision across set sizes are unlikely to be fully captured by a simple linear trend. The posterior estimates indicate that the influence of memory load varies across set sizes rather than changing at a constant rate, although the present analyses were not intended to characterize the precise functional form of this relationship. Establishing the cognitive mechanisms underlying these nonlinear patterns will require direct comparisons among theoretically motivated computational models.

A second contribution of the study is methodological. Hierarchical Bayesian modeling naturally accommodates the multilevel structure of behavioral data by simultaneously estimating population-level effects and participant-specific variation. Partial pooling stabilizes individual parameter estimates while preserving meaningful differences among participants, reducing the instability that can arise when participants are analyzed independently. In addition, Bayesian inference provides full posterior distributions and credible intervals, allowing uncertainty to be quantified directly rather than relying exclusively on point estimates or null-hypothesis significance testing. Together, these characteristics make hierarchical Bayesian models well suited for the analysis of continuous-report data in cognitive psychology.

The study also demonstrates a fully reproducible computational workflow based on publicly available behavioral data and open-source software. By combining systematic data validation, Bayesian model fitting, posterior predictive checking, predictive model comparison, and transparent visualization within a single analysis pipeline, the project illustrates how open datasets can support rigorous computational investigations without requiring new data collection. Rather than proposing a novel cognitive model, the workflow provides a practical framework that can be adapted for evaluating alternative computational models using shared behavioral datasets.

An additional strength of the study is the breadth of the robustness analyses. The principal conclusions remained consistent across alternative prior specifications, independent sampling runs, and different random initializations. Furthermore, participant influence analyses indicated that no single participant disproportionately affected the overall results. Although these analyses do not guarantee that the models are correct, they increase confidence that the reported inferences are stable and are not artifacts of particular modeling choices or sampling variability. Such robustness assessments are becoming an increasingly important component of principled Bayesian workflow and contribute to the overall reliability of computational analyses.

Several limitations should be considered when interpreting the findings. First, the analyses were conducted using a secondary dataset collected for a different research objective, limiting control over the experimental design and available variables. Second, the study examined a single continuous-report paradigm, and the generalizability of the findings to other working memory tasks remains uncertain. Third, although the nonlinear model demonstrated the strongest predictive performance among the candidate models, the comparison was intentionally restricted to a small set of hierarchical statistical models rather than to competing cognitive process models. Consequently, the results should not be interpreted as evidence favoring one theoretical account of visual working memory over another. Finally, the models assume that response errors follow a von Mises distribution and therefore inherit the assumptions associated with that likelihood specification.

Future research could extend this framework by fitting established cognitive models, including resource, mixture, and variable-precision models, within a common hierarchical Bayesian framework. Applying the same reproducible workflow to additional publicly available datasets and experimental paradigms would also help determine the extent to which the present findings generalize across different working memory tasks. Such extensions would further strengthen the integration of computational modeling, open science, and reproducible statistical practice in the study of visual working memory.

# Conclusion

This study applied hierarchical Bayesian modeling to a publicly available visual working memory dataset to examine how memory precision changes with increasing memory load. Across descriptive analyses and Bayesian models, the results consistently showed that memory precision declined as set size increased and that substantial individual differences in baseline precision were present. Among the candidate models considered, the nonlinear hierarchical model provided the strongest predictive performance, suggesting that a more flexible statistical parameterization provided a better predictive description of the observed relationship than a simple linear trend.

Beyond these empirical findings, the primary contribution of the study is methodological. Rather than proposing a new cognitive theory of visual working memory, the study demonstrates a transparent and reproducible Bayesian workflow for analyzing continuous-report behavioral data. By combining hierarchical modeling, predictive model comparison, posterior predictive checking, and robustness analyses within an open-science framework, the project illustrates how publicly available datasets can be used to evaluate alternative statistical models of cognitive performance.

The workflow presented here provides a practical foundation for future computational investigations of visual working memory. Extending this framework to compare established cognitive models across multiple datasets and experimental paradigms may contribute to a more comprehensive understanding of the computational mechanisms underlying human memory performance.

# Acknowledgements

This study used publicly available data from the BenchmarksWM repository. I thank the original contributors for making the dataset accessible and supporting open research practices. I also acknowledge the open-source scientific computing community and the Python ecosystem, including the tools that enabled data processing, statistical analysis, visualization, and reproducible computational modeling.

# Data and Code Availability

The dataset analyzed in this study is publicly available through the BenchmarksWM repository. All analysis scripts, processed data files, generated figures, supplementary materials, manuscript source files, and computational environment details are publicly available in the project repository (https://github.com/erfanjaripour/working-memory-bayesian-model). It also includes the software versions, computational environment, and reproducibility materials required to reproduce the analyses. The computational workflow was developed to support transparent and reproducible research.

# References

Bays, P. M., Catalao, R. F. G., \& Husain, M. (2009). The precision of visual working memory is set by allocation of a shared resource. Journal of Vision, 9(10), 7–11. https://doi.org/10.1167/9.10.7

Bays, P. M., Ma, W. J., \& Schneegans, S. (2022). Representation and computation in working memory. Nature Reviews Neuroscience, 23, 385–401. https://doi.org/10.1038/s41583-022-00573-0

Bays, P. M., Schneegans, S., Ma, W. J., \& Brady, T. F. (2024). Theories of visual working memory: The state of the art. Nature Human Behaviour, 8, 1–17. https://doi.org/10.1038/s41562-024-01802-9

Luck, S. J., \& Vogel, E. K. (1997). The capacity of visual working memory for features and conjunctions. Nature, 390, 279–281. https://doi.org/10.1038/36846

Ma, W. J., Husain, M., \& Bays, P. M. (2014). Changing concepts of working memory. Nature Neuroscience, 17, 347–356. https://doi.org/10.1038/nn.3655

Oberauer, K., Lewandowsky, S., Awh, E., Brown, G. D. A., Conway, A., Cowan, N., Donkin, C., Farrell, S., Hitch, G. J., Hurlstone, M. J., et al. (2018). Benchmarks for models of short-term and working memory. Psychological Bulletin, 144(9), 885–958. https://doi.org/10.1037/bul0000153

van den Berg, R., Shin, H., Chou, W. C., George, R., Ma, W. J., \& Wiesman, J. (2012). Variability in encoding precision accounts for visual short-term memory limitations. Proceedings of the National Academy of Sciences, 109(22), 8780–8785. https://doi.org/10.1073/pnas.0908002107

Zhang, W., \& Luck, S. J. (2008). Discrete fixed-resolution representations in visual working memory. Nature, 453, 233–235. https://doi.org/10.1038/nature06860

Gelman, A., Vehtari, A., Simpson, D., Margossian, C. C., Carpenter, B., Yao, Y., Kennedy, L., Gabry, J., Bürkner, P.-C., \& Modrák, M. (2020). Bayesian workflow. arXiv. https://doi.org/10.48550/arXiv.2011.01808