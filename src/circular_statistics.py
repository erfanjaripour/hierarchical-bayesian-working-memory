from typing import Any

import pandas as pd
import numpy as np

from scipy.stats import circmean, circvar, circstd


def summarize_error(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df["errorrad"]
        .describe()
        .to_frame(name="errorrad")
        .T
    )


def summarize_circular_error(df):

    errors = df["errorrad"]

    return pd.DataFrame(
        {
            "circular_mean": [
                circmean(errors, high=3.141593, low=0)
            ],
            "circular_variance": [
                circvar(errors, high=3.141593, low=0)
            ],
            "circular_std": [
                circstd(errors, high=3.141593, low=0)
            ],
        }
    )


def summarize_error_by_setsize(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("setsize")["errorrad"]
        .agg(
            count="count",
            mean="mean",
            median="median",
            std="std",
            min="min",
            max="max",
        )
        .reset_index()
    )


def summarize_error_by_participant(df: pd.DataFrame) -> pd.DataFrame:

    summary = (
        df.groupby("id")["errorrad"]
        .agg(
            count="count",
            mean_error="mean",
            median="median",
            std="std",
        )
        .reset_index()
        .rename(columns={"id": "participant"})
    )

    summary["se"] = summary["std"] / np.sqrt(summary["count"])
    summary["ci95"] = 1.96 * summary["se"]

    return summary

def summarize_error_by_experiment(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("experiment")["errorrad"]
        .agg(
            count="count",
            mean="mean",
            median="median",
            std="std",
            min="min",
            max="max",
        )
        .reset_index()
    )


def summarize_setsize(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df["setsize"]
        .value_counts()
        .sort_index()
        .rename("count")
        .rename_axis("setsize")
        .reset_index()
    )


def summarize_participants(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("experiment")["id"]
        .nunique()
        .rename("n_participants")
        .reset_index()
    )


def summarize_trials(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["experiment", "id"])
        .size()
        .rename("n_trials")
        .reset_index()
    )


def summarize_dataset(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "rows": [len(df)],
            "participants": [df["id"].nunique()],
            "experiments": [df["experiment"].nunique()],
            "trials": [len(df)],
            "variables": [df.shape[1]],
        }
    )