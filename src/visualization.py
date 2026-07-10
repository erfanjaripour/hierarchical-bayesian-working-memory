from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_figure(
    fig: plt.Figure,
    output_dir: Path,
    filename: str,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    fig.savefig(
        output_dir / f"{filename}.png",
        dpi=300,
        bbox_inches="tight",
    )

    fig.savefig(
        output_dir / f"{filename}.pdf",
        bbox_inches="tight",
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
    errors = df["errorrad"].dropna()

    fig = plt.figure(figsize=(6, 6))

    ax = fig.add_subplot(
        111,
        projection="polar",
    )

    ax.hist(
        errors,
        bins=36,
    )

    ax.set_title("Circular Error Distribution")

    fig.tight_layout()

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