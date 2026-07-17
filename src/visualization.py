from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import arviz as az



# Global Scientific Visualization Style


FIG_SINGLE = (3.35, 2.8)
FIG_DOUBLE = (6.9, 4.0)
FIG_DIAGNOSTIC = (8.5, 6.5)

FONT_SIZE = 9
TITLE_SIZE = 10
LABEL_SIZE = 10
TICK_SIZE = 9
LEGEND_SIZE = 9
LINE_WIDTH = 1.8

LINE_MARKER = 4
SCATTER_SIZE = 18

PLOT_MARGIN = 0.2

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": FONT_SIZE,
        "axes.labelsize": LABEL_SIZE,
        "xtick.labelsize": TICK_SIZE,
        "ytick.labelsize": TICK_SIZE,
        "legend.fontsize": LEGEND_SIZE,
        "figure.dpi": 300,
        "axes.spines.top": False,
        "axes.spines.right": False,
	"xtick.direction": "in",
	"ytick.direction": "in",
	"pdf.fonttype": 42,
	"ps.fonttype": 42,
	"svg.fonttype": "none",
	"savefig.transparent": False,
    }
)



# Figure Saving


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
        transparent=False,
        **kwargs,
    )

    plt.close(fig)



# Dataset Structure Figures


def plot_setsize_distribution(
    summary: pd.Series,
) -> plt.Figure:

    fig, ax = plt.subplots(figsize=FIG_SINGLE)

    ax.bar(
        summary.index,
        summary.values,
    )

    ax.set_xlabel("Set size")
    ax.set_ylabel("Number of trials")

    ax.grid(
        axis="y",
        alpha=0.35,
	linestyle="--",
	linewidth=0.5,
    )

    fig.set_constrained_layout(True)

    return fig



def plot_error_distribution(
    error: pd.Series,
    bins: int = 30,
) -> plt.Figure:

    fig, ax = plt.subplots(figsize=FIG_SINGLE)

    ax.hist(
        error,
        bins=bins,
        edgecolor="white",
        linewidth=0.3,
    )

    ax.set_xlabel("Error (radians)")
    ax.set_ylabel("Frequency")

    fig.set_constrained_layout(True)

    return fig



def plot_error_density(
    error: pd.Series,
) -> plt.Figure:

    fig, ax = plt.subplots(figsize=FIG_SINGLE)

    error.plot.density(ax=ax)

    ax.set_xlabel("Error (radians)")
    ax.set_ylabel("Density")

    fig.set_constrained_layout(True)

    return fig



def plot_error_distribution_by_setsize(df):

    fig, ax = plt.subplots(figsize=FIG_DOUBLE)

    for size in [1, 4, 8]:

        values = df.loc[
            df["setsize"] == size,
            "errorrad"
        ]

        ax.hist(
            values,
            bins=40,
            alpha=0.65,
            label=f"Set size {size}",
            density=True,
    	    edgecolor="white",
    	    linewidth=0.3,
        )

    ax.set_xlabel("Error magnitude (radians)")
    ax.set_ylabel("Density")

    ax.legend(
        frameon=False,
	handlelength=1.8,
    )

    ax.grid(
        alpha=0.35,
	linestyle="--",
	linewidth=0.5,
    )

    fig.set_constrained_layout(True)

    return fig



def plot_circular_error(
    df: pd.DataFrame,
) -> plt.Figure:

    errors = df["devrad"].dropna()

    fig = plt.figure(figsize=FIG_SINGLE)

    ax = fig.add_subplot(
        111,
        projection="polar",
    )

    ax.hist(
        errors,
        bins=36,
        edgecolor="white",
        linewidth=0.3,
    )

    ax.tick_params(
        axis="both",
        labelsize=6,
    )

    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)

    fig.set_constrained_layout(True)

    return fig




# Behavioral Results


def plot_error_by_setsize(
    summary: pd.DataFrame,
) -> plt.Figure:

    fig, ax = plt.subplots(figsize=FIG_SINGLE)

    ax.plot(
        summary["setsize"],
        summary["mean_error"],
        marker="o",
        markersize=LINE_MARKER,
        linewidth=LINE_WIDTH,
        solid_capstyle="round",
    )

    ax.set_xlabel("Set size")
    ax.set_ylabel("Mean error (radians)")

    ax.grid(
        alpha=0.35,
	linestyle="--",
	linewidth=0.5,
    )

    ax.set_xticks(np.arange(1, 9))

    fig.set_constrained_layout(True)

    return fig



