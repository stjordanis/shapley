import random
import numpy as np
from shapley.solution_concept import SolutionConcept

class PermutationSampler(SolutionConcept):

    def __init__(self, permutations: int=1000):
        self.permutations = permutations

    def _setup(self, W: np.ndarray):
        self._Phi = np.zeros(W.shape)
        self._indices = [i for i in range(W.shape[1])]

    def _run_permutations(self, W: np.ndarray, q: float):

        for _ in range(self.permutations):
            random.shuffle(self._indices)
            W_perm = W[:, self._indices]
            cum_sum = np.cumsum(W_perm, axis=1)
            pivotal = np.argmax(cum_sum>q, axis=1)
            self._Phi[np.arange(W.shape[0]), pivotal] += 1.0
        self._Phi = self._Phi/self.permutations

    def solve_game(self, W: np.ndarray, q: float) -> np.ndarray:
        r"""Solving the weigted voting game(s).

        Args:
            W (Numpy array): Weights in the games. 
            q (float): Quota in the games.

        Return Types:
            Out (PyTorch Float Tensor): (Sequence) of node features
        """
        self._check_quota(q)
        self._setup(W)
        self._run_permutations(W, q)
        self._run_sanity_check(W, self._Phi)
        return self._Phi
