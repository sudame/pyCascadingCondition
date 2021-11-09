import numpy as np


class CascadingCondition:
    def run(self, alpha: np.ndarray, baseline: np.ndarray) -> np.ndarray:
        """calc cascading condition.

        Parameters
        ----------
        alpha : np.ndarray
        baseline : np.ndarray

        Returns
        -------
        np.ndarray
        """
        I = np.identity(len(alpha))
        L = np.linalg.pinv(I - alpha)
        rho = np.array([i if i > 0 else 10 ** -10 for i in baseline])
        Lambdas = np.dot(L, rho)
        cc = np.sum(np.dot(np.dot(L, np.diag(Lambdas)), L.T).reshape(-1)) / np.sum(
            Lambdas
        )
        return cc