def plot_participant_precision(summary):

    fig, ax = plt.subplots(figsize=FIG_DOUBLE)

    ax.errorbar(
        summary["id"].astype(str),
        summary["mean_error"],
        yerr=summary["std"],
        fmt="o",
        markersize=LINE_MARKER,
        capsize=3,
    )

    ax.set_xlabel("Participant")
    ax.set_ylabel("Mean error (radians)")

    ax.tick_params(
        axis="x",
    )

    plt.setp(
        ax.get_xticklabels(),
        ha="right",
    )

    ax.grid(
        axis="y",
        alpha=0.35,
	linestyle="--",
	linewidth=0.5,
    )

    fig.set_constrained_layout(True)

    return fig



def plot_experiment_setsize_error(summary):

    fig, ax = plt.subplots(figsize=FIG_DOUBLE)

    for experiment in summary["experiment"].unique():

        subset = summary[
            summary["experiment"] == experiment
        ]

        ax.plot(
            subset["setsize"],
            subset["mean_error"],
            marker="o",
            markersize=LINE_MARKER,
            linewidth=LINE_WIDTH,
            label=experiment,
            solid_capstyle="round",
        )

    ax.set_xlabel("Set size")
    ax.set_ylabel("Mean error (radians)")

    ax.legend(
        frameon=False,
	handlelength=1.8
    )

    ax.grid(
        alpha=0.35,
	linestyle="--",
	linewidth=0.5,
    )

    ax.set_xticks(np.arange(1, 9))

    fig.set_constrained_layout(True)

    return fig


# Bayesian Diagnostics


def plot_prior_predictive(
    prior_predictive,
) -> plt.Figure:

    az.plot_ppc(
        prior_predictive,
        group="prior",
    )

    fig = plt.gcf()
    fig.set_size_inches(FIG_DOUBLE)

    for ax in fig.axes:

        legend = ax.get_legend()

        if legend is not None:
            legend.remove()

        handles, labels = ax.get_legend_handles_labels()

        ax.legend(
            handles,
            labels,
            frameon=False,
            fontsize=LEGEND_SIZE,
            handlelength=1.8,
            handletextpad=0.8,
        )

        ax.set_title("")
        ax.set_xlabel("Error (radians)")
        ax.set_ylabel("Density")

        ax.tick_params(labelsize=TICK_SIZE)

        ax.grid(
            alpha=0.35,
            linestyle="--",
            linewidth=0.5,
        )

    fig.tight_layout(pad=0.5)

    return fig



def plot_trace(idata, var_names):

    az.plot_trace(
        idata,
        var_names=var_names,
        figsize=FIG_DIAGNOSTIC,
    )

    fig = plt.gcf()

    fig = plt.gcf()

    for ax in fig.axes:
        ax.set_title(ax.get_title(), fontsize=TITLE_SIZE)
        ax.xaxis.label.set_fontsize(LABEL_SIZE)
        ax.yaxis.label.set_fontsize(LABEL_SIZE)
        ax.tick_params(labelsize=TICK_SIZE)

    fig.tight_layout(pad=0.5)
    fig.subplots_adjust(hspace=0.6, wspace=0.3)

    return fig



def plot_posterior(
    idata,
    var_names,
) -> plt.Figure:

    az.plot_posterior(
        idata,
        var_names=var_names,
        figsize=FIG_DOUBLE,
    )

    fig = plt.gcf()

    for ax in fig.axes:
        ax.set_title(ax.get_title(), fontsize=TITLE_SIZE)
        ax.xaxis.label.set_fontsize(LABEL_SIZE)
        ax.yaxis.label.set_fontsize(LABEL_SIZE)
        ax.tick_params(labelsize=TICK_SIZE)

    fig.tight_layout(pad=0.5)

    return fig


def plot_posterior_predictive(
    posterior_predictive,
) -> plt.Figure:

    az.plot_ppc(posterior_predictive)

    fig = plt.gcf()
    fig.set_size_inches(FIG_DOUBLE)

    for ax in fig.axes:
        ax.set_title("")
        ax.set_xlabel("Error (radians)")
        ax.set_ylabel("Density")

        ax.tick_params(labelsize=TICK_SIZE)
        ax.xaxis.label.set_size(LABEL_SIZE)
        ax.yaxis.label.set_size(LABEL_SIZE)

        ax.grid(
            alpha=0.35,
            linestyle="--",
            linewidth=0.5,
        )

        ax.legend(
            frameon=False,
            fontsize=LEGEND_SIZE,
            handlelength=1.8,
        )

    fig.tight_layout(pad=0.5)

    return fig



