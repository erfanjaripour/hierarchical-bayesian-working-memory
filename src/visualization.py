from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import arviz as az


def save_figure(
    fig: plt.Figure,
    output_dir: Path,
    filename: str,
    **kwargs,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig.savefig(
        output_dir / f"{filename}.png",
        dpi=300,
        bbox_inches="tight",
        **kwargs,
    )

    fig.savefig(
        output_dir / f"{filename}.pdf",
        bbox_inches="tight",
        **kwargs,
    )

    plt.close(fig)


def plot_setsize_distribution(
    summary: pd.Series,
) -> plt.Figure:

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(
        summary.index,
        summary.values,
    )

    ax.set_xlabel("Set size")
    ax.set_ylabel("Number of trials")
    ax.set_title("Set Size Distribution")

    return fig


def plot_error_distribution(
    error: pd.Series,
    bins: int = 30,
) -> plt.Figure:

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.hist(
        error,
        bins=bins,
    )

    ax.set_xlabel("Error (radians)")
    ax.set_ylabel("Frequency")
    ax.set_title("Error Distribution")

    return fig


def plot_error_density(
    error: pd.Series,
) -> plt.Figure:

    fig, ax = plt.subplots(figsize=(6, 4))

    error.plot.density(ax=ax)

    ax.set_xlabel("Error (radians)")
    ax.set_ylabel("Density")
    ax.set_title("Error Density")

    return fig


def plot_error_distribution_by_setsize(df):

    fig, ax = plt.subplots(figsize=(7,4))

    for size in [1,4,8]:
        values = df.loc[
            df["setsize"] == size,
            "errorrad"
        ]

        ax.hist(
            values,
            bins=40,
            alpha=0.5,
            label=f"Set size {size}",
            density=True,
        )

    ax.set_xlabel("Error magnitude (radians)")
    ax.set_ylabel("Density")
    ax.legend()

    return fig


def plot_circular_error(
    df: pd.DataFrame,
) -> plt.Figure:

    errors = df["devrad"].dropna()

    fig = plt.figure(figsize=(6, 6))

    ax = fig.add_subplot(
        111,
        projection="polar",
    )

    ax.hist(
        errors,
        bins=36,
    )

    return fig

def plot_error_by_setsize(
    summary: pd.DataFrame,
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(
        summary["setsize"],
        summary["mean_error"],
        marker="o",
    )

    ax.set_xlabel("Set size")
    ax.set_ylabel("Mean error (radians)")
    ax.set_title("Error by Set Size")

    fig.tight_layout()

    return fig


def plot_participant_precision(summary):

    fig, ax = plt.subplots(figsize=(8,4))

    ax.errorbar(
        summary["id"].astype(str),
        summary["mean_error"],
        yerr=summary["std"],
        fmt="o",
    )

    ax.set_xlabel("Participant")
    ax.set_ylabel("Mean error (radians)")
    ax.tick_params(axis="x", rotation=90)

    return fig


def plot_experiment_setsize_error(summary):

    fig, ax = plt.subplots(figsize=(7,4))

    for experiment in summary["experiment"].unique():

        subset = summary[
            summary["experiment"] == experiment
        ]

        ax.plot(
            subset["setsize"],
            subset["mean_error"],
            marker="o",
            label=experiment,
        )

    ax.set_xlabel("Set size")
    ax.set_ylabel("Mean error (radians)")
    ax.legend()

    return fig


def plot_prior_predictive(
    prior_predictive,
) -> plt.Figure:
    az.plot_ppc(
        prior_predictive,
        group="prior",
    )

    return plt.gcf()


def plot_trace(
    idata,
    var_names,
) -> plt.Figure:
    az.plot_trace(
        idata,
        var_names=var_names,
        figsize=(10, 6),
    )

    plt.subplots_adjust(
        hspace=0.6,
        wspace=0.4,
    )

    return plt.gcf()


def plot_posterior(
    idata,
    var_names,
) -> plt.Figure:
    az.plot_posterior(
        idata,
        var_names=var_names,
    )

    return plt.gcf()


def plot_posterior_predictive(
    posterior_predictive,
) -> plt.Figure:
    az.plot_ppc(
        posterior_predictive,
    )

    return plt.gcf()


def plot_setsize_posterior_predictive(
    set_sizes,
    observed_means,
    predicted_mean,
    predicted_hdi,
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot(
        set_sizes,
        observed_means,
        marker="o",
        linewidth=2,
        label="Observed",
    )

    ax.plot(
        set_sizes,
        predicted_mean,
        marker="o",
        linewidth=2,
        label="Posterior mean",
    )

    ax.fill_between(
        set_sizes,
        predicted_hdi[:, 0],
        predicted_hdi[:, 1],
        alpha=0.25,
        label="95% HDI",
    )

    ax.set_xlabel("Set Size")
    ax.set_ylabel("Mean Error (radians)")
    ax.legend()

    return fig


def plot_rank(
    idata,
    var_names,
) -> plt.Figure:
    az.plot_rank(
        idata,
        var_names=var_names,
    )

    return plt.gcf()


def plot_participant_ppc(
    observed,
    predicted,
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7, 5))

    ax.scatter(
        observed,
        predicted,
    )

    lims = [
        min(observed + predicted),
        max(observed + predicted),
    ]

    ax.plot(
        lims,
        lims,
        "--",
    )

    ax.set_xlabel("Observed Mean Error")
    ax.set_ylabel("Predicted Mean Error")

    return fig


def plot_residuals(
    setsize,
    residuals,
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7, 5))

    ax.scatter(
        setsize,
        residuals,
        alpha=0.2,
    )

    ax.axhline(
        0,
        linestyle="--",
    )

    ax.set_xlabel("Set Size")
    ax.set_ylabel("Observed − Predicted")

    return fig


def plot_participant_influence(
    participant_influence,
):
    """
    Plot participant-level influence diagnostics.

    Parameters
    ----------
    participant_influence : pandas.DataFrame
        Must contain:
        - participant
        - mean_error
        - uncertainty (optional)

    Returns
    -------
    matplotlib.figure.Figure
    """

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(
        participant_influence["participant"],
        participant_influence["mean_error"],
    )

    ax.set_xlabel("Participant")
    ax.set_ylabel("Mean Error")
    ax.set_title("Participant Influence Diagnostics")

    return fig



def plot_posterior_stability(
    stability_results,
):
    """
    Plot posterior stability across independent sampling runs.

    Parameters
    ----------
    stability_results : pandas.DataFrame
        Must contain:
        - parameter
        - mean
        - hdi_3%
        - hdi_97%
        - seed

    Returns
    -------
    matplotlib.figure.Figure
    """

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))

    seeds = stability_results["seed"].unique()

    for seed in seeds:

        subset = stability_results[
            stability_results["seed"] == seed
        ]

        ax.errorbar(
            subset["parameter"],
            subset["mean"],
            yerr=[
                subset["mean"] - subset["hdi_3%"],
                subset["hdi_97%"] - subset["mean"],
            ],
            fmt="o",
            label=f"Seed {seed}",
        )

    ax.set_ylabel("Posterior Estimate")
    ax.set_title("Posterior Stability Across Seeds")
    ax.legend()

    return fig