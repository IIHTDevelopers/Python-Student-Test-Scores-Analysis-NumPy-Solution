import numpy as np
from scipy import stats

class TestScoresAnalysis:
    def __init__(self, scores):
        """Initialize NumPy array for student test scores."""
        if len(scores) == 0:
            raise ValueError("Scores data cannot be empty")
        self.scores = np.array(scores, dtype=np.int32)

    def mean_score(self):
        """Calculate and return the mean of the test scores."""
        return np.mean(self.scores)

    def median_score(self):
        """Calculate and return the median of the test scores."""
        return np.median(self.scores)


    def mode_score(self):
        """Calculate and return the mode of the test scores."""
        mode = stats.mode(self.scores, keepdims=False)[0]  # No need to index
        return mode