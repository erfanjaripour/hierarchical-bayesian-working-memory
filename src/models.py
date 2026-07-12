import numpy as np
import pymc as pm


def build_null_model(
    error,
    participant_idx,
    n_participants,
):

    with pm.Model() as model:

        alpha = pm.Normal(
            "alpha",
            mu=0.0,
            sigma=2.0,
        )

        sigma_alpha = pm.HalfNormal(
            "sigma_alpha",
            sigma=1.0,
        )

        alpha_participant = pm.Normal(
            "alpha_participant",
            mu=alpha,
            sigma=sigma_alpha,
            shape=n_participants,
        )

        log_kappa = alpha_participant[participant_idx]

        kappa = pm.math.exp(log_kappa)

        pm.VonMises(
            "error",
            mu=0.0,
            kappa=kappa,
            observed=error,
        )

    return model


def build_hierarchical_model(
    error,
    setsize,
    participant_idx,
    n_participants,
):

    setsize = np.asarray(setsize, dtype=float)
    setsize_centered = setsize - setsize.mean()

    with pm.Model() as model:

        alpha = pm.Normal(
            "alpha",
            mu=0.0,
            sigma=2.0,
        )

        beta = pm.Normal(
            "beta",
            mu=0.0,
            sigma=1.0,
        )

        sigma_alpha = pm.HalfNormal(
            "sigma_alpha",
            sigma=1.0,
        )

        alpha_participant = pm.Normal(
            "alpha_participant",
            mu=alpha,
            sigma=sigma_alpha,
            shape=n_participants,
        )

        log_kappa = (
            alpha_participant[participant_idx]
            + beta * setsize_centered
        )

        kappa = pm.math.exp(log_kappa)

        pm.VonMises(
            "error",
            mu=0.0,
            kappa=kappa,
            observed=error,
        )

    return model


def build_nonlinear_model(
    error: np.ndarray,
    setsize: np.ndarray,
    participant_idx: np.ndarray,
    n_participants: int,
):
    """
    Bayesian hierarchical nonlinear Variable Precision model.

    log(kappa_ij) =
        alpha_participant_j
        + beta_setsize_k

    Subject to:

        sum(beta_setsize) = 0

    where

        alpha_participant_j =
            alpha + sigma_alpha * alpha_offset_j
    """

    setsize_idx = setsize.astype(int) - 1

    with pm.Model() as model:

        # ---------------------------------------------------------
        # Population precision
        # ---------------------------------------------------------

        alpha = pm.Normal(
            "alpha",
            mu=0.0,
            sigma=2.0,
        )

        # ---------------------------------------------------------
        # Participant variability
        # ---------------------------------------------------------

        sigma_alpha = pm.HalfNormal(
            "sigma_alpha",
            sigma=1.0,
        )

        # ---------------------------------------------------------
        # Non-centered participant effects
        # ---------------------------------------------------------

        alpha_offset = pm.Normal(
            "alpha_offset",
            mu=0.0,
            sigma=1.0,
            shape=n_participants,
        )

        alpha_participant = pm.Deterministic(
            "alpha_participant",
            alpha + sigma_alpha * alpha_offset,
        )

        # ---------------------------------------------------------
        # Sum-to-zero set-size effects
        # ---------------------------------------------------------

        beta_raw = pm.Normal(
            "beta_raw",
            mu=0.0,
            sigma=0.5,
            shape=8,
        )

        beta_setsize = pm.Deterministic(
            "beta_setsize",
            beta_raw - pm.math.mean(beta_raw),
        )

        # ---------------------------------------------------------
        # Linear predictor
        # ---------------------------------------------------------

        log_kappa = (
            alpha_participant[participant_idx]
            + beta_setsize[setsize_idx]
        )

        kappa = pm.math.exp(log_kappa)

        # ---------------------------------------------------------
        # Likelihood
        # ---------------------------------------------------------

        pm.VonMises(
            "error",
            mu=0.0,
            kappa=kappa,
            observed=error,
        )

    return model