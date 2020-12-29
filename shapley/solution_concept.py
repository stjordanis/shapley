"""Solution Concept base class."""

import numpy as np

class SolutionConcept(object):
    """Solution Concept base class with constructor and public methods."""

    def __init__(self):
        """Creating a Solution Concept."""
        pass

    def _check_quota(self, q: float):
        """Checking for negative quota."""
        assert 0.0 <= q

    def _verify_result_shape(self, W: np.ndarray, Phi: np.ndarray):
        """Checking the shape of the Shapley value matrix."""
        assert W.shape == Phi.shape

    def _verify_distribution(self, Phi: np.ndarray):
        """Verify distribution hypothesis."""
        assert np.sum(Phi) == Phi.shape[0]

    def _run_sanity_check(self, W: np.ndarray, Phi: np.ndarray):
        """Checking the basic assumptions about the Shapley values."""
        self._verify_result_shape(W, Phi)
        self._verify_distribution(Phi)

    def get_shapley_entropy(self, Phi):
        Phi_tilde = np.mean(Phi, axis=0)
        shapley_entropy = -np.sum(Phi_tilde*np.log(Phi_tilde))
        return shapley_entropy