def plot_setsize_posterior_predictive(
    set_sizes,
    observed_means,
    predicted_mean,
    predicted_hdi,
) -> plt.Figure:

    fig, ax = plt.subplots(
        figsize=FIG_DOUBLE
    )

    ax.plot(
        set_sizes,
        observed_means,
        marker="o",
        markersize=LINE_MARKER,
        linewidth=LINE_WIDTH,
        solid_capstyle="round",
        label="Observed",
    )

    ax.plot(
        set_sizes,
        predicted_mean,
        marker="o",
        markersize=LINE_MARKER,
        linewidth=LINE_WIDTH,
        solid_capstyle="round",
        label="Posterior mean",
    )

    ax.fill_between(
        set_sizes,
        predicted_hdi[:, 0],
        predicted_hdi[:, 1],
        alpha=0.35,
        label="95% HDI",
    )

    ax.set_xlabel("Set size")
    ax.set_ylabel("Mean error (radians)")

    ax.legend(
        frameon=False,
	handlelength=1.8
    )

    ax.grid(
        alpha=0.35,
	linestyle="--",
	linewidth=0.5,
    )

    ax.set_xticks(np.arange(1, 9))

    fig.set_constrained_layout(True)

    return fig



def plot_rank(
    idata,
    var_names,
) -> plt.Figure:

    az.plot_rank(
        idata,
        var_names=var_names,
        figsize=FIG_DIAGNOSTIC,
        kind="bars",
    )

    fig = plt.gcf()

    for ax in fig.axes:
        ax.set_title(ax.get_title().replace("\n", " "), fontsize=TITLE_SIZE)
        ax.xaxis.label.set_fontsize(LABEL_SIZE)
        ax.yaxis.label.set_fontsize(LABEL_SIZE)
        ax.tick_params(labelsize=TICK_SIZE)

    fig.tight_layout(pad=0.5)
    fig.subplots_adjust(hspace=0.8, wspace=0.4)

    return fig


# Model Validation


def plot_participant_ppc(
    observed,
    predicted,
) -> plt.Figure:

    fig, ax = plt.subplots(
        figsize=FIG_SINGLE
    )

    ax.scatter(
        observed,
        predicted,
        s=SCATTER_SIZE,
    )

    lims = [
        min(observed + predicted),
        max(observed + predicted),
    ]

    ax.plot(
        lims,
        lims,
        linestyle="--",
        solid_capstyle="round",
    )

    ax.set_xlabel(
        "Observed mean error"
    )

    ax.set_ylabel(
        "Predicted mean error"
    )

    ax.grid(
        alpha=0.35,
	linestyle="--",
	linewidth=0.5,
    )

    fig.set_constrained_layout(True)

    return fig



def plot_residuals(
    setsize,
    residuals,
) -> plt.Figure:

    fig, ax = plt.subplots(
        figsize=FIG_SINGLE
    )

    ax.scatter(
        setsize,
        residuals,
        alpha=0.35,
        s=15,
    )

    ax.axhline(
        0,
        linestyle="--",
    )

    ax.set_xlabel(
        "Set size"
    )

    ax.set_ylabel(
        "Observed − Predicted"
    )

    ax.grid(
        alpha=0.35,
	linestyle="--",
	linewidth=0.5,
    )

    fig.set_constrained_layout(True)

    return fig




# Robustness Analysis


def plot_participant_influence(
    participant_influence,
):

    fig, ax = plt.subplots(
        figsize=FIG_DOUBLE
    )

    ax.scatter(
        participant_influence["participant"],
        participant_influence["mean_error"],
        s=SCATTER_SIZE,
    )

    ax.set_xlabel(
        "Participant"
    )

    ax.set_ylabel(
        "Mean error (radians)"
    )

    ax.grid(
        alpha=0.35,
	linestyle="--",
	linewidth=0.5,
    )

    fig.set_constrained_layout(True)

    return fig



def plot_posterior_stability(
    stability_results,
):

    fig, ax = plt.subplots(
        figsize=FIG_DOUBLE
    )

    parameters = stability_results["parameter"].unique()
    x = np.arange(len(parameters))

    offsets = {
        42: -0.15,
        123: 0.00,
        456: 0.15,
    }

    for seed in stability_results["seed"].unique():

        subset = (
            stability_results[
                stability_results["seed"] == seed
            ]
            .set_index("parameter")
            .loc[parameters]
            .reset_index()
        )

        ax.errorbar(
            x + offsets.get(seed, 0.0),
            subset["mean"],
            yerr=[
                subset["mean"] - subset["hdi_3%"],
                subset["hdi_97%"] - subset["mean"],
            ],
            fmt="o",
            markersize=LINE_MARKER,
            capsize=3,
            linewidth=1.5,
            label=f"Seed {seed}",
        )

    ax.set_xticks(x)
    ax.set_xticklabels(
        parameters,
    )

    ax.set_xlabel("Parameter")
    ax.set_ylabel("Posterior estimate")

    ax.legend(
        frameon=False,
        handlelength=1.8,
    )

    ax.grid(
        axis="y",
        alpha=0.35,
        linestyle="--",
        linewidth=0.5,
    )

    fig.set_constrained_layout(True)

    return fig