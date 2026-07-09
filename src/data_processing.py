from pathlib import Path

import pandas as pd

from pandas.api.types import (
    is_string_dtype,
    is_integer_dtype,
    is_float_dtype,
)


EXPECTED_COLUMNS = [
    "experiment",
    "id",
    "trial",
    "stims",
    "response_selection",
    "setsize",
    "target",
    "response",
    "targetrad",
    "responserad",
    "devrad",
    "errorrad",
]


EXPECTED_DTYPES = {
    "experiment": "object",
    "id": "int64",
    "trial": "int64",
    "stims": "object",
    "response_selection": "object",
    "setsize": "int64",
    "target": "int64",
    "response": "int64",
    "targetrad": "float64",
    "responserad": "float64",
    "devrad": "float64",
    "errorrad": "float64",
}


def load_raw_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def validate_columns(df: pd.DataFrame) -> None:
    if list(df.columns) != EXPECTED_COLUMNS:
        raise ValueError(
            f"Column mismatch.\nExpected: {EXPECTED_COLUMNS}\nFound: {list(df.columns)}"
        )


def validate_data_types(df: pd.DataFrame) -> None:
    for column, expected in EXPECTED_DTYPES.items():

        if expected == "object":
            valid = is_string_dtype(df[column])

        elif expected == "int64":
            valid = is_integer_dtype(df[column])

        elif expected == "float64":
            valid = is_float_dtype(df[column])

        else:
            raise ValueError(f"Unsupported dtype: {expected}")

        if not valid:
            raise TypeError(
                f"{column}: expected {expected}, found {df[column].dtype}"
            )


def validate_missing_values(df: pd.DataFrame) -> None:
    missing = df.isna().sum()

    if missing.sum() > 0:
        raise ValueError(
            f"Missing values detected:\n{missing[missing > 0]}"
        )


def validate_duplicates(df: pd.DataFrame) -> None:
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        raise ValueError(
            f"{duplicates} duplicated rows detected."
        )


def validate_participants(df: pd.DataFrame) -> dict:
    participants = df.groupby("experiment")["id"].nunique()

    return {
        "total_participants": df["id"].nunique(),
        "participants_by_experiment": participants.to_dict(),
    }


def validate_trials(df: pd.DataFrame) -> dict:
    duplicate_trials = df.duplicated(
        subset=["experiment", "id", "trial"]
    ).sum()

    if duplicate_trials > 0:
        raise ValueError(
            f"{duplicate_trials} duplicate trial identifiers detected."
        )

    trials = df.groupby(
        ["experiment", "id"]
    ).size()

    return {
        "total_trials": len(df),
        "trials_per_participant_min": int(trials.min()),
        "trials_per_participant_max": int(trials.max()),
        "mean_trials_per_participant": float(trials.mean()),
    }


def validate_variables(df: pd.DataFrame) -> None:

    checks = {
        "setsize": df["setsize"].between(1, 8).all(),
        "target": df["target"].between(1, 360).all(),
        "response": df["response"].between(1, 360).all(),
        "devrad": df["devrad"].between(-3.141593, 3.141593).all(),
        "errorrad": df["errorrad"].between(0, 3.141593).all(),
    }

    invalid = [name for name, valid in checks.items() if not valid]

    if invalid:
        raise ValueError(
            f"Invalid variable ranges detected: {invalid}"
        )


def apply_transformations(df: pd.DataFrame) -> pd.DataFrame:
    processed = df.copy()

    processed["experiment"] = processed["experiment"].astype("category")
    processed["stims"] = processed["stims"].astype("category")
    processed["response_selection"] = (
        processed["response_selection"]
        .astype("category")
    )

    processed = processed.sort_values(
        ["experiment", "id", "trial"]
    ).reset_index(drop=True)

    return processed